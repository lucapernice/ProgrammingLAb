from datetime import datetime

my_file = open('shampoo_sales.csv','r')
def get_datetime(file):
    dates=[]
    for line in file:
        element = line.split(',')
        if element[0] != "Date":
            dates = datetime.strptime(element[0] , '%d−%m−%Y' )
            value = element[1]
            dates.append(dates)
    return dates


dates = get_datetime(my_file)

for data in dates:
    print(data.strftime('%d−%m−%Y'))
