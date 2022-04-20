import re
import os.path
import csv
import time


def open_and_read(file_path):
    return os.path.exists(file_path) is True and os.path.getsize('start_time.txt') != 0


def error_msg_past(error_msg):
    reg = re.compile('time is too much in the past more than 3 days+')
    return bool(re.match(reg, error_msg))


def error_msg_future(error_msg):
    reg = re.compile('time is in the future +')
    return bool(re.match(reg, error_msg))


# open and read s_time from file
def read_start_time_from_file(path):
    with open(path, 'r') as file: # ToDo: What if open fails?
        line = file.readline()
        return int(line)


def write_to_json(http_response, start_time):
    # Create DictReader for http_response content
    http_response = [line.decode('utf-8') for line in http_response.readlines()]
    reader = csv.DictReader(http_response, delimiter='|')

    # Write to json file
    file_name = time.strftime('%Y-%m-%dT%H-%M-%S', time.localtime(start_time))

    f = open(file_name + ".json", "w") # ToDo: What if open fails?
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

        for key, val_of_key in list(row.items())[3:]:
            if key != "" and val_of_key is not None:
                if not is_first_item:
                    value += ','
                value += '\n\t\t\t\t"' + key + '"' + ':' + val_of_key
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


def write_start_time_to_file(new_s_time, path):
    with open(path, 'w') as file:
        file.write(str(new_s_time))


def valid_stime():
    s_time = int(time.time())
    return s_time - s_time % 300
