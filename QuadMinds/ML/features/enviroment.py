from ML.commons import Driver


def after_all(context):
    context.driver.close()