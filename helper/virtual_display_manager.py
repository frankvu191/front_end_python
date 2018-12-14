from pyvirtualdisplay import Display


def start_virtual_display(context):
    context.display = Display(visible=0, size=(1024, 768))
    context.display.start()


def stop_virtual_display(context):
    context.display.stop()
