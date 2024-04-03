import socket
import random
from time import sleep
import json
from socket import *


serverName = '255.255.255.255'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

carSpeedData = {
    "censorName": "Alexanders Speed Sensor",
    "carSpeed": 0  
}

while True:
    carSpeedData["carSpeed"] = random.randint(1, 200)
    jsonData = json.dumps(carSpeedData)
    print(jsonData)
    sleep(random.randint(1, 5))
    clientSocket.sendto(jsonData.encode(), (serverName, serverPort))

    
