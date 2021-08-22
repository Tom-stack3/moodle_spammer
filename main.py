import time
from datetime import datetime
from selenium.webdriver import Firefox
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


def launce_and_login(link_to_login):
    login_info = open("login.txt", "r")
    USERNAME = login_info.readline()
    PASS = login_info.readline()

    # to make the window invisible
    '''
    # import needed:
    from selenium.webdriver.firefox.options import Options
    
    opts = Options()
    opts.headless = False
    assert opts.headless  # Operating in headless mode
    driver = Firefox(options=opts)
    '''

    driver = Firefox()
    driver.get(link_to_login)

    # wait 2 seconds to press the username input box
    time.sleep(2)

    element = driver.find_element_by_xpath('//*[@id="login_username"]')
    element.send_keys(USERNAME)
    element = driver.find_element_by_xpath('//*[@id="login_password"]')
    element.send_keys(PASS)
    element.send_keys(Keys.ENTER)

    # wait 2 seconds to log in
    time.sleep(2)

    return driver


def send_msg(browser, text):
    chat_textbox = browser.find_element_by_xpath('//*[@data-region="send-message-txt"]')
    chat_textbox.send_keys(text)

    chat_send_btn = browser.find_element_by_xpath('//*[@data-region="send-icon-container"]')
    chat_send_btn.click()


def get_chat_ready(browser, person):
    time.sleep(2)

    chat_btn = browser.find_element_by_xpath('//*[@title="הצגת/הסתרת תפריט מסרים"]')
    chat_btn.click()

    time.sleep(2)

    chat_search = browser.find_element_by_xpath('//*[@data-region="view-overview-search-input"]')
    chat_search.send_keys(person + Keys.ENTER)

    time.sleep(8)

    browser.find_element_by_xpath('//*[@data-route="view-conversation"]').click()

    time.sleep(5)


def main():
    messages_to_send = 15
    start_time = time.time()
    link_to_login = "https://lemida.biu.ac.il/blocks/login_ldap/index.php"

    # Login and get the browser.
    browser = launce_and_login(link_to_login)

    f = open("login.txt", "r")
    person = f.readline()
    get_chat_ready(browser, person)

    for i in range(messages_to_send):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        text = "ah yes " + ' ' + str(i + 1)
        print(text)
        send_msg(browser, text)
        time.sleep(5)

    print("--- run ended ---\n")
    minutes_took = (time.time() - start_time) / 60
    print("run ended after:", minutes_took, "minutes")

    # Close the browser
    browser.close()


if __name__ == '__main__':
    main()
