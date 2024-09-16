import os

def restart():
    os.system("shutdown /r /t 1")
def restartTime():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")