FROM python:3.7
COPY ./#notifier.py# /app/app.py
RUN pip install --no-cache-dir urllib3
RUN pip install --no-cache-dir python-time
RUN pip install --no-cache-dir requests
RUN pip install --no-cache-dir bs4
WORKDIR /app
CMD [ "python", "./app.py" ]
