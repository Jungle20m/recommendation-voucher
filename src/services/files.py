import csv


def read_lines(file_location):
    try:
        rows = []
        file = open(file_location, 'r')
        lines = file.readlines()
        for line in lines:
            line = line.rstrip("\n")
            rows.append(line)
        file.close()
        return rows
    except Exception as e:
        print(e)
        return []
    

def load_csv(file_location):
    try:
        with open(file_location) as csv_file:
            data = []
            rows = csv.reader(csv_file, delimiter=',')
            for row in rows:
                data.append(row)
            return data
    except Exception as e:
        print(e)
        return []