

from utilities import configReader
import logging
import allure
from utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)



class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self,locator):
        with allure.step(f"Clicking on an Element: {locator}"):
            self.page.locator(configReader.readConfig("locator", locator)).click()
            log.logger.info(f"Clicking on {locator}")

    def type(self, locator, value):
        with allure.step(f"Typing on {locator} and entered {value}"):
            self.page.locator(configReader.readConfig("locator", locator)).fill(value)
            log.logger.info(f"Typing on {locator} and entered {value}")

    def move_to(self,locator):
        with allure.step(f"Moving to an Element {locator}"):
            self.page.locator(configReader.readConfig("locator", locator)).hover()
            log.logger.info(f"Moving to an Element {locator}")

    def select(self, locator, value):
        xpath = configReader.readConfig("locator", locator)
        with allure.step(f"Selecting {value} from {locator}"):
            self.page.locator(xpath).select_option(value)
            log.logger.info(f"Selected {value} from {locator}")

    def is_visible(self,locator):

        return self.page.locator(configReader.readConfig("locator", locator)).is_visible

    def get_attribute(self,locator,attribute):
        return self.page.locator(configReader.readConfig("locator", locator)).get_attribute(attribute)

    def get_text(self, locator):
        with allure.step(f"Getting text of {locator}"):
            value = self.page.locator(configReader.readConfig("locator", locator)).text_content()
        log.logger.info(f"Text of {locator}: {value}")
        return value