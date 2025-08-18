from playwright.sync_api import sync_playwright

def setup_browser(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()

def teardown_browser(context, scenario):
    context.page.close()
    context.browser.close()
    context.playwright.stop()