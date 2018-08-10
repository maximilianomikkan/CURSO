from behave import fixture, use_fixture


def before_all(context):
    pass


def after_all(context):
    # close the browser window
    context.driver.quit()