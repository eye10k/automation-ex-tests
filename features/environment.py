import os
import re
import logging
import allure
from allure_commons.types import AttachmentType
from utilities.log_util import Logger
from playwright.sync_api import sync_playwright

log = Logger(__name__, logging.INFO)

ART_DIR = "artifacts"
os.makedirs(ART_DIR, exist_ok=True)

def _safe_name(name: str) -> str:
    # безопасное имя файла для Windows/macOS/Linux
    return re.sub(r"[^-\w]+", "_", name).strip("_")[:80]

def before_all(context):
    log.logger.info("=== TEST RUN STARTED ===")

def before_scenario(context, scenario):
    # Логирование только для UI-сценариев
    if "ui" not in getattr(scenario, "effective_tags", []):
        return

    scen = _safe_name(scenario.name)
    log.logger.info(f"Starting scenario: {scenario.name}")

    # Запуск Playwright
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)

    # Создаём BrowserContext с HAR-записью
    context.browser_context = context.browser.new_context(
        record_har_path=os.path.join(ART_DIR, f"{scen}.har")
    )
    context.page = context.browser_context.new_page()

    # Включаем Playwright trace (остановим в after_scenario)
    context.browser_context.tracing.start(screenshots=True, snapshots=True, sources=True)

    # Подписка на консоль браузера (копим, а в шагах отдаём дельту)
    context._console_logs = []
    context._console_cursor = 0

    def _on_console(msg):
        # msg.type, msg.text
        try:
            context._console_logs.append(f"{msg.type}: {msg.text}")
        except Exception:
            pass

    context.page.on("console", _on_console)

def before_step(context, step):
    if not hasattr(context, "page"):
        return

    try:
        # Текущий URL
        current_url = context.page.url
        log.logger.info(f"Step STARTED: {step.name} | URL: {current_url}")
        allure.attach(current_url, name="Current URL", attachment_type=AttachmentType.TEXT)

        # Дельта console logs с прошлого шага
        if hasattr(context, "_console_logs"):
            new_logs = context._console_logs[context._console_cursor:]
            context._console_cursor = len(context._console_logs)
            if new_logs:
                allure.attach(
                    "\n".join(new_logs),
                    name="Console Logs (delta)",
                    attachment_type=AttachmentType.TEXT
                )
    except Exception as e:
        log.logger.warning(f"before_step logging failed: {e}")


def after_step(context, step):
    if not hasattr(context, "page"):
        return

    # Скриншот после каждого шага
    try:
        scen_step = _safe_name(step.name)
        screenshot_path = os.path.join(ART_DIR, f"{scen_step}.png")
        context.page.screenshot(path=screenshot_path, full_page=True)
        allure.attach.file(
            screenshot_path,
            name=f"Screenshot - {step.name}",
            attachment_type=AttachmentType.PNG
        )
    except Exception as e:
        log.logger.warning(f"Screenshot failed: {e}")

    # Статус шага в файл-лог
    log.logger.info(f"Step FINISHED: {step.name} [{step.status}]")


def after_scenario(context, scenario):
    if not hasattr(context, "browser_context"):
        return

    scen = _safe_name(scenario.name)
    log.logger.info(f"Finishing scenario: {scenario.name}")

    # Останавливаем trace и прикрепляем в Allure
    try:
        trace_path = os.path.join(ART_DIR, f"{scen}_trace.zip")
        context.browser_context.tracing.stop(path=trace_path)
        if os.path.exists(trace_path):
            # В allure-python нет AttachmentType.ZIP — используем TEXT (файл всё равно приложится как загрузка)
            allure.attach.file(trace_path, name="Playwright Trace", attachment_type=AttachmentType.TEXT)
    except Exception as e:
        log.logger.warning(f"Could not save Playwright trace: {e}")

    # Прикрепляем HAR (он уже записан самим контекстом)
    try:
        har_path = os.path.join(ART_DIR, f"{scen}.har")
        if os.path.exists(har_path):
            # HAR — это JSON, его можно читать прямо в Allure
            allure.attach.file(har_path, name="HAR Log", attachment_type=AttachmentType.JSON)
    except Exception as e:
        log.logger.warning(f"Could not attach HAR: {e}")

    # Закрываем браузер/Playwright
    try:
        context.browser_context.close()
        context.browser.close()
        context.playwright.stop()
    except Exception as e:
        log.logger.warning(f"Could not close browser: {e}")
