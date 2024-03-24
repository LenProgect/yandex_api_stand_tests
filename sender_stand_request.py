import configuration
import requests

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count":20})

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_docs()
print(response.status_code)

response1 = get_logs()
print(response1.status_code)
print(response.headers)

response2 = get_users_table()
print(response.status_code)