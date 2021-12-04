"""
 ******************************************************************************
 *   @file  	 server.py
 *   @brief 	 This file contains all the function.
 *   @date       Dec 4, 2021
 *   @author	 Kaan Dönmez
 *   @version    1.0.0
 ******************************************************************************
"""

import socket
import threading

"""
@brief: Variable declarions made
@param: header : Byte of data
        portNumber : Connection port number
        format : encoding format
        ipAdrress : Device ip adrress (auto)
        serverAdrress : server adress parameters
"""
header, portNumber, format = 64, 5050, "utf-8"
ipAddress = socket.gethostbyname(socket.gethostname())
serverAddress = (ipAddress, portNumber)

"""
@brief: Messages related with server station.
"""
disconnectMessage = "Disconnect"

"""
@brief: Server type declared.
"""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""
@brief: Server bind server adrress
"""
server.bind(serverAddress)


def HandleClient(conn, addr):
    """
    @brief: This function handle client.
    """

    print(f"{addr} connected to server.")

    connected = True
    while connected:
        messageLength = conn.recv(header).decode(format)
        if messageLength:
            messageLength = int(messageLength)
            messagge = conn.recv(messageLength).decode(format)
            if messagge == disconnectMessage:
                connected = False

            print(f"[{addr}] {messagge}")
            conn.send("Message received".encode(format))

    conn.close()


def StartComumnication():
    """
    @brief: This function start communication. 
    """

    server.listen()
    print(f"Server is listening on {ipAddress}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=HandleClient, args=(conn, addr))
        thread.start()
        print(f"Active Connections : {threading.activeCount() - 1}")


StartComumnication()
