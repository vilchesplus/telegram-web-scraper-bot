## https://www.codementor.io/@gergelykovcs/scrape-the-web-with-python-and-get-updates-on-telegram-rv83fbgie
## https://www.codementor.io/@gergelykovcs/how-and-why-i-built-a-simple-web-scrapig-script-to-notify-us-about-our-favourite-food-fcrhuhn45


#Import libraries for Python Website Monitoring project
import urllib.request
import smtplib,time, hashlib
import requests
import urllib
from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
TOKEN = config('TOKEN')

#Read the website and read time interval
input_website = 'https://analisiscalidadaire.madrid.es/situacionactual'

while True:
#Visit the website to know if it is up

    status = urllib.request.urlopen(input_website).getcode()
#If it returns 200, the website is up
    if status != 200:
#Call email function
        ResultText = "The website is down"
        print(ResultText)
        requests.get("https://api.telegram.org/bot" + TOKEN + "/sendMessage?chat_id=5002532208&text={}".format(ResultText))
    else:
        ResultText = "The website is up"
        options = Options()
        options.headless = True
        driver = webdriver.Remote("http://selenium:4444/wd/hub",options=options)
       # driver = webdriver.Chrome('C:/Users/rvilchef/OneDrive - NTT DATA EMEAL/chromedriver', options=options)
        driver.get("https://analisiscalidadaire.madrid.es/situacionactual")
        time.sleep(5)
        a = driver.find_element(by=By.XPATH, value=("//*[@id='tiempo_real_fecha']")).text
        time.sleep(5)

        print(ResultText)
        b = "Última carga de datos realizada: {}, \n {}".format(a, ResultText)
        requests.get("https://api.telegram.org/bot" + TOKEN + "/sendMessage?chat_id=5002532208&text={}".format(b))
        time.sleep(2000)



#ParsedRestultText = urllib.parse.quote_plus(ResultText)

#requests.get("https://api.telegram.org/bot" + TOKEN + "/sendMessage?chat_id=[5002532208]&text={}".format(ParsedResultText))
