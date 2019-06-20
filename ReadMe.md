![camera_installation](camera_installation.jpg)

## DOWNLOADING THE RASPBERRY PI OS
•	Go to https://www.raspberrypi.org/downloads/raspbian/
•	Click “Download ZIP” for the Raspbian Stretch with Desktop
•	Unzip the downloaded file and copy the contents of this folder as is into the newly formatted SD card
•	Create a new file name “autoboot.txt” and write “boot_partition=6” in it. (This is required for proper functioning of the Witty Pi)
•	Insert the SD card into the raspberry pi and turn the power ON. It should start the installation and follow the steps. 
•	Choose to download the “Raspberry Pi OS Debian Desktop version if it asks during installation.

## Downloading the Witty Pi software on raspberry pi
Once the raspberry pi OS has been successfully installed, connect the raspberry pi with Wi-Fi and then follow the below steps for downloading Witty Pi software.
•	Type: wget http://www.uugear.com/repo/WittyPi2/installWittyPi.sh
•	If the download was successful, type: sudo sh installWittyPi.sh
•	If it prompts something regarding fake-hwclock package, press ‘y’. Since we want to remove this package.
•	Then it will ask about Qt 5 GUI installation, for which press ‘n’ since we can use terminal to perform the setup.
•	If everything is properly installed, then it will say that you need to reboot the pi.
•	Type: reboot, to reboot the raspberry pi.
Setting up the witty pi
•	Type: cd wittyPi
•	Now type: sudo ./wittyPi.sh
•	This should start a wittyPi interface, if it doesn’t then redo the installation steps.
•	For the steps for configuring the raspberry pi startup time and shutdown time,  http://www.uugear.com/doc/WittyPiMini_UserManual.pdf use this manual.

## Troubleshooting / Checking raspberry pi functioning
Start the remote session through SSH using the IP address of the raspberry pi. We used putty software for this, but many other alternatives are available. Once you are able to access the pi, use the below codes for different tasks that you might require to perform.

Check the name of raspberry pi
Type: cat myname.txt
This gives the number of the raspberry pi.

See if code was invoked
Type: cat logs.txt
This will display the contents of the logs file and it shows when the code was invoked, and image is taken.

See the list of images on the pi
Type: ls images/
This will give a list of all images taken and stored in the raspberry pi.

See the date and time on the pi
Type: date

Check if code is running
Type: ps -aef | grep python
The first two lines should have “takeImage.py” in the end. If not then, there has been some issue and the code has stopped working.





