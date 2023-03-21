import time

def file():
    while True:
        with open('apache-status.txt') as f:
            regels = f.readlines()
            if 'active' in regels[2]:
                print(".")
            elif 'failed' in regels[2]:
                tijd = (regels[2].split(' '))
                print("[" + tijd[7] + ' ' + tijd[8] + '] Apache entered a failed state!' )
            time.sleep(10)

print("Starting to monitor apache-status.txt in current directory.")
file()
