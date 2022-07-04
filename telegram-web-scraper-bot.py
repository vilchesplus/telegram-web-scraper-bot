## https://www.codementor.io/@gergelykovcs/scrape-the-web-with-python-and-get-updates-on-telegram-rv83fbgie
## https://www.codementor.io/@gergelykovcs/how-and-why-i-built-a-simple-web-scrapig-script-to-notify-us-about-our-favourite-food-fcrhuhn45


#Import libraries for Python Website Monitoring project
import urllib.request
import smtplib,time, hashlib
import requests
import urllib

#Read the website and read time interval
input_website = 'https://analisiscalidadaire.madrid.es/situacionactual'

while True:
#Visit the website to know if it is up
#Visit the website to know if it is up
    status = urllib.request.urlopen(input_website).getcode()
#If it returns 200, the website is up
    if status != 200:
#Call email function
        ResultText = "The website is down"
        print(ResultText)
        requests.get("https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage?chat_id=5002532208&text={}".format(ResultText))
    else:
        ResultText = "The website is up"
 
        print(ResultText)
        requests.get("https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage?chat_id=5002532208&text={}".format(ResultText))
        time.sleep(2000)



#ParsedRestultText = urllib.parse.quote_plus(ResultText)

#requests.get("https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage?chat_id=[5002532208]&text={}".format(ParsedResultText))
