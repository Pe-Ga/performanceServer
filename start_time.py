
import time


# open and read s_time from file
def read_start_time_from_file():
    with open('start_time.txt', 'r') as file:
        line = file.readline()
        return int(line)


def valid_stime(s_time):
    if s_time % 300 == 0:
        return s_time
    else:
        remainder = s_time % 300
        s_time -= remainder
        return s_time

# get local time as epochtime
def get_local_time():
    current_time = time.time()
    return current_time
