"""
 ******************************************************************************
 *   @file  	 client.py
 *   @brief 	 This file contains all the function.
 *   @date       Dec 4, 2021
 *   @author	 Kaan Dönmez
 *   @version    1.0.0
 ******************************************************************************
"""

import socket

"""
@brief: Variable declarions made
@param: header : Byte of data
        portNumber : Connection port number
        format : encoding format
        serverIpAdrress : Server ip adrress
        serverAdrress : server adress parameters
"""

header, portNUmber, format, serverIpAddress = 64, 5050, 'utf-8', "172.20.80.11"
serverAddress = (serverIpAddress, portNUmber)

"""
@brief: Messages related with server station.
"""
disconnectMessage = "Disconnect"

"""
@brief: Server type declared.
"""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""
@brief: Connect to server.
"""
client.connect(serverAddress)


def Send(sendingMessage):
    """
    @brief: This function send message to server.
    """
    message = sendingMessage.encode(format)
    messageLength = len(message)
    send_length = str(messageLength).encode(format)
    send_length += b' ' * (header - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(format))
