import logging
import allure
from utilities.log_util import Logger

log = Logger(__name__, logging.INFO)

class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator, timeout=10000):
        with allure.step(f"Clicking on element: {locator}"):
            self.page.wait_for_selector(locator, state="visible", timeout=timeout)
            self.page.locator(locator).click()
            log.logger.info(f"Clicked on {locator}")

    def type(self, locator, value, timeout=10000):
        with allure.step(f"Typing '{value}' into element: {locator}"):
            self.page.wait_for_selector(locator, state="visible", timeout=timeout)
            self.page.locator(locator).fill(value)
            log.logger.info(f"Typed '{value}' into {locator}")

    def move_to(self, locator, timeout=10000):
        with allure.step(f"Moving to element: {locator}"):
            self.page.wait_for_selector(locator, state="visible", timeout=timeout)
            self.page.locator(locator).hover()
            log.logger.info(f"Moved to {locator}")

    def select(self, locator, value, timeout=10000):
        with allure.step(f"Selecting '{value}' from element: {locator}"):
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
        return visible

    def get_attribute(self, locator, attribute, timeout=5000):
        with allure.step(f"Getting attribute '{attribute}"):
            self.page.wait_for_selector(locator, timeout=timeout)
            attr = self.page.locator(locator).get_attribute(attribute)
            log.logger.info(f"Got attribute '{attribute}' of {locator}: {attr}")
            return attr

    def get_text(self, locator, timeout=5000):
        with allure.step(f"Getting text of element: {locator}"):
            self.page.wait_for_selector(locator, timeout=timeout)
            value = self.page.locator(locator).text_content()
            log.logger.info(f"Text of {locator}: {value}")
            return value
