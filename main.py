from os import listdir,getcwd, remove, system
from threading import Thread
from time import sleep
from shutil import move
import clamd

def UpdateClamAV():
    while True :
        try:
            system("freshclam")
            sleep(86400)  #24hour
        except : pass

VirusKiller = clamd.ClamdUnixSocket()
oldlist = list()
newlist = list()
PathScan = getcwd()+"/Scan/"
PathToScan = getcwd()+"/ToScan/"
ThreadUpdate = Thread(target=UpdateClamAV)
ThreadUpdate.start()
while VirusKiller.ping() != "PONG":pass

while True: 
    newlist = listdir("ToScan")

    if newlist != oldlist : 
        for i in newlist:
            file = PathToScan+i
            scanReport = VirusKiller.scan(file)
            if scanReport[file][0] == 'OK': 
                move(file,PathScan)
            else : 
                remove(file)
                print(scanReport)

        oldlist = listdir("ToScan")
    else :
        oldlist = newlist




