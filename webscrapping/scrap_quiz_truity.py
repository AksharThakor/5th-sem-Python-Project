from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

#defining list to store questions

questions=[]

#link of our website
url="https://www.truity.com/test/career-personality-profiler-test"

#checking if html accessable
r=requests.get(url)

#if accesssable
if(r.status_code==200):
    
    print("you have access to this website's resources")
    
    #getting a browser driver for automation
    options = webdriver.ChromeOptions()
    
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(
    service= webdriver.ChromeService(), 
    options=options,
    )
    
    #opening link on automated browser window
    driver.get(url)
    
    time.sleep(15)
    
    #getting content of current website state
    content=driver.page_source
    soup=BeautifulSoup(content,"html.parser")
    element=None
    #looping through website pages till all the questions fetched
    while(element==None):
        
        #finding desired data by element id
        temp=soup.findAll("span",class_="label-text")
        
        #stripping it to get textdata removing html tags
        for i in temp:
            que=i.text
            print(que)
        
        #adding question to our list
        questions.append(que)
        
        #getting buttons by it's value and class to automate click and get next question 
        buttons=driver.find_elements(By.XPATH,'//input[@value="3" and @class="form-radio fancy-processed"]//ancestor::div')
        
        
        #click the button
        for button in buttons:
            button.click()
            time.sleep(2)
        
        nextpg_button=driver.find_element(By.XPATH,'//button[@value="Next step >" and @class="webform-next button-primary btn btn-default form-submit"]//parent::div')
        nextpg_button.click()

        
        #repeating process of getting next page data

        time.sleep(15)
        content=driver.page_source
        soup=BeautifulSoup(content,"html.parser")
        element = EC.presence_of_element_located((By.XPATH,'//button[@value="Score it!" and @class="webform-next button-primary btn btn-default form-submit"]//parent::div'))
        if(element!=None):
            break
        
   
    
    
else:
    print("You don't have access to this site's resources")
    