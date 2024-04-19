import requests
import json
### 台北景點資料 ###
url_1="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
response=requests.get(url_1)
spot_json=json.loads(response.text)
spot_key_list=["stitle", "longitude", "latitude", "SERIAL_NO", "picURL"]
stitle_list=[]
longitude_list=[]
latitude_list=[]
SERIAL_NO_list=[]
picURL_list=[]
spot_dict={}
m=0
while(m<len(spot_json["data"]["results"])): #58
    stitle_list.append(spot_json["data"]["results"][m]["stitle"])
    longitude_list.append(spot_json["data"]["results"][m]["longitude"])
    latitude_list.append(spot_json["data"]["results"][m]["latitude"])
    SERIAL_NO_list.append(spot_json["data"]["results"][m]["SERIAL_NO"])
 
    url_string=spot_json["data"]["results"][m]["filelist"]
    first_url=""
    for char in url_string:
        first_url += char
        if first_url.endswith("jpg") or first_url.endswith("JPG"):
            break
    picURL_list.append(first_url)
    m+=1
spot_dict = {key: value for key, value in zip(spot_key_list, [stitle_list, longitude_list, latitude_list, SERIAL_NO_list, picURL_list])}
# print(spot_dict)

### 台北捷運站資料 ###
url_2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"
response=requests.get(url_2)
mrt_json=json.loads(response.text)

mrt_key_list=["mrt", "SERIAL_NO", "district"]
mrt_list=[]
SERIAL_NO_list=[]
district_list=[]
n=0
while(n<len(mrt_json["data"])):
    mrt_list.append(mrt_json["data"][n]["MRT"])
    SERIAL_NO_list.append(mrt_json["data"][n]["SERIAL_NO"])
    address = mrt_json["data"][n]["address"]
    district = ""
    for a in range(5, 8):
        district += address[a]
        a+=1
    district_list.append(district)
    n+=1

mrt_dict = {key: value for key, value in zip(mrt_key_list, [mrt_list, SERIAL_NO_list, district_list])}
# print(mrt_dict)

### 透過景點SERIAL_NO找行政區，並存成spot.csv ###
x=0
spot_dict["district"]=[]
while(x<len(spot_dict["SERIAL_NO"])):
    district_found = False
    for i, serial in enumerate(mrt_dict["SERIAL_NO"]):
        if spot_dict["SERIAL_NO"][x] == serial:
            spot_dict["district"].append(mrt_dict["district"][i])
            district_found = True
            break
    if not district_found:
        spot_dict["district"].append("Unknown")
    x+=1

k=0
with open("spot.csv", mode="w") as spot_file:
    while(k<len(spot_dict["stitle"])):
        spot_file.write(spot_dict["stitle"][k]+","+spot_dict["district"][k]+","+spot_dict["longitude"][k]+","+spot_dict["latitude"][k]+","+spot_dict["picURL"][k]+"\n")
        # print(spot_dict["stitle"][k]+","+spot_dict["district"][k]+","+spot_dict["longitude"][k]+","+spot_dict["latitude"][k]+","+spot_dict["picURL"][k])
        k+=1
# print(spot_dict["stitle"][k])
# print(spot_dict["district"][k])
# print(spot_dict["longitude"][k])
# print(spot_dict["latitude"][k])
# print(spot_dict["picURL"][k])
# print(spot_dict)

### 透過景點SERIAL_NO找對應的捷運站，並存成mrt.csv ###

mrt_spot_dict = {}

for j, spot_serial in enumerate(spot_dict["SERIAL_NO"]):
    for k, mrt_serial in enumerate(mrt_dict["SERIAL_NO"]):
        if spot_serial == mrt_serial:
            mrt_station = mrt_dict["mrt"][k]
            spot = spot_dict["stitle"][j]
            if mrt_station not in mrt_spot_dict:
                mrt_spot_dict[mrt_station] = [spot]
            else:
                mrt_spot_dict[mrt_station].append(spot)

with open("mrt.csv", mode="w") as mrt_file:
    for e in mrt_spot_dict:
        mrt_file.write(e + "," + ",".join(map(str, mrt_spot_dict[e]))+"\n")