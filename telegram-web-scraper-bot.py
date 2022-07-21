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

#Function to send email
def send_email(email_string):
   #Fill credentials for sender's email and receiver's email
   email_from = 'vilchesplus@gmail.com'
   password = 'kgfpirtuazuqtopj'
   email_to = 'vilchesplus@gmail.com', 'rvilchef@nttdata.com', 'veronica.hernandez.negrin@nttdata.com', 'rafael.vilchesfernandez@nttdata.com'
   #Enter subject line
   subject = "Status of website WBANA CALAIR"
 
   #Connect to gmail's smtp server
   smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
 
   #Login to the gmail server 
   smtp_server.login(email_from, password)
 
   #Content of email
   message = f"Subject: {subject}\n\n{email_string}"
 
   #Send email through the smtp server
   smtp_server.sendmail(email_from, email_to, message.encode('utf8'))
 
   #Close the server connection
   smtp_server.close()



#Read the website and read time interval
input_website = 'https://analisiscalidadaire.madrid.es/situacionactual'

while True:
#Visit the website to know if it is up

    status = urllib.request.urlopen(input_website).getcode()
#If it returns 200, the website is up
    if status != 200:
#Call email function
        estado = "The website is down"
        requests.get("https://api.telegram.org/bot" + TOKEN + "/sendMessage?chat_id=5002532208&text={}".format(estado))
        send_email("The website is down")
    else:
        ResultText = "The website is up"
        options = Options()
        options.headless = True
        driver = webdriver.Remote("http://selenium:4444/wd/hub",options=options)
        #driver = webdriver.Chrome('C:/Users/rvilchef/OneDrive - NTT DATA EMEAL/chromedriver', options=options)
        driver.get("https://analisiscalidadaire.madrid.es/situacionactual")
        time.sleep(5)
        a = driver.find_element(by=By.XPATH, value=("//*[@id='tiempo_real_fecha']")).text
        time.sleep(5)

        print(ResultText)
        b = "Última carga de datos realizada: {}, \n {}".format(a, ResultText)
        send_email(b)
        requests.get("https://api.telegram.org/bot" + TOKEN + "/sendMessage?chat_id=5002532208&text={}".format(b))
        time.sleep(2000)



#ParsedRestultText = urllib.parse.quote_plus(ResultText)

#requests.get("https://api.telegram.org/bot" + TOKEN + "/sendMessage?chat_id=[5002532208]&text={}".format(ParsedResultText))
