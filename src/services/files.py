

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