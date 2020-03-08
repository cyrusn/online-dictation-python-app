FROM python:3

RUN mkdir /app
WORKDIR /app
RUN mkdir /app/public
RUN mkdir /app/data
COPY . /app

RUN pip install -r requirements.txt
EXPOSE 5050

ENTRYPOINT ["python","./main.py","--config","./config.ini"] 
CMD ["serve"]
