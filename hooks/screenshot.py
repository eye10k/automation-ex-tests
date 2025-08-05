import allure
from allure_commons.types import AttachmentType

def attach_screenshot_if_failed(context, step):
    if step.status == "failed":
        screenshot = context.page.screenshot()
        allure.attach(screenshot, name="step-failed", attachment_type=AttachmentType.PNG)
