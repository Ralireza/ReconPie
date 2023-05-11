import csv

# data to be written to csv file
data = [['Name', 'Age'], ['John', '25'], ['Jane', '30'], ['Smith', '28']]

# name of csv file
filename = "example.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the data rows
    csvwriter.writerows(data)