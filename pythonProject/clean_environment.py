import requests

try:
    requests.get('http://127.0.0.1:5000/stop_server')
except:
    print("Failed to contact server")
