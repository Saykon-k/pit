import csv
def cvs_norm(csv_file):
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
    print('\n another way \n')
def csv_dict(csv_file):
    csv_dict = csv.DictReader(csv_file)
    line_count = 0
    for row1 in csv_dict:
        if line_count == 0:
            print(f'Column names are {", ".join(row1)}')
            line_count += 1
        print(
            f'\t{row1["name"]} works in the {row1["department"]} department, and was born in {row1["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')