import requests
import datetime
import schedule
import time
import random

url = 'https://ptrp.com.br/home/create_ponto'
headers = {'cookie': '', 'x-csrf-token': ''}

def register_point1():
    random_minute_string = str(0) + str(random.randint(0, 9))
    while 1:
        now = datetime.datetime.now()
        if now.hour == 9 and str(now.minute) == random_minute_string:
            print(r)
            r = requests.post(url, headers = headers)
            print('ponto 1')
            break

def register_point2():
    random_minute_string = str(0) + str(random.randint(0, 9))
    while 1:
        now = datetime.datetime.now()
        if now.hour == 12 and str(now.minute) == random_minute_string:
            print(r)
            r = requests.post(url, headers = headers)
            print('ponto 2')
            break

def register_point3():
    random_minute_string = str(3) + str(random.randint(0, 9))
    while 1:
        now = datetime.datetime.now()
        print(now.minute)
        if now.hour == 13 and str(now.minute) == random_minute_string:
            print(r)
            r = requests.post(url, headers = headers)
            print('ponto 3')
            break

def register_point4():
    random_minute_string = str(3) + str(random.randint(0, 9))
    while 1:
        now = datetime.datetime.now()
        if now.hour == 18 and str(now.minute) == random_minute_string:
            r = requests.post(url, headers = headers)
            print(r)
            print('ponto 4')
            break

point1_houer = "09:00"
point2_houer = "12:00"
point3_houer = "13:30"
point4_houer = "18:30"

schedule.every().day.at(point1_houer).do(register_point1)
schedule.every().day.at(point2_houer).do(register_point2)
schedule.every().day.at(point3_houer).do(register_point3)
schedule.every().day.at(point4_houer).do(register_point4)

while 1:
    schedule.run_pending()
    time.sleep(1)
