import random

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
# sleep(random.randint(2,10))

#1. Khai bao browsers
browsers = webdriver.Chrome(executable_path="../venv/chromedriver")

#2. Mo url cua post
browsers.get("https://www.facebook.com/topcomments.vn/posts/3711154159142692")
sleep(5.0)
#2a. Lay link hien comment
exit_step = browsers.find_element_by_id("expanding_cta_close_button")
exit_step.click()
sleep(3.0)

show_comments_link = browsers.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]//a")
show_comments_link.click()
sleep(3.0)

choices = browsers.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[1]/div/div/div/div/a")
choices.click()
sleep(3)

choices1 = browsers.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div/div/div/ul/li[3]/a")
choices1.click()
sleep(3)

showmore_comments_link = browsers.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[2]/div/a/div")
showmore_comments_link.click()
sleep(3.0)


#3. Tim tat ca cac the comment va ghi ra man hinh
comment_link = browsers.find_elements_by_xpath("//div[@aria-label='Bình luận']")
# comment_link = browsers.find_element_by_class_name("_6c7i")
#3a. Comment Loop
i = 0
for comment in comment_link:
    poster = comment.find_element_by_class_name("_6qw4")
    content = comment.find_element_by_class_name("_3l3x")
    i+=1
    print(str(i) + "-" + poster.text + ":" + content.text)

sleep(3.0)


#4. Dong trinh duyet
browsers.close()