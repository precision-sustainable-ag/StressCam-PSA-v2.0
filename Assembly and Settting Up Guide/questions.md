Questions about StressCam

- --Where is save the file autoboot.txt when it is created the OS SD Card? When \*.img is load in SD Card could be created some partitions, which one will have the information (autoboot)



You insert your SD card to your PC (use a SD card reader if your PC doesn?t have SD card slot), open the RECOVERY partition and create a text file named &quot;autoboot.txt&quot; there. [Source: http://www.uugear.com/doc/WittyPi2\_UserManual.pdf]



- --Which is it the process to setup files and to run properly takeImage.py, is it necessary to add command lines in OS files. I found one of them in etc/rc.local, are there more like this.

No, modifying the file in etc/rc.local will make the pi run takeImage.py during the startup and it will continue to run until it encounters any errors/issues.

- --What about other \*.py required. Is it necessary to add a command line in any OS file?

No, you need not add that file in any other OS file.

- --Are there other steps to set up the camera. This question should solve for answering to any developer.

You need to type &quot;sudo raspi-config&quot; on the command line and then go to interfaces option. There you&#39;ll find option to enable camera interface for the rasberry pi.