import csv

def read_csv(path):
  with open(path,'r') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    header=next(reader)
    data = []
    #print(header)
    for row in reader:
      iterable = zip(header,row)
      #print(list(iterable))
      country_dict = {
        key:value for key,value in iterable
      }
      #print(country_dict)
      data.append(country_dict)
    return data  


#data = read_csv('data.csv')      
#print(data[0])