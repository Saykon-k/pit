import csv
import meth_csv as meth
with open ('name_csv.txt') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ',')
    meth.cvs_norm(csv_file)
    second = open('name_csv.txt', 'r')
    meth.csv_dict(second)
with open ('new_file.txt', mode ='w') as csv_file2:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file2, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})