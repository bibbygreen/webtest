def find_and_print(messages, current_station):
    GreenLine=["Xindian", "Xindian City Hall", "Qizhang", "Dapinglin", "Jingmei", "Wanlong", "Gongguan",
            "Taipower Building", "Guting", "Chiang Kai-shek Memorial Hall", "Xiaonanmen", "Ximen", "Beimen",
            "Zhongshan", "Songjiang Nanjing", "Nanjing Fuxing", "Taipei Arena", "Nanjing Sanmin","Songshan"]

    # current_station = "Wanlong"
    current_station_index = GreenLine.index(current_station)
    Xiaobitan = "Xiaobitan"
    clean_messages = {}
    for key in messages:
        x = messages[key]
        x = x.strip(".")
        if Xiaobitan in x:
            clean_messages[key]=3.5  ###待優化
        for green_station in GreenLine:
            if green_station in x:
                clean_messages[key]=GreenLine.index(green_station)
    # print(clean_messages)

    for key in clean_messages:
        msg_station_index = clean_messages[key]
        # print(clean_messages[key])
        # print(msg_station_index)
        station_count = abs(current_station_index-msg_station_index)
        clean_messages[key]= station_count

    clean_messages_key=list(clean_messages.keys())
    clean_messages_value=list(clean_messages.values())

    closest = min(clean_messages_value)
    closest_friend = clean_messages_key[clean_messages_value.index(closest)]
    return print(closest_friend)

messages={ 
    "Leslie":"I'm at home near Xiaobitan station.",
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Vivian":"I'm at Xindian station waiting for you."
}


find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian