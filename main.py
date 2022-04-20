from functions import *
import urllib.request
import urllib.error


path = 'start_time.txt'

if open_and_read(path) is True:
    s_time = read_start_time_from_file(path)
else:
    s_time = valid_stime()
    s_time -= 900

while True:
    s_time += 300

    url = 'http://127.0.0.1:8001/getdata?time=' + str(s_time)

    try:
        response = urllib.request.urlopen(url)

    except urllib.error.HTTPError as e:
        # Return code error (e.g. 404, 501, ...)
        http_body = e.read().decode()
        if error_msg_past(http_body):
            pass
        elif error_msg_future(http_body):
            exit()
        else:
            print("Error: " + http_body)
            exit()

    except urllib.error.URLError as e:
        # Not an HTTP-specific error (e.g. connection refused)
        print('URLError: {}'.format(e.reason))
        exit()
    else:
        # 200
        write_to_json(response, s_time)
        write_start_time_to_file(s_time, path)
