from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# derecionando para o gekodriver.
class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=r'D:\Ferramentas\Geko\chromedriver.exe')

# tela de login, seleção de tag e click no bootão enter.
 
    def login(self):
        driver = self.driver
        driver.get('http://www.instagram.com')
        time.sleep(3)
        #login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        #login_button.click()
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_elements = driver.find_element_by_xpath("//input[@name='password']")
        password_elements.clear()
        password_elements.send_keys(self.password)
        time.sleep(2)
        password_elements.send_keys(Keys.RETURN)
        time.sleep(3)
        self.curtir_fotos('clothes')

#função de acesso ao menu de tags do instagram 

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(3)
        for i in range(1, 3):
            driver.execute_script("window.scroll(0, 2000);")
            time.sleep(5)
        hrefs = driver.find_element_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' fotos: ' + str(len(pic_hrefs)))

#função de rolagem e click no botão curtir 

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scroll(0, 200);") #"window.scrollTo(0, documente.body.scrollHeigtht);"
            try:
                driver.find_element_by_class_name('//button[@class="wpO6b"]').click()
                time.sleep(5)
            except Exception as e:
                time.sleep(5)

# login e senha do instagram.
# login comando de login 
theodoroBot = InstagramBot('Login', 'senha')
theodoroBot.login()