import datetime

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