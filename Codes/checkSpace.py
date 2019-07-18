import subprocess

def getAvail():
    df = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE)
    output = df.communicate()[0]
    device, size, used, available, percent, mountpoint = output.split("\n")[1].split()
    
    return int(available[:-1])

