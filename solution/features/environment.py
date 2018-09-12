from behave import fixture, use_fixture


def before_all(context):
    pass

# TODO: Mover la logica del nombre del screenshot a un helper
# obtener el nombre relativo del proyecto*(pedimelo)

def after_scenario(context, scenario):
    import datetime
    date = datetime.datetime.now()
    myDate = date.today()
    myTime = date.today().time()
    dateString = str(myDate.month) + "-" + str(myDate.day) + "-" + str(myDate.year) + " - " + str(
        myTime.hour) + ":" + str(myTime.minute) + ":" + str(myTime.second)
    context.driver.save_screenshot(
        "/Users/maximacbook/Repositorio/solution/screenshots/" + dateString + " - " + scenario.name + ".png")

    context.driver.quit()


def after_all(context):
    pass