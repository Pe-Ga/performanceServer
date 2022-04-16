import urllib.request
import csv
import time

# Parse user input form integer -> string
# user_input = str(input("Enter unix epochtime: "))

user_input = "1649156500"

with urllib.request.urlopen("http://127.0.0.1:8001/getdata?time=" ) as response:
    response = [line.decode('utf-8') for line in response.readlines()]
    reader = csv.DictReader(response, delimiter='|')

    epoch_time = int(user_input)
    user_input = time.strftime('%Y-%m-%dT%H-%M-%S', time.localtime(epoch_time))

    f = open(user_input + ".json", "w")
    f.write('{\n')
    f.write('\t"PerformanceData":[\n')

    is_first_line = True

    for row in reader:
        epoch_time = row['Timestamp']
        epoch_time = int(epoch_time)
        starttime = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(epoch_time / 1000000))
        duration = row['Duration']
        key1 = row['Key']
        value = '"value":{'
        is_first_item = True


        dict_lst = row.items()
        lst = list(dict_lst)
        sublst = lst[3:]

        #for key, val_of_key in sublst:
        for key, val_of_key in list(row.items())[3:]:
            if key != "" and val_of_key is not None:
                if not is_first_item:
                    value += ','
                value += '\n\t\t\t\t"'+ key + '"' + ':' + val_of_key
                is_first_item = False
        value += "\n\t\t\t}"


        if is_first_line:
            is_first_line = False
        else:
            f.write(',\n')
        f.write(
            '\t\t{\n\t\t\t"starttime":"' + starttime + '",\n\t\t\t"duration":' + duration + ',\n\t\t\t"key":{\n\t\t\t\t"key":"' + key1 + '"\n\t\t\t},\n\t\t\t' + value + '\n\t\t}')

    f.write('\n\t]\n}\n')
    f.close()
