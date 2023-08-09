import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome(r'C:/some_folder`/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.maximize_window()
   pytest.driver.get('https://b2c.passport.rt.ru')
   time.sleep(10)
   yield

   pytest.driver.quit()

def test_main_logo():
   # Проверяем наличие логотипа на странице авторизации
   logo = pytest.driver.find_element(By.CSS_SELECTOR, 'header#app-header > div > div > svg').is_displayed()
   assert logo == True

def test_section():
   # Проверяем наличие в левой секции формы авторизации, а в правой вспомогательная информация
   left_section = pytest.driver.find_element(By.ID, "page-left").find_element(By.CSS_SELECTOR, "div.card-container.login-form-container").is_displayed()
   right_section = pytest.driver.find_element(By.ID, "page-right").find_element(By.CSS_SELECTOR, "div.what-is-container").is_displayed()
   assert left_section == True
   assert right_section == True

def test_button_registration():
   # Проверяем кнопку зарегистрироваться
   btn_registration = pytest.driver.find_element(By.ID, 'kc-register').click()
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"

def test_button_forgot_password():
   # Проверяем кнопку забыл пароль
   btn_forgot_password = pytest.driver.find_element(By.ID, 'forgot_password').click()
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "Восстановление пароля"

def test_confidential():
   # Проверяем ссылку на политику конфиденциальности
   confidential = pytest.driver.find_element(By.CSS_SELECTOR, 'a#rt-footer-agreement-link > span').click()
   pytest.driver.switch_to.window(pytest.driver.window_handles[1])
   page = pytest.driver.current_url
   assert "политика" in pytest.driver.find_element(By.TAG_NAME, 'body').text

def test_agreement():
   # Проверяем ссылку на пользовательское соглашение
   agreement = pytest.driver.find_element(By.CSS_SELECTOR, 'a#rt-footer-agreement-link > span:nth-of-type(2)').click()
   pytest.driver.switch_to.window(pytest.driver.window_handles[1])
   page = pytest.driver.current_url
   assert page == "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"

def test_footer():
   # Проверяем наличие в футере наличие копирайта, ссылок на политику конфиденциальности и пользовательское соглашение, телефона поддержки
   copyright = pytest.driver.find_element(By.CSS_SELECTOR, 'footer#app-footer > div > div')
   conf = pytest.driver.find_element(By.PARTIAL_LINK_TEXT, 'Политикой конфиденциальности').is_displayed()
   sogl = pytest.driver.find_element(By.PARTIAL_LINK_TEXT, 'Пользовательским соглашением').is_displayed()
   help = pytest.driver.find_element(By.CSS_SELECTOR, 'footer#app-footer > div:nth-of-type(2)')
   assert copyright.text == "© 2023 ПАО «Ростелеком». 18+"
   assert conf == True
   assert sogl == True
   assert "8 800 100 0 800" in help.text

def test_tabs():
   # Проверяем название вкладок
   tabs = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div')
   assert "Номер" in tabs.text
   assert "Почта" in tabs.text
   assert "Логин" in tabs.text
   assert "Лицевой счёт" in tabs.text

def test_start_tab():
   # Проверяем активный таб по умолчанию
   tab = pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active')
   assert "Телефон" in tab.text

def test_smena_phone_to_mail():
   # Проверяем смену таба с телефона на почту
   phone = pytest.driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()
   pytest.driver.find_element(By.ID, 'username').send_keys('alex@mail.ru')
   pytest.driver.find_element(By.ID, 'password').click()
   tab = pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active')
   assert "Почта" in tab.text

def test_smena_login_to_mail():
   # Проверяем смену таба с логина на почту
   login = pytest.driver.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]').click()
   pytest.driver.find_element(By.ID, 'username').send_keys('alex@mail.ru')
   pytest.driver.find_element(By.ID, 'password').click()
   tab = pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active')
   assert "Почта" in tab.text

def test_smena_ls_to_mail():
   # Проверяем смену таба с лицевого счета на почту
   ls = pytest.driver.find_element(By.XPATH, '//*[@id="t-btn-tab-ls"]').click()
   pytest.driver.find_element(By.ID, 'username').send_keys('alex@mail.ru')
   pytest.driver.find_element(By.ID, 'password').click()
   tab = pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active')
   assert "Почта" in tab.text

def test_smena_mail_to_phone():
   # Проверяем смену таба с почты на телефон
   mail = pytest.driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
   pytest.driver.find_element(By.ID, 'username').send_keys('89210002222')
   pytest.driver.find_element(By.ID, 'password').click()
   tab = pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active')
   assert "Телефон" in tab.text

def test_smena_login_to_phone():
   # Проверяем смену таба с логина на телефон
   login = pytest.driver.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]').click()
   pytest.driver.find_element(By.ID, 'username').send_keys('89210002222')
   pytest.driver.find_element(By.ID, 'password').click()
   tab = pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active')
   assert "Телефон" in tab.text

def test_smena_ls_to_phone():
   # Проверяем смену таба с лицевого счета на телефон
   ls = pytest.driver.find_element(By.XPATH, '//*[@id="t-btn-tab-ls"]').click()
   pytest.driver.find_element(By.ID, 'username').send_keys('89210002222')
   pytest.driver.find_element(By.ID, 'password').click()
   tab = pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active')
   assert "Телефон" in tab.text

def test_smena_phone_to_ls():
   # Проверяем смену таба с телефона на лицевой счет
   phone = pytest.driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()
   pytest.driver.find_element(By.ID, 'username').send_keys('123456789009')
   pytest.driver.find_element(By.ID, 'password').click()
   tab = pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active')
   assert "Лицевой счёт" in tab.text

def test_smena_mail_to_ls():
   # Проверяем смену таба с почты на лицевой счет
   phone = pytest.driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
   pytest.driver.find_element(By.ID, 'username').send_keys('123456789009')
   pytest.driver.find_element(By.ID, 'password').click()
   tab = pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active')
   assert "Лицевой счёт" in tab.text

def test_smena_login_to_ls():
   # Проверяем смену таба с логина на лицевой счет
   login = pytest.driver.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]').click()
   pytest.driver.find_element(By.ID, 'username').send_keys('123456789009')
   pytest.driver.find_element(By.ID, 'password').click()
   tab = pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active')
   assert "Лицевой счёт" in tab.text

def test_smena_phone_to_login():
   # Проверяем смену таба с телефона на логин
   phone = pytest.driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()
   pytest.driver.find_element(By.ID, 'username').send_keys('Alex')
   pytest.driver.find_element(By.ID, 'password').click()
   tab = pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active')
   assert "Логин" in tab.text

def test_smena_mail_to_login():
   # Проверяем смену таба с почты на логин
   mail = pytest.driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
   pytest.driver.find_element(By.ID, 'username').send_keys('Alex')
   pytest.driver.find_element(By.ID, 'password').click()
   tab = pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active')
   assert "Логин" in tab.text

def test_smena_ls_to_login():
   # Проверяем смену таба с лицевого счета на логин
   ls = pytest.driver.find_element(By.XPATH, '//*[@id="t-btn-tab-ls"]').click()
   pytest.driver.find_element(By.ID, 'username').send_keys('Alex')
   pytest.driver.find_element(By.ID, 'password').click()
   tab = pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active')
   assert "Логин" in tab.text

def test_autorization_vk():
   # Проверяем авторизацию через vk
   pytest.driver.find_element(By.ID, 'oidc_vk').click()
   page = pytest.driver.current_url
   assert "https://id.vk.com/" in page

def test_autorization_ok():
   # Проверяем авторизацию через ok
   pytest.driver.find_element(By.ID, 'oidc_ok').click()
   page = pytest.driver.current_url
   assert "https://connect.ok.ru/" in page

def test_autorization_mail():
   # Проверяем авторизацию через mail
   pytest.driver.find_element(By.ID, 'oidc_mail').click()
   page = pytest.driver.current_url
   assert "https://connect.mail.ru/" in page

def test_autorization_ya():
   # Проверяем авторизацию через ya
   pytest.driver.find_element(By.ID, 'oidc_ya').click()
   time.sleep(10)
   page = pytest.driver.current_url
   assert "https://oauth.yandex.ru/" in page

def test_enter():
   # Проверяем ввод корректной почты и пароля
   mail = pytest.driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
   pytest.driver.find_element(By.ID, 'username').send_keys('v.lexa.v@mail.ru')
   pytest.driver.find_element(By.ID, 'password').send_keys('Alex161288')
   pytest.driver.find_element(By.ID, 'kc-login').click()
   assert pytest.driver.find_element(By.TAG_NAME, 'h3').text == "Учетные данные"

def test_not_valid_password():
   # Проверяем ввод некорректного пароля
   mail = pytest.driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
   pytest.driver.find_element(By.ID, 'username').send_keys('v.lexa.v@mail.ru')
   pytest.driver.find_element(By.ID, 'password').send_keys('Alex')
   pytest.driver.find_element(By.ID, 'kc-login').click()
   assert pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

def test_not_valid_mail():
   # Проверяем ввод некорректной почты
   mail = pytest.driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
   pytest.driver.find_element(By.ID, 'username').send_keys('lexa@mail.ru')
   pytest.driver.find_element(By.ID, 'password').send_keys('Alex161288')
   pytest.driver.find_element(By.ID, 'kc-login').click()
   assert pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

def test_not_valid_mail_and_password():
   # Проверяем ввод некорректной почты и пароля
   mail = pytest.driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
   pytest.driver.find_element(By.ID, 'username').send_keys('lexa@mail.ru')
   pytest.driver.find_element(By.ID, 'password').send_keys('Alex')
   pytest.driver.find_element(By.ID, 'kc-login').click()
   assert pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

def test_password_phone():
   # Проверяем восстановление пароля по номеру телефона
   btn_forgot_password = pytest.driver.find_element(By.ID, 'forgot_password').click()
   phonetab = pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
   phone = pytest.driver.find_element(By.ID, 'username').click()
   assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder--active').text == "Мобильный телефон"

def test_password_mail():
   # Проверяем восстановление пароля по электронной почте
   btn_forgot_password = pytest.driver.find_element(By.ID, 'forgot_password').click()
   phonetab = pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
   phone = pytest.driver.find_element(By.ID, 'username').click()
   assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder--active').text == "Электронная почта"

def test_button_back_forgot_password():
   # Проверяем кнопку назад с страницы восстановления пароля
   btn_forgot_password = pytest.driver.find_element(By.ID, 'forgot_password').click()
   btn_forgot_back = pytest.driver.find_element(By.ID, 'reset-back').click()
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "Авторизация"
