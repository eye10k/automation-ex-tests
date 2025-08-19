import logging
import allure
import json
from utilities.log_util import Logger
from allure_commons.types import AttachmentType
from config.config import Config

log = Logger(__name__, logging.INFO)

class BasePage:

    def __init__(self, page):
        self.page = page
        self.base_url = Config.BASE_URL

    def open(self, path=""):
        """Открыть страницу по относительному пути"""
        self.page.goto(f"{self.base_url}/{path.lstrip('/')}")

    def _attach_locator_info(self, locator, value=None):
        allure.attach(
            str(locator),
            name="Locator",
            attachment_type=AttachmentType.TEXT
        )
        if value is not None:
            allure.attach(
                str(value),
                name="Value",
                attachment_type=AttachmentType.TEXT
            )

    def click(self, locator, timeout=10000):
        with allure.step(f"Click element"):
            self._attach_locator_info(locator)
            self.page.wait_for_selector(locator, state="visible", timeout=timeout)
            self.page.locator(locator).click()
            log.logger.info(f"Clicked on {locator}")

    def type(self, locator, value, timeout=10000):
        with allure.step(f"Type into element"):
            self._attach_locator_info(locator, value)
            self.page.wait_for_selector(locator, state="visible", timeout=timeout)
            self.page.locator(locator).fill(value)
            log.logger.info(f"Typed '{value}' into {locator}")

    def move_to(self, locator, timeout=10000):
        with allure.step(f"Move to element"):
            self._attach_locator_info(locator)
            self.page.wait_for_selector(locator, state="visible", timeout=timeout)
            self.page.locator(locator).hover()
            log.logger.info(f"Moved to {locator}")

    def select(self, locator, value, timeout=10000):
        with allure.step(f"Select option"):
            self._attach_locator_info(locator, value)
            self.page.wait_for_selector(locator, state="visible", timeout=timeout)
            self.page.locator(locator).select_option(value)
            log.logger.info(f"Selected '{value}' from {locator}")

    def is_visible(self, locator, timeout=5000):
        try:
            self.page.wait_for_selector(locator, state="visible", timeout=timeout)
            visible = True
        except TimeoutError:
            visible = False
        log.logger.info(f"Element {locator} visible: {visible}")
        allure.attach(
            json.dumps({"locator": locator, "visible": visible}, indent=2),
            name="Visibility Check",
            attachment_type=AttachmentType.JSON
        )
        return visible

    def get_attribute(self, locator, attribute, timeout=5000):
        with allure.step(f"Get attribute"):
            self._attach_locator_info(locator, attribute)
            self.page.wait_for_selector(locator, timeout=timeout)
            attr = self.page.locator(locator).get_attribute(attribute)
            log.logger.info(f"Got attribute '{attribute}' of {locator}: {attr}")
            return attr

    def get_text(self, locator, timeout=5000):
        with allure.step(f"Get text"):
            self._attach_locator_info(locator)
            self.page.wait_for_selector(locator, timeout=timeout)
            value = self.page.locator(locator).text_content()
            log.logger.info(f"Text of {locator}: {value}")
            allure.attach(
                value if value else "None",
                name="Element Text",
                attachment_type=AttachmentType.TEXT
            )
            return value
