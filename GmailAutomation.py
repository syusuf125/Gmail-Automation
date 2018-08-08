#Script to find out the total money spent on Uber rides
#Author name : Syed Yusuf W
#Date : 02/Aug/2018

import requests
import webbrowser
import bs4
import os
from selenium import webdriver
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.keys import Keys


chromedriver = "/Users/webyog/Downloads/chromedriver"
browser = webdriver.Chrome(chromedriver)
browser.get('https://www.gmail.com')


def loginMail(email,password):

    uname = browser.find_element_by_name("identifier")
    uname.send_keys(email)
    nextButton = browser.find_element_by_xpath('//*[@id="identifierNext"]/content/span')
    nextButton.click()
    time.sleep(1)
    pwd = browser.find_element_by_name("password")
    pwd.send_keys(password)
    nextButton1 = browser.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
    nextButton1.click()
    time.sleep(4)


def sendMail(n,recipient,cv): #n:number of mails, recipient : to whom the mail is to be sent, cv is whether conversation view should be on or off

    compose = browser.find_element_by_xpath('//div[@class ="T-I J-J5-Ji T-I-KE L3"]')

    for i in range(int(n)):
        if ((cv == "t") or (cv == "T")):
            compose.click()
            time.sleep(1)
            sendTo = browser.find_element_by_name('to')
            sendTo.send_keys(recipient)
            subject = browser.find_element_by_name('subjectbox')
            subject.send_keys("test")
            time.sleep(2)
            msgbody = browser.find_element_by_xpath("//div[@aria-label='Message Body']")
            msgbody.send_keys("hi hellooo how are you" + Keys.COMMAND + Keys.ENTER)
            time.sleep(2)
        if ((cv == 'n') or (cv == "N")):
            compose.click()
            time.sleep(1)
            sendTo = browser.find_element_by_name('to')
            sendTo.send_keys(recipient)
            subject = browser.find_element_by_name('subjectbox')
            subject.send_keys("test" + str(uuid.uuid1()))
            time.sleep(2)
            msgbody = browser.find_element_by_xpath("//div[@aria-label='Message Body']")
            msgbody.send_keys("hi hellooo how are you" + Keys.COMMAND + Keys.ENTER)
            time.sleep(2)

def logoutFunc():
    avatar = browser.find_element_by_xpath('//*[@class="gb_9a gbii"]')
    avatar.click()
    signout = browser.find_element_by_xpath('//*[@class="gb_za gb_3f gb_9f gb_Oe gb_Fb"]')
    signout.click()
    #//*[@id="gb"]/div[2]/div[3]/div/div[2]/div/a/span
    # compose.find
    # time.sleep(3)
    # sendbutton = browser.find_element_by_css_selector('#\3a o8')
    # sendbutton.click()
    # //*[@id=":o3"]

loginMail("email","password")
sendMail(2,"to address","n")
logoutFunc()

# <div class="T-I J-J5-Ji T-I-KE L3" role="button" tabindex="0" gh="cm" style="user-select: none;">COMPOSE</div>




