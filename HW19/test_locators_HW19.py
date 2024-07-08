import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium import webdriver


URL = 'https://www.bbc.com/news'


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


menu_item_css_pattern = "[data-testid='mainNavigationLink'][href='/{}']"
menu_item_xpath_pattern = "//a[@data-testid='mainNavigationLink' and @href='/{}']"


def test_bbc_css(driver_chrome):
    driver_chrome.get(URL)
    bbc_css = driver_chrome.find_element(By.CSS_SELECTOR, ".sc-49542412-2")
    assert bbc_css.is_displayed()


def test_bbc_xpath(driver_chrome):
    driver_chrome.get(URL)
    bbc_xpath = driver_chrome.find_element(By.XPATH, "//div[@class='sc-49542412-2 hrGuyi']")
    assert bbc_xpath.is_displayed()


def test_sign_in_css(driver_chrome):
    driver_chrome.get(URL)
    sign_in_css = driver_chrome.find_element(By.CSS_SELECTOR,
                                             "button[class='sc-238aa436-2 sc-238aa436-5 cUUVqo iPqQVG']")
    assert sign_in_css.is_displayed()


def test_sign_in_xpath(driver_chrome):
    driver_chrome.get(URL)
    sign_in_xpath = driver_chrome.find_element(By.XPATH, "//button[@class='sc-238aa436-2 sc-238aa436-5 cUUVqo iPqQVG']")
    assert sign_in_xpath.is_displayed()


def test_home_in_css(driver_chrome):
    driver_chrome.get(URL)
    home_css = driver_chrome.find_element(By.CSS_SELECTOR, menu_item_css_pattern.format(''))
    assert home_css.is_displayed()


def test_home_xpath(driver_chrome):
    driver_chrome.get(URL)
    home_xpath = driver_chrome.find_element(By.XPATH, menu_item_xpath_pattern.format(''))
    assert home_xpath.is_displayed()


def test_sport_in_css(driver_chrome):
    driver_chrome.get(URL)
    sport_css = driver_chrome.find_element(By.CSS_SELECTOR, menu_item_css_pattern.format('sport'))
    assert sport_css.is_displayed()


def test_sport_xpath(driver_chrome):
    driver_chrome.get(URL)
    sport_xpath = driver_chrome.find_element(By.XPATH, menu_item_xpath_pattern.format('sport'))
    assert sport_xpath.is_displayed()


# the video is instead of Reels, so I can't locate reel on the page
def test_video_in_css(driver_chrome):
    driver_chrome.get(URL)
    video_css = driver_chrome.find_element(By.CSS_SELECTOR, menu_item_css_pattern.format('video'))
    assert video_css.is_displayed()


def test_video_xpath(driver_chrome):
    driver_chrome.get(URL)
    video_xpath = driver_chrome.find_element(By.XPATH, menu_item_xpath_pattern.format('video'))
    assert video_xpath.is_displayed()


def test_travel_in_css(driver_chrome):
    driver_chrome.get(URL)
    travel_css = driver_chrome.find_element(By.CSS_SELECTOR, menu_item_css_pattern.format('travel'))
    assert travel_css.is_displayed()


def test_travel_xpath(driver_chrome):
    driver_chrome.get(URL)
    travel_xpath = driver_chrome.find_element(By.XPATH, menu_item_xpath_pattern.format('travel'))
    assert travel_xpath.is_displayed()

# the 7th element is absent on the page, so I skipped it ¯\_(ツ)_/¯

def test_article_title_css(driver_chrome):
    driver_chrome.get(URL)
    article_title_css = driver_chrome.find_elements(By.CSS_SELECTOR, "[data-testid='card-headline']")[1]
    assert article_title_css.is_displayed()


def test_article_title_xpath(driver_chrome):
    driver_chrome.get(URL)
    article_title_xpath = driver_chrome.find_element(By.XPATH, "(//*[@data-testid='card-headline'])[2]")
    assert article_title_xpath.is_displayed()


def test_article_photo_css(driver_chrome):
    driver_chrome.get(URL)
    article_photo_css = driver_chrome.find_element(By.CSS_SELECTOR, "[data-testid='card-media']")
    assert article_photo_css.is_displayed()


def test_article_photo_xpath(driver_chrome):
    driver_chrome.get(URL)
    article_photo_xpath = driver_chrome.find_element(By.XPATH, "//*[@data-testid='card-media']")
    assert article_photo_xpath.is_displayed()


def test_article_last_updated_css(driver_chrome):
    driver_chrome.get(URL)
    article_last_updated_css = driver_chrome.find_element(By.CSS_SELECTOR, "[data-testid='card-metadata-lastupdated']")
    assert article_last_updated_css.is_displayed()


def test_article_last_updated_xpath(driver_chrome):
    driver_chrome.get(URL)
    article_last_updated_xpath = driver_chrome.find_element(By.XPATH, "//*[@data-testid='card-metadata-lastupdated']")
    assert article_last_updated_xpath.is_displayed()


def test_features_and_analysis_css(driver_chrome):
    driver_chrome.get(URL)
    article_photo_css = driver_chrome.find_element(By.CSS_SELECTOR, "[data-analytics_group_name='Features & "
                                                                    "analysis'] [data-testid='virginia-title']")
    driver_chrome.execute_script("arguments[0].scrollIntoView({block: \"center\"});", article_photo_css)
    assert article_photo_css.is_displayed()


def test_features_and_analysis_xpath(driver_chrome):
    driver_chrome.get(URL)
    article_photo_xpath = driver_chrome.find_element(By.XPATH, "//*[@data-testid='virginia-title' and text()="
                                                               "'Features & analysis']")
    driver_chrome.execute_script("arguments[0].scrollIntoView({block: \"center\"});", article_photo_xpath)
    assert article_photo_xpath.is_displayed()
