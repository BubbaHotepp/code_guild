import datetime
# class rain_data:

#     def __init__(self, location, date, daily_total):
#         self.location = location
#         self.date = date
#         self.daily_total = daily_total

#     def date():
#         date = datetime.datetime.strptime(y, '%d-%b-%Y')
#         print(date.year)   # 2016
#         print(date.month)  # 3
#         print(date.day)    # 25
#         print(date)  # 2016-03-25 00:00:00
#         print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016
def main():

    data_list = []
    rain_data = []

    data_file =''.join(open('columbia_ips.txt').readlines()[11:])
    raw_data = data_file.split('\n')
    del raw_data[-1]
    
    for i in raw_data:
        data_list.append(i[0:22])

    for i in data_list:
        x = i.split()
        y = tuple(x)
        rain_data.append(y)
        
    print(rain_data)
    
main()