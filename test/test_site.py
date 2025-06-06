import time
from selenium.webdriver.common.by import By






def test_open_s6(browser, value=None):
    browser.get('https://demoblaze.com/')
    galaxy_s6 = browser.find_element(By.XPATH, value = '//a[text()="Samsung galaxy s6"]')
    galaxy_s6.click()
    title = browser.find_element(By.CSS_SELECTOR, value='h2')
    assert title.text == 'Samsung galaxy s6'


def test_two_monitors(browser):
    browser.get('https://demoblaze.com/')
    monitor_link = browser.find_element(By.CSS_SELECTOR, value='''[onclick="byCat('monitor')"]''')
    monitor_link.click()
    time.sleep(2)
    monitors = browser.find_elements(By.CSS_SELECTOR, value='.card')
    assert len(monitors) == 2