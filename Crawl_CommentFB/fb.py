from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


#1. Khai bao bien brower
brower = webdriver.Chrome(executable_path="../venv/chromedriver")

#2. Mo thu mot trang web
url = 'https://www.facebook.com'
brower.get(url)

#2a. Dien thong tin vao o user va password
txtUser = brower.find_element_by_id("email")
txtUser.send_keys("hahahaha")

txtPassword = brower.find_element_by_id("pass")
txtPassword.send_keys("123456")

#2b. Submit Form
txtPassword.send_keys(Keys.ENTER)




#3. Dung chuong trinh 5 giay
sleep(5.0)

#4. Dong trinh duyet
brower.close()

