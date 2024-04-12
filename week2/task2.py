def book(consultants, hour, duration, criteria):

    query_time = range(hour, hour + duration)

    # Sort consultants based on the specified criteria
    if criteria == "price":
        sorted_consultants = sorted(consultants, key=lambda x: x["price"])
        # Check each consultant's availability and book the first available one
        for consultant in sorted_consultants:
            temp_name = consultant["name"]
            temp_time = consultants_time[temp_name]
            if not any(time in temp_time for time in query_time):
                temp_time.extend(query_time)
                print(temp_name)
                break
        else:
            print("No service")

    elif criteria == "rate":
        sorted_consultants = sorted(consultants, key=lambda x: x["rate"], reverse=True)
        for consultant in sorted_consultants:
            temp_name = consultant["name"]
            temp_time = consultants_time[temp_name]
            if not any(time in temp_time for time in query_time):
                temp_time.extend(query_time)
                print(temp_name)
                break
        else:
            print("No service")
    else:
        print("Invalid criteria")
        exit()

consultants = [
    {"name": "John", "rate": 4.5, "price": 1000},
    {"name": "Bob", "rate": 3, "price": 1200},
    {"name": "Jenny", "rate": 3.8, "price": 800}
]
# Initialize consultants_time dictionary
consultants_time = {consultant['name']: [] for consultant in consultants}
# for consultant in consultants:
#     consultants_time = {consultant['name']: []}

# print(consultants_time)


book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John
# count_middle_dict = {'明': 2, '大': 1}

# # Using list comprehension to directly extract keys where value is 1
# unique_middle = [key for key, value in count_middle_dict.items() if value == 1]

# print(unique_middle)  # Output: ['大']

# query_time = [7] 
# time = [9, 10 ,11]
# time.extend([12, 13])

# if query_time not in time:
#     time.extend(query_time)
# print(sorted(time))


# time2 = [9, 10 ,11]
# time2.append([12, 13])

# print(time2)