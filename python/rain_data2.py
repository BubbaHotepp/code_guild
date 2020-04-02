def rain_mean(list_input):
    sub_total = 0
    total_days = (len(list_input))
    for item in range(total_days):
        indice = x[item]
        daily = indice[1]
        print(daily)
        sub_total += int(daily)
    total = sub_total / total_days
    return total

def main():

    data_list = []
    rain_data = []

    data_file =''.join(open('columbia_ips.txt').readlines()[11:])
    raw_data = data_file.split('\n')
    del raw_data[-1]
    
    for i in raw_data:
        data_list.append(i[0:17])

    for i in data_list:
        x = i.split()
        y = tuple(x)
        rain_data.append(y)
    print(len(rain_data))
    print(rain_data)
    print(rain_data[0][1])
    print(rain_mean(rain_data))

main()
