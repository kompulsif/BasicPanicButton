from pynput.keyboard import Listener
from webbrowser import open as openUrl


panic_button = None
panic_func = None
panic_url = None


def check_key(k):
    global panic_button

    if (not panic_button):
        panic_button = k
        print('[ Panic button selected, please enjoy yourself! ]')

    elif (k == panic_button):
        panic_func()
        return False


def keylogger():
    with Listener(on_press=check_key) as listener:
        print('[ Firstly, please press/choose panic button ]\r', end='')
        listener.join()


def open_web_site():
    openUrl(panic_url)


def main():
    global panic_func, panic_url

    while True:

        enter_url = input('Enter url: ').strip()
        if (enter_url == 'q'):
            break

        elif (enter_url.startswith('https://') or enter_url.startswith('http://')):
            panic_url = enter_url
            panic_func = open_web_site
            l = False
            break

        else:
            print('\n[!]-> Invalid url address, Ex: https://www.google.com <-[!]\n')

    keylogger()


if __name__ == '__main__':
    main()
