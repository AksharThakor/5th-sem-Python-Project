from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
import time




#defining list to store questions

questions=[]




#link of our website
url="https://openpsychometrics.org/tests/RIASEC/1.php"

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
   
    time.sleep(5)
   
    #getting content of current website state
    content=driver.page_source
    soup=BeautifulSoup(content,"html.parser")
    
   
    
    #looping through website pages till all the questions fetched
    while(soup.find("div",id="itext")!=None):
        
        #finding desired data by element id
        temp=soup.find(id="itext")
        
        #stripping it to get textdata removing html tags
        que=temp.text
        print(que)
        
        #adding question to our list
        questions.append(que)
        
        #getting button by it's id to automate click and get next question 
        button=driver.find_element(By.ID,"A3")
        
        #click the button
        button.click()
        
        #repeating process of getting next page data

        time.sleep(5)
        content=driver.page_source
        soup=BeautifulSoup(content,"html.parser")
       
        
    
#if not accessable
else:
    print("you don't have access to this website's resources")
    
    
print(questions)
with open("OSYCHO_QUE.csv","a") as csv:
    
    for i in range(len(questions)):
        csv.write(questions[i]+"\n")