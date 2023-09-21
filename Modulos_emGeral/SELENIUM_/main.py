from make_chrome_browser_ import make_chrome_browser
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support. wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIME_TO_WAIT = 10

options = ()
browser = make_chrome_browser(*options)


browser.get('https://www.google.com')

# Once opened, i need to wait for the page to load to find the input
search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
    EC.presence_of_element_located(
        (By.NAME, 'q')
    )
)

search_input.send_keys('Hello World!')
sleep(TIME_TO_WAIT)
