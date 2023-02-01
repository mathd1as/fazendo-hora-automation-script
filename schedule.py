import requests
import datetime
import schedule
import time
import random

url = 'https://ptrp.com.br/home/create_ponto'
headers = {'cookie': 'intercom-id-98c1119f8a25c0b886bf6f022cbf8cfbdc15f49f=323ce685-ca26-4fa3-86e3-f9ac189549fe; intercom-device-id-98c1119f8a25c0b886bf6f022cbf8cfbdc15f49f=e68d63ae-04bb-4fda-882c-8100a90e0fba; cookie_eu_consented=true; intercom-session-98c1119f8a25c0b886bf6f022cbf8cfbdc15f49f=; remember_user_token=BAhbCFsGaQK1YUkiIiQyYSQxMCRMWU01RzZZS0FobUxHcWJTT0JLVDhPBjoGRVRJIhcxNjc1MTgzMzMzLjIxMjcyNTkGOwBG--8c98adb0c604e3a58bf73ffecd01663e55806743; _ptrp_session=NTRhV0dRMCtKSy9Cd0lheEluRElYVWZjaXJXcHFnWlYrSWZmQ1pGUldxeGVYbnN6S2s0dmhWSzZzbEdjQU5xcjM2RGZsZ1gwaXVXVG0zKzJPVEJ5c1lYbVdlZXBkUVYrM2dGNFNqbUxkZjc5enZiZ3FyL1dnVGN5SVJMbzZxM0o1NFo2N0k2UWRTbDZaWDFJUTlDNzZ3ZCtJdWd4YS9PeHdEdklsMTBVeXo5cFVVOGhmWEhjZGZZM1ZNalBlV0lSNkN2ekJuc3Qyc1UrRDFCREpSMmErNWYxNnhtaEd1NTZqd1dhNXN0c3YwZEVYUHVQVXltbGhtblFFdHlLWDIyZ2RVUnNveEc0Q2pobVNsSG1qK0ZBWndac1V6eUxSdHd4ZzVtMzl4NGl0aHM4RmQ3Sk9NbCt6ZVNQbFpLaGlFS2doTEYrTWVjc1ZMbURiNzcxNDJxT1c5TDNtZmFJVTE4dFpUbDdZaVpiM3VJPS0tVUlqakZmOUtpS0FoWlRzOHBaYWJ1Zz09--9deacbd1095d406b58dc6692927f27af4a4d84c5; PTRP-LB="MTAuMTM2LjE1LjEwNzo4MA=="', 'x-csrf-token': 'fqF69/zHm3ER7vG3PkIcG1GkgFYP3tJ6ANGZ6Gwn4FJZiegum2vcWhu+d5i8LmNvIMf88v+vqDS2S0qWpoDezA=='}

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
