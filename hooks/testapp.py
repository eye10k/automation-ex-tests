from pages.home_page import HomePage

def initialize_home_page(context):
    print("initialize_home_page")
    context.home_page = HomePage(context.page)
    context.home_page.navigate_to_home()
    context.home_page.verify_home_page_loaded()