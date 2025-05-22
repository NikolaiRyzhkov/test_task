import requests
import json
import time


def get_data_from_server(link: str) -> dict:
    json_str = requests.get(link).text # get data
    json_dict = json.loads(json_str)    # transfer str to dict
    return json_dict

def transfer_time_to_human_format(unix_timestamp: int) -> str:
    unix_timestamp = str(unix_timestamp / 1000)
    unix_timestamp = float(unix_timestamp)
    time_struct = time.gmtime(unix_timestamp)
    human_format = time.strftime('%D %H %M %S', time_struct)
    return human_format

def delta_time(link: str) -> int:
    client_unix_timestamp = int((time.time())) * 1000  # client time
    data = get_data_from_server(SERVER_LINK)    # data from server
    server_unix_timestamp = data['time']    # server time
    delta = server_unix_timestamp - client_unix_timestamp
    return delta


if __name__ == '__main__':

    SERVER_LINK = 'https://yandex.com/time/sync.json?geo=213'

    data = get_data_from_server(SERVER_LINK)    # get data
    server_time = data['time']
    server_UTS = data['clocks']['213']['offsetString']

    #raw data
    print('raw data:')
    print(data, '\n')

    #Time and time zone in a human format
    print('time:', transfer_time_to_human_format(server_time))
    print('UTS:', server_UTS, '\n')

    #Delta between request and time on the server 
    print('Delta between request and time on the server:')
    number_of_requests = 5
    list_delta = 0
    for i in range(1, number_of_requests + 1):
        delta = delta_time(SERVER_LINK) / 1000
        list_delta += delta
        print(i, delta, 's') 
    
    average_delta = list_delta / number_of_requests
    print('average delta:', average_delta, 's')
