import os

try:
    import os
    from os import system
    system("title " + "Ip Pinger,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass

print("""
______ _                       
| ___ (_)                      
| |_/ /_ _ __   __ _  ___ _ __ 
|  __/| | '_ \ / _` |/ _ \ '__|
| |   | | | | | (_| |  __/ |   
\_|   |_|_| |_|\__, |\___|_|   
                __/ |          
               |___/           """)
ip = input("Enter Ip: ")
while True:
    os.system("ping -n 4 " + ip)
