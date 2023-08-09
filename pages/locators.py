from selenium.webdriver.common.by import By

class AuthLocators:
   MAIN_LOGO = (By.CSS_SELECTOR, "header#app-header > div > div > svg")
   MAIN_LOG = (By.CLASS_NAME, "rt-logo main-header__logo")
   SECTION_LEFT = (By.ID, "page-left")
   SECTION_RIGHT = (By.ID, "page-right")
   MENU = (By.XPATH, "//*[@id='page-right']/div[1]/div[1]")
   MEN = (By.CLASS_NAME, "card-container__wrapper")
   PHONE = (By.ID, "t-btn-tab-phone")
   MAIL = (By.ID, "t-btn-tab-mail")
   LOGIN = (By.ID, "t-btn-tab-login")
   LS = (By.ID, "t-btn-tab-ls")
   USERNAME = (By.ID, "username")
   PASSWORD = (By.ID, "password")
   ENTER = (By.ID, "kc-login")
   FORGOT = (By.ID, "forgot_password")
   REGISTER = (By.ID, "kc-register")
   RESET_BACK = (By.ID, 'reset-back')
   VK = (By.ID, "oidc_vk")
   OK = (By.ID, "oidc_ok")
   EMAIL = (By.ID, "oidc_mail")
   YA = (By.ID, "oidc_ya")
   COPYRIGHT = (By.CSS_SELECTOR, 'footer#app-footer > div > div')
   CONFANDSOGL = (By.CLASS_NAME, "rt-footer-left__item")
   HELP = (By.CSS_SELECTOR, 'footer#app-footer > div:nth-of-type(2)')
   CONFIDENTIAL = (By.CSS_SELECTOR, 'a#rt-footer-agreement-link > span')
   AGREEMENT = (By.CSS_SELECTOR, 'a#rt-footer-agreement-link > span:nth-of-type(2)')
   TABS = (By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div')
   ACTIVETAB = (By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active')
   ERROR_MESSAGE = (By.ID, 'form-error-message')
   CONF = (By.PARTIAL_LINK_TEXT, 'Политикой конфиденциальности')
   SOGL = (By.PARTIAL_LINK_TEXT, 'Пользовательским соглашением')
   PLACEHOLDER = (By.CLASS_NAME, 'rt-input__placeholder--active')
   H1 = (By.TAG_NAME, 'h1')
   H3 = (By.TAG_NAME, 'h3')
   BODY = (By.TAG_NAME, 'body')
   FORM = (By.CSS_SELECTOR, "div.card-container.login-form-container")
   INFO = (By.CLASS_NAME, "what-is-container")

