import browser
import time


def search_input():
    search=input("Press a username  ")
    return str(search)


def main():
    search=search_input()
    time.sleep(1)
    browser.Browser(str(search))

main()
