from behave import fixture, use_fixture


def before_all(context):
    pass


def after_scenario(context, scenario):
    context.driver.quit()


def after_all(context):
    pass