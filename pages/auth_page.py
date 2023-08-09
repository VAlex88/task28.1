from .base_page import BasePage
from .locators import AuthLocators

import time,os


class AuthPage(BasePage):

   def __init__(self, driver, timeout=10):
       super().__init__(driver, timeout)
       url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru"
       driver.get(url)
       #создаем нужные элементы
       self.main_logo = driver.find_element(*AuthLocators.MAIN_LOGO)
       self.section_left = driver.find_element(*AuthLocators.SECTION_LEFT)
       self.section_right = driver.find_element(*AuthLocators.SECTION_RIGHT)
       self.menu = driver.find_element(*AuthLocators.MENU)
       self.phone = driver.find_element(*AuthLocators.PHONE)
       self.mail = driver.find_element(*AuthLocators.MAIL)
       self.login = driver.find_element(*AuthLocators.LOGIN)
       self.ls = driver.find_element(*AuthLocators.LS)
       self.username = driver.find_element(*AuthLocators.USERNAME)
       self.password = driver.find_element(*AuthLocators.PASSWORD)
       self.enter = driver.find_element(*AuthLocators.ENTER)
       self.forgot = driver.find_element(*AuthLocators.FORGOT)
       self.register = driver.find_element(*AuthLocators.REGISTER)
       #self.reset_back = driver.find_element(*AuthLocators.RESET_BACK)
       self.vk = driver.find_element(*AuthLocators.VK)
       self.ok = driver.find_element(*AuthLocators.OK)
       self.email = driver.find_element(*AuthLocators.EMAIL)
       self.ya = driver.find_element(*AuthLocators.YA)
       self.copyright = driver.find_element(*AuthLocators.COPYRIGHT)
       self.confandsogl = driver.find_element(*AuthLocators.CONFANDSOGL)
       self.help = driver.find_element(*AuthLocators.HELP)
       self.confidential = driver.find_element(*AuthLocators.CONFIDENTIAL)
       self.agreement = driver.find_element(*AuthLocators.AGREEMENT)
       self.tabs = driver.find_element(*AuthLocators.TABS)
       self.activetabs = driver.find_element(*AuthLocators.ACTIVETAB)
       #self.error_massage = driver.find_element(*AuthLocators.ERROR_MESSAGE)
       self.sogl = driver.find_element(*AuthLocators.SOGL)
       self.conf = driver.find_element(*AuthLocators.CONF)
       #self.placeholder = driver.find_element(*AuthLocators.PLACEHOLDER)
       self.h1 = driver.find_element(*AuthLocators.H1)
       #self.h3 = driver.find_element(*AuthLocators.H3)
       self.form = driver.find_element(*AuthLocators.FORM)
       self.info = driver.find_element(*AuthLocators.INFO)
       #self.mb = driver.find_element(*AuthLocators.SECTION_LEFT).find_element(*AuthLocators.FORM)
       #self.body = driver.find_element(*AuthLocators.BODY)
       time.sleep(3)

   def login_form_in_section(self):
       self.mb.is_displayed()

   def texth1(self):
       self.h1.get_element_text()

   def enter_username(self, value):
       self.username.send_keys(value)

   def enter_password(self, value):
       self.password.send_keys(value)

   def btn_username(self):
       self.username.click()
       time.sleep(3) #ждем реакции

   def btn_password(self):
       self.password.click()
       time.sleep(3) #ждем реакции

   def btn_enter(self):
       self.enter.click()
       time.sleep(3) #ждем реакции

   def btn_register(self):
       self.register.click()
       time.sleep(3) #ждем реакции

   def btn_forgot(self):
       self.forgot.click()
       time.sleep(3) #ждем реакции

   def btn_back(self):
       self.reset_back.click()
       time.sleep(3) #ждем реакции

   def btn_phonetab(self):
       self.phone.click()
       time.sleep(3) #ждем реакции

   def btn_mailtab(self):
       self.mail.click()
       time.sleep(3) #ждем реакции

   def btn_logintab(self):
       self.login.click()
       time.sleep(3) #ждем реакции

   def btn_lstab(self):
       self.ls.click()
       time.sleep(3) #ждем реакции

   def btn_vk(self):
       self.vk.click()
       time.sleep(3) #ждем реакции

   def btn_ok(self):
       self.ok.click()
       time.sleep(3) #ждем реакции

   def btn_email(self):
       self.email.click()
       time.sleep(3) #ждем реакции

   def btn_ya(self):
       self.ya.click()
       time.sleep(3) #ждем реакции