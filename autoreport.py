import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from .log import Logger

class AutoHealthReport:
    def __init__(self, username, password, url, headless=True, logger=Logger()):
        self.username = username
        self.password = password
        self.url = url
        self.logger = logger
        option = webdriver.ChromeOptions()
        if headless:
            option.add_argument('headless')
        self.driver = webdriver.Chrome(options=option)

    def run(self):
        self.driver.get(url=self.url)
        self.login()
        self.fill_form()
        self.driver.close()

    def login(self):
        html = self.driver.page_source
        if html.find('统一身份认证平台') != -1:
            try:
                self.driver.find_element(By.ID, 'username').send_keys(self.username)
                self.driver.find_element(By.ID, 'password').send_keys(self.password)
                self.driver.find_element(By.ID, 'dl').click()
            except Exception as e:
                self.logger.writeln(e)
                exit(1)
    
    def fill_form(self):
        html = self.driver.page_source
        if html.find('统一身份认证平台') != -1:
            self.logger.writeln('登录失败')
            exit(1)
        js = '''
            console.log('请遵循疫情防控规定');
        '''
        self.driver.execute_script(js)
        self.driver.find_element(By.XPATH, '//div[@class="footers"]/a').click()
        try:
            self.driver.find_element(By.CSS_SELECTOR, "[class='wapcf-btn wapcf-btn-ok']").click()
            self.logger.writeln('{} {} 提交成功'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), self.username))
        except Exception as e:
            self.logger.writeln('{} {} 今日已提交过信息'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), self.username))