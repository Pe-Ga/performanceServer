import urllib.request

import time
import os.path
from start_time import read_start_time_from_file, valid_stime, get_local_time
from send_request import send_request_to_server

path = 'C:\\Users\\gamsj\\PycharmProjects\\performanceServer\\start_time.txt'


if os.path.exists(path) is True:
    request_input = read_start_time_from_file() + 300                 # Read from text file add 5 min / 300 seconds
    request_input = str(request_input)
    send_request_to_server(request_input)                   # Send request to server
else:
    alt_start_time = valid_stime(int(get_local_time()))
    alt_start_time -= 900                                   # Current time - 15 min
    alt_start_time = str(alt_start_time)                    # Convert back to string for server request
    send_request_to_server(alt_start_time)                  # Send request to server



# write new s_time to text file

with open('start_time.txt', 'w') as file:
    file.write("write new start time from last slice")
