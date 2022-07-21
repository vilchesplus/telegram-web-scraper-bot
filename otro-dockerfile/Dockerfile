FROM python:3.7
COPY ./telegram-web-scraper-bot.py /app/app.py
COPY ./.env /app/.env
RUN pip install --no-cache-dir selenium
RUN pip install --no-cache-dir urllib3
RUN pip install --no-cache-dir python-time
RUN pip install --no-cache-dir requests
RUN pip install --no-cache-dir python-decouple
RUN pip install --no-cache-dir bs4
WORKDIR /app
CMD [ "python", "./app.py" ]
