from os import listdir,getcwd, remove, system
from threading import Thread
from time import sleep
from shutil import move
import clamd

def UpdateClamAV():
    while True :
        try:
            #sleep(60)
            system("freshclam")
            sleep(86400)  #24hour
        except : pass
try :
    
    system("service clamav-daemon start") #IMPORTANT
    VirusKiller = clamd.ClamdUnixSocket()
    oldlist = list()
    newlist = list()
    PathScan = getcwd()+"/Scanned/"
    PathToScan = getcwd()+"/ToScan/"
    ThreadUpdate = Thread(target=UpdateClamAV)
    ThreadUpdate.start()
    while VirusKiller.ping() != "PONG" : pass
    print("init pass") 
    
except Exception as e: print("Erreur survenu : " + str(e))

while True:
    
    try:
        newlist = listdir(PathToScan)

        if newlist != oldlist : 
            for i in newlist:
                file = PathToScan+i
                scanReport = VirusKiller.scan(file)
                if scanReport[file][0] == 'OK': 
                    move(file,PathScan)
                else : 
                    remove(file)
                    print(scanReport)

            oldlist = listdir(PathToScan)
        else :
            oldlist = newlist
    except Exception as e:pass#print(str(e))
    sleep(60)



