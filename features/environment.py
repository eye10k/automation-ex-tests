from hooks.browser import setup_browser, teardown_browser
from hooks.screenshot import attach_screenshot_if_failed
from hooks.testapp import initialize_home_page

def before_scenario(context, scenario):
   # if "ui" in scenario.effective_tags:
        setup_browser(context)
        initialize_home_page(context)

def after_scenario(context, scenario):
    if hasattr(context, "page"):
        teardown_browser(context, scenario)

def after_step(context, step):
    attach_screenshot_if_failed(context, step)