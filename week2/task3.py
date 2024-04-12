def func(*data):    
# data = ("郭宣雅", "林靜宜", "郭宣恆", "林靜花");  ## tuple 有序不可變動的列表
    middle_name_list = []
    for name in data:
        middle_index = int(len(name)/2)
        # print(name[middle_index])
        middle_name_list.append(name[middle_index])
    count_middle_dict = {item: middle_name_list.count(item) for item in set(middle_name_list)}
    # print(count_middle_dict)   ###{'明': 2, '大': 1}
    count_middle_dict_key = list(count_middle_dict.keys())
    count_middle_dict_value = list(count_middle_dict.values())

    # print(count_middle_dict_key)   ##['大', '明']
    # print(count_middle_dict_value)  ##[2, 1]
    unique_middle = []
    for n in count_middle_dict_value:
        if n == 1:
            unique_middle.append(count_middle_dict_key[count_middle_dict_value.index(n)])
    # print(unique_middle) ##['大']

    print_out = ""
    for name in data:
        middle_index = int(len(name)/2)
        name[middle_index]
        for m in unique_middle:
            if m == name[middle_index]:
                print_out = name
            # else:
            #     print("沒有")
    if print_out == "":
        return print("沒有")
    else:
        return print(print_out)

func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安