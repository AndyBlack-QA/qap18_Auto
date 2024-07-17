import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Написать 5 автотестов по примеры ниже, на выбранного вами сайта либо на https://candymapper.com/ (
# https://candymapperr2.com/ исправленный сайт)
#
# 1. Открыйть сайт http://thedemosite.co.uk/login.php
# 2. Ввести имя в поле username
# 3. Ввести пароль в поле password
# 4. Нажать на кнопку Test Login
# 5. Проверить, что Successful Login отображаются


URL = 'https://candymapper.com/'


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


def test_instant_window(driver):
    driver.get(URL)
    instant_pop_up_message = driver.find_element(By.CSS_SELECTOR, 'div[class="x-el x-el-div c1-1 c1-2 c1-2v c1-ge '
                                                                  'c1-gf c1-cy c1-6u c1-4v c1-b c1-c c1-d c1-e c1-f '
                                                                  'c1-g"]')
    assert instant_pop_up_message.is_displayed


def test_create_account(driver):
    driver.get(URL)
    close_instant_message_btn = driver.find_element(By.ID, "popup-widget238491-close-icon")
    close_instant_message_btn.click()
    profile_icon = driver.find_element(By.CSS_SELECTOR, "svg[class='x-el x-el-svg c2-g c2-h c2-16 c2-17 c2-1e"
                                                        " c2-1f c2-1a c2-t c2-s c2-u c2-r c2-1d c2-1b c2-m c2-3"
                                                        " c2-w c2-x c2-y c2-z c2-10 c2-11 c2-12 c2-13']")
    profile_icon.click()
    create_account_in_menu_button = driver.find_element(By.ID, "n-238369238407-membership-create-account")
    create_account_in_menu_button .click()
    first_name_field = driver.find_element(By.XPATH, "//input[@data-aid='CREATE_ACCOUNT_NAME_FIRST']")
    first_name_field.send_keys("Andrei")
    last_name_field = driver.find_element(By.XPATH, "//input[@data-aid='CREATE_ACCOUNT_NAME_LAST']")
    last_name_field.send_keys("Kuznets")
    email_field = driver.find_element(By.XPATH, "//input[@data-aid='CREATE_ACCOUNT_EMAIL']")
    email_field.send_keys("qwerty@gmail.com")
    phone_field = driver.find_element(By.XPATH, "//input[@data-aid='CREATE_ACCOUNT_PHONE']")
    phone_field.send_keys("80447079510")
    create_account_button = driver.find_element(By.XPATH, "//button[@data-ux='ButtonPrimary']")
    create_account_button.click()
    check_email_message = driver.find_element(By.ID, "CheckMailIcon")
    assert check_email_message.is_displayed()


def test_input_wrong_sign_in_data_message_displays(driver):
    driver.get(URL)
    close_instant_message_btn = driver.find_element(By.ID, "popup-widget238491-close-icon")
    close_instant_message_btn.click()
    profile_icon = driver.find_element(By.XPATH, "//a[@data-aid='MEMBERSHIP_ICON_DESKTOP_RENDERED']")
    profile_icon.click()
    my_account_in_menu_button = driver.find_element(By.CSS_SELECTOR, "[id='n-238369238407-membership-"
                                                                     "account-logged-out']")
    my_account_in_menu_button.click()
    email_field = driver.find_element(By.XPATH, "//input[@data-aid='MEMBERSHIP_SSO_LOGIN_EMAIL']")
    email_field.send_keys("asdiofasdifas@gmail.com")
    password_field = driver.find_element(By.XPATH, "//input[@data-aid='MEMBERSHIP_SSO_LOGIN_PASSWORD']")
    password_field.send_keys("pasidofgmasdfa")
    sign_in_button = driver.find_element(By.XPATH, "//button[@data-aid='MEMBERSHIP_SSO_SUBMIT']")
    sign_in_button.click()
    sign_in_error = driver.find_element(By.XPATH, "//p[@data-aid='MEMBERSHIP_SSO_ERR_REND']")
    assert sign_in_error.is_displayed()


def test_invalid_email_address_message(driver):
    driver.get(URL)
    close_instant_message_btn = driver.find_element(By.ID, "popup-widget238491-close-icon")
    close_instant_message_btn.click()
    profile_icon = driver.find_element(By.XPATH, "//a[@data-aid='MEMBERSHIP_ICON_DESKTOP_RENDERED']")
    profile_icon.click()
    my_account_in_menu_button = driver.find_element(By.CSS_SELECTOR, "[id='n-238369238407-membership-"
                                                                     "account-logged-out']")
    my_account_in_menu_button.click()
    email_field = driver.find_element(By.XPATH, "//input[@data-aid='MEMBERSHIP_SSO_LOGIN_EMAIL']")
    email_field.send_keys("asdiofasdifas")
    password_field = driver.find_element(By.XPATH, "//input[@data-aid='MEMBERSHIP_SSO_LOGIN_PASSWORD']")
    password_field.send_keys("pasidofgmasdfa")
    sign_in_button = driver.find_element(By.XPATH, "//button[@data-aid='MEMBERSHIP_SSO_SUBMIT']")
    sign_in_button.click()
    email_error = driver.find_element(By.XPATH, "//p[@data-aid='MEMBERSHIP_SSO_ERR_REND']")
    assert email_error.is_displayed()


def test_empty_password_field_error(driver):
    driver.get(URL)
    close_instant_message_btn = driver.find_element(By.ID, "popup-widget238491-close-icon")
    close_instant_message_btn.click()
    profile_icon = driver.find_element(By.XPATH, "//a[@data-aid='MEMBERSHIP_ICON_DESKTOP_RENDERED']")
    profile_icon.click()
    my_account_in_menu_button = driver.find_element(By.CSS_SELECTOR, "[id='n-238369238407-membership-"
                                                                     "account-logged-out']")
    my_account_in_menu_button.click()
    email_field = driver.find_element(By.XPATH, "//input[@data-aid='MEMBERSHIP_SSO_LOGIN_EMAIL']")
    email_field.send_keys("asdiofasdifas@gmail.com")
    sign_in_button = driver.find_element(By.XPATH, "//button[@data-aid='MEMBERSHIP_SSO_SUBMIT']")
    sign_in_button.click()
    empty_password_error_message = driver.find_elements(By.XPATH, "//p[@data-aid='MEMBERSHIP_SSO_ERR_REND']")
    assert empty_password_error_message


def test_ghostville_party_location(driver):
    driver.get(URL)
    close_instant_message_btn = driver.find_element(By.ID, "popup-widget238491-close-icon")
    close_instant_message_btn.click()
    halloween_party_button = driver.find_element(By.XPATH, "//a[text()='Halloween Party']")
    halloween_party_button.click()
    attending_party_button = driver.find_element(By.XPATH, "//a[@data-page='1e207470-841e-4b3b-be7e-aa1e8ed21486']")
    attending_party_button.click()
    ghostville_button = driver.find_element(By.XPATH, "//a[@data-page='18a76c56-d68b-4793-a2e5-2df8f996b7b0']")
    ghostville_button.click()
    party_location = driver.find_element(By.CSS_SELECTOR, "div[class='x-el x-el-div x-el c1-1 c1-2 c1-r c1-6w c1-4 "
                                                          "c1-ao c1-t c1-7o c1-ap c1-aq c1-b c1-c c1-ar c1-as c1-d "
                                                          "c1-e c1-f c1-g c1-1 c1-2 c1-b c1-c c1-d c1-e c1-f c1-g']")
    assert party_location.is_displayed()





















