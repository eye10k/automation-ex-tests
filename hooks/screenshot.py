import allure
from allure_commons.types import AttachmentType
import os
from datetime import datetime

os.makedirs("screenshots", exist_ok=True)

def attach_screenshot(context, step, always=False):
    """
    Takes a screenshot of the step.
    :param always: True — always, False — only when falling.
    """
    if always or step.status == "failed":
        screenshot_path = f"screenshots/{datetime.now().strftime('%Y%m%d_%H%M%S')}_{step.name}.png"
        context.page.screenshot(path=screenshot_path, full_page=True)
        allure.attach.file(screenshot_path, name=f"Screenshot - {step.name}", attachment_type=AttachmentType.PNG)

def attach_screenshot_if_failed(context, step):
    """Screenshot only when falling (old method, in case it is used separately)."""
    attach_screenshot(context, step, always=False)
