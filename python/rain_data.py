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

    raw_data = []
    data_list = []

    data_file =''.join(open('columbia_ips.txt').readlines()[11:])
    raw_data = data_file.split('\n')
    del raw_data[-1]
    for i in raw_data:
        data_list.append(i[0:22])
    rain_data = tuple(data_list)
    print(rain_data)

main()