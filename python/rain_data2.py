import statistics

def rain_mean(list_input):
    sub_total = 0
    total_days = (len(list_input))
    print(total_days)
    for item in range(total_days):
        indice = list_input[item]
        daily = indice[1]
        sub_total += int(daily)
    total = sub_total / total_days
    return total

def variance(mean_input):
    pass



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
    
    print(f'The mean rain day value is {rain_mean(rain_data)}.')
    mean_value = float(rain_mean(rain_data))
    print(variance(mean_value))
main()
