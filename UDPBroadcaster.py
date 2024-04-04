import socket
import random
from time import sleep
import json
from socket import *


serverName = '255.255.255.255'
serverPort = 10100
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

carSpeedData = {
    "SensorName": "Alexanders Speed Sensor",
    "CarSpeed": 0  
}

while True:
    carSpeedData["CarSpeed"] = random.randint(1, 200)
    jsonData = json.dumps(carSpeedData)
    print(jsonData)
    clientSocket.sendto(jsonData.encode(), (serverName, serverPort))
    sleep(random.randint(1, 5))

    
