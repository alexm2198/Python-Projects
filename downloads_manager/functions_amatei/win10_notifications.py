from win10toast import ToastNotifier


def win10toast_notifier(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message)
