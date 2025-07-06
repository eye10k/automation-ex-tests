import pytest
import allure
import subprocess
import sys
import os
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    # Добавляем с уникальным именем, чтобы избежать конфликта
    parser.addoption(
        "--my-headed",
        action="store_true",
        default=False,
        help="Run tests with headed browser",
    )



@pytest.fixture(scope="session")
def browser(request):
    headed = request.config.getoption("--my-headed")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headed)
        yield browser
        browser.close()



@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    context.tracing.stop(path="trace.zip")
    context.close()


@pytest.fixture(scope="function")
def page(context, request):
    page = context.new_page()
    yield page

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshot = page.screenshot(full_page=True)
        allure.attach(screenshot, name="Failure Screenshot", attachment_type=AttachmentType.PNG)

    page.close()


def pytest_runtest_makereport(item, call):
    if call.when == "call":
        setattr(item, "rep_call", call)


# Автооткрытие Allure-отчёта после завершения всех тестов
def pytest_sessionfinish(session, exitstatus):

    if not os.getenv("CI"):
        print("\n[INFO] Generating Allure report...")
        try:
            subprocess.run(["allure", "generate", "allure-results", "-o", "allure-report", "--clean"], check=True)
            print("[INFO] Opening Allure report in browser...")
            if sys.platform.startswith("win"):
                os.startfile("allure-report/index.html")
            elif sys.platform.startswith("darwin"):
                subprocess.run(["open", "allure-report/index.html"])
            else:
                subprocess.run(["xdg-open", "allure-report/index.html"])
        except Exception as e:
            print(f"[ERROR] Failed to generate or open Allure report: {e}")
