import requests
import json
import datetime
from datetime import timezone,timedelta
import time
##
import Lib
##

#################################################################################

##
#timeFrom=2022-03-20T00%3A00%3A00
#timeTo=2022-03-20T23%3A59%3A59
#
##

timeZone=["0點-3點",
          "3點-6點",
          "6點-9點",
          "9點-12點",
          "12點-15點",
          "15點-18點",
          "18點-21點",
          "21點-0點"]

def get_data():
    _time = datetime.datetime.now().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
    #print(_time)
    ## 換日
    if _time.hour>21 and _time.hour < 24:
        dateToday = _time + timedelta(days=1)
    else:
        dateToday = _time
    #print(dateToday)
    ######
    ##########
    timeFrom = dateToday.strftime("%Y-%m-%d") + "T00:00:00"
    timeTo = dateToday.strftime("%Y-%m-%d") + "T23:59:59"



    ##
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-065"
    params = {
        "Authorization": "CWB-8AA28B89-03AC-455F-9EAC-6D0394AA9AD9",
        "locationName": "三民區",
        "timeFrom": timeFrom,
        "timeTo": timeTo
    }

    ###
    ctx = ""

    ##
    response = requests.get(url, params=params)
    ##print(response.status_code)

    if response.status_code == 200:
        # print(response.text)
        data = json.loads(response.text)
        #print(data["records"])
        _location = data["records"]["locations"][0]["locationsName"]  #市
        _location += data["records"]["locations"][0]["location"][0]["locationName"] #區

        ##
        ctx += "=========\r\n"
        ctx += _location +"\r\n"
        ctx += "=========\r\n"
        ##
        #print("=========")
        #print(_location)
        #print("=========")
        ##  weather_elements
        #0 12小時降雨機率
        #1 天氣現象
        #2 體感溫度
        #3 溫度
        #4 相對濕度
        #5 舒適度指數
        #6 天氣預報綜合描述
        #7 6小時降雨機率
        #8 風速
        #9 風向
        #10 露點溫度
        ##

        weather_elements = data["records"]["locations"][0]["location"][0]["weatherElement"]
        j = len(weather_elements[6]["time"])
        #print(j)
        for i in range(0, len(weather_elements[6]["time"])):
            elememt = "。".join(weather_elements[6]["time"][i]["elementValue"][0]["value"].split("。")[1:3])
            #ctx += weather_elements[6]["time"][i]["elementValue"][0]["value"] + "\r\n"
            ctx += timeZone[8-j] + "\r\n" + elememt + "\r\n"
            j -= 1

        return ctx
    else:
        return 0
        #print("Can't get data!")
#########
if __name__ == '__main__':
    Lib.push(get_data())
