import numpy as np
import datetime

def rain_mean(list_input):
    sub_total = 0
    total_days = (len(list_input))
    
    for item in range(total_days):
        indice = list_input[item]
        daily = indice[1]
        sub_total += int(daily)
    total = sub_total / total_days
    return total

def variance(variance_input):
    # variance_result = sum((xi - mean_input) ** 2 for xi in variance_input) / len(variance_results)
    variance_result = np.var(variance_input)
    return variance_result

def max_rain_year(data_input):
    year_dict = {}
    count = 0
    year_list = []
    year_averages = {}
    average_values = []

    for elem in data_input:
        elem_date = elem[0]
        year_dict[f'{elem_date}'] = [elem[1]]
        date = datetime.datetime.strptime(elem_date, '%d-%b-%Y')
        year = date.year
        if year in year_list:
            continue
        else:
            year_list.append(year)

    for elem in year_list:
        count = 1
        year_sum = 0        
        elem_year = elem
        for elem in data_input:
            elem_date = elem[0]
            date = datetime.datetime.strptime(elem_date, '%d-%b-%Y')
            if date.year == elem_year:
                year_sum += int(elem[1])
                count += 1
            else:
                continue
        
        average = year_sum / count
        average_values.append(average)
        year_averages[f'{elem_year}'] = average
        average_values.sort(reverse = True)
    
    for value in year_averages.values():
        if value == average_values[0]:
            year_max = average_values[value]
    print(average_values)
    print(year_max)



def main():

    data_list = []
    rain_data = []
    variance_list = []
    
    
    data_file =''.join(open('columbia_ips.txt').readlines()[11:])
    raw_data = data_file.split('\n')
    del raw_data[-1]
        
    for i in raw_data:
        data_list.append(i[0:17])
    
    for i in data_list:
        x = i.split()
        y = tuple(x)
        rain_data.append(y)
    
    for i in rain_data:
        x = i[1]      
        variance_list.append(int(x))
    
    print(f'The mean rain day value is {rain_mean(rain_data)}.')
    mean_value = float(rain_mean(rain_data))
    print(f'The variance value of the data is {variance(variance_list)}')

    max_rain_year(rain_data)


main()
