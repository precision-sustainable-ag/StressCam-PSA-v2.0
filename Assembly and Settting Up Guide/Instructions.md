# Building and Setting Up

The materials list could find in this link

1. Take the box NBF-32002 and do hole of 1 ½&quot; in the middle of the tap. Use a rotatory tool kit to for edge polishing. Use Spade bit (1 ½&quot;).
2. Glue Sensei 37-58mm Step-Up Ring with silicone.
3. Drill a hole with a ½&quot; bit to put the cable gland in one of the shortest sides of the box.
4. Cut a rectangle wood 3.1&quot; by 4.25&quot; in a Portable Tabletop Saw.
5. Put the rectangle wood inside of tap and mark the point center in line with the hole do it in step 1.
6. In this point center, do a hole of ½&quot;.
7. Connect the Raspberry Camera to Raspberry Pi with the flexible cable

# Step 1 Micro SD Card and O.

The Raspberry Pi should work with any compatible Micros SD card, although there are some guidelines that should be followed

## SD card size (capacity)

For installation of NOOBS or the image installation of Raspbian, the minimum recommended card size is 8GB and the maximun is 64Gb. In this tutorial we will use a micro SD car of 16Gb.

## SD card class

The card class determines the sustained write speed for the card; a class 4 card will be able to write at 4MBs, whereas a class 10 should be able to attain 10 MBs. We will use a class 10 because is easier find it in the market.

## Troubleshooting

If you are having trouble with corruption of your Micro SD cards, make sure you follow these steps

- --Make sure you are using a genuine SD card.
- --Make sure you are using a good quality power supply. You can check your power supply by measuring the voltage between TP1 and TP2 on the Raspberry Pi; if this drops below 4.75V when doing complex tasks then it is most likely unsuitable.
- --Make sure you are using a good quality USB cable for the power supply. When using a lower quality power supply, the TP1-&gt;TP2 voltage can drop below 4.75V.
- --Make sure you are shutting your Raspberry Pi down properly before powering it off. Type sudo halt and wait for the Pi to signal it is ready to be powered off by flashing the activity LED.

If you have an older Micro SD card, you can reused if you flow these steps

- --Insert micro SD in an adapter and then insert them in your computer (Windows)
- --Open a command browser. Type cmd in start text box.
- --In this window, type diskpart. New window will be opened.
- --In this new window, type list disk. Identify the number of micro SD card ( a ).
- --Select this disk ( a ), type select disk a. In a place, type the corresponding number to Micro SD card.
- --Type clean.
- --Type create partition primary.
- --Type select partition 1.
- --Type format fs=fat32 quickly label=pi.
- --Type assign letter=Z.
- --Type exit.
- --Close window.
- --Copy all files in the new unit pi(Z), in the same way if you have a new micro SD card.

# Step 2 Copy OS files in Micro SD card, install OS Raspbian and updateupgrade system

Raspberry pi comes with the raspberry pi board and the operating system is already present in the memory card. Follow the below steps to install the operating system and configure camera.

- --Go to [httpswww.raspberrypi.orgdownloadsraspbian](httpswww.raspberrypi.orgdownloadsraspbian).
- --Click &quot;NOOBS&quot; , and then download zip for NOOBS Offline and network install.
- --Unzip the downloaded file and copy the contents of this folder as is into the Micro SD card configured in last steps.
- --Remove this Micro SD card for your computer and put it in the Raspberry Pi Zero W. Connect monitor, mouse, keyboard and USB power, and follow the instructions to install Raspbian system.
- --Connect to Wi-Fi (Wi-Fi Access point to download images in the future, preferable. If It is not possible, connect to Wi-Fi network to connect with your computer by SSH).
- --By default, the username is &quot;pi&quot; and the password is &quot;raspberry&quot;.
- --When the desktop shows, click on the Wi-Fi icon on the top left corner of the screen.
- --Choose the Wi-Fi network that you wish to connect to and enter password.
- --Follow locations, time and systems updates instructions.
- --Reboot the system typing &quot; sudo reboot&quot; in terminal.
- --Continue with Step 3.

## Troubleshooting

It is possible that the system does not been installed, because some problems with the board could happen. You can figure out that because

- --The installation process is longer than habitual.
- --The system cannot be update or upgrade.
- --Some hardware errors appear when you test the camera (See Step 3).

# Step 3 Enable camera module and SSH communication

When the system finish to updateupgrade. Follow the below steps for this

- Click on the terminal icon present in the taskbar on the top.
- Type &#39; sudo raspi-config&#39; and hit &#39; enter&#39;.
- A menu will be displayed
- Choose &quot;Localization Options&quot;
  - Select &quot; Change TimeZone&quot;, and choose &quot; US&quot; from the list and then select appropriate time zone in US
  - If the time is still not set, choose &quot; Change Wi-Fi country&quot; from the &quot; Localization Options&quot; and choose US from the list.
  - Choose &quot; Interfacing Options&quot;
  - Select &quot; Camera&quot; and choose &quot; yes&quot; to enable camera.
  - Select &quot; SSH&quot; and choose &quot; yes&quot; to enable SSH.
  - Reboot the raspberry. Typing &quot; sudo reboot&quot; or accept to reboot when you exit of the menu.

## Troubleshooting

- --XXXX

# Step 4 Test camera module and install of files to have a time lapse camera in your raspberry.

## Prerequisites

## Fetching the IP address of the raspberry pi.

For connecting with the raspberry pi over the Wi-Fi, it is required that both pi and laptopdesktop are connected to the same Wi-Fi network. IP address will be used to access pi from the system.

Type &quot;ifconfig&quot; on the terminal in pi and see the number written after _&quot;inet&quot;_ in the _&quot;wlan0&quot;_ section. It is usually of the form 192.162.1.xxx

## Installing required software on the personal computer.

Software is required for communicating with the raspberry pi and transferring files between the laptopdesktop and the raspberry pi. One application is required to remotely run codes and scripts on the pi which is Putty or you can use &quot; cmd&quot; Command Window in Windows System. Another software named &quot; WinSCP&quot; will be used to transfer files between pi and the laptopdesktop. Links to both the software are mentioned below. There are lot of software available for free and can be used to do the same task.

Putty [httpswww.chiark.greenend.org.uk~sgtathamputtylatest.html](httpswww.chiark.greenend.org.uk~sgtathamputtylatest.html)

WinSCP [httpswinscp.netengdownload.php](httpswinscp.netengdownload.php)

### Running codes from system remotely into pi.

- --Open command window, typing &quot; cmd&quot; in the star text box of Windows.
- --Type &quot;ssh [pi@192.168.xx](mailtopi@192.168.xx)&quot;, where &quot;xx&quot; corresponds to the last numbers of IP Address of Raspberry Pi.
- --Type &quot;yes&quot;, then hit &quot;enter&quot;.
- --And the system request password. Type &quot;raspberry&quot;
- --Immediately you can see in green and blue colors &quot;pi@raspberry $&quot;
- --To test the camera, type &quot;raspistill -o test.jpg&quot;. Verify that the system saves in a &quot;pi&quot; folder the image &quot;test.jpg&quot;.

### Transferring files from system tofrom pi.

WinSCP (or any other file transfer software) will be used for this task. For this, open WinSCP and enter all the details like IP Address, username, and the password of pi.

Once this connection is successful, you can see the file directory on the system and in the pi. Drag and drop the files that you want to transfer from one place to the other. If same name files are present the files in the destination location will be replaced.

Move all files that you find in the folder &quot; Codes&quot; of GitHub repository ([httpsgithub.comprecision-sustainable-agStress-CamtreemasterCodes](httpsgithub.comprecision-sustainable-agStress-CamtreemasterCodes)), directly in the folder &quot; homepi&quot; of raspberry pi.

### Modify OS file (etcrc.local) to run continuously the program to take pictures.

- Type in the terminal&#39;s raspberry &quot; sudo nano etcrc.local&quot;.
- In this file, type before last line (exit 0) &quot; sudo python homepitakeImage.py &amp;&quot;, this command line does the system runs continuously the file takeImage.py.
- Type in terminal &quot;sudo reboot&quot;
- Test the camera working, It should be turned at least by 30 minutes.
- Inspect the files in the folder &quot;images&quot;

## Troubleshooting

Sequence of commands for setting up tranfer of images from pi to laptop

1. Interrupt the raspberry pi startup

2. When the login screen shows enter the credentials

 Username pi

 Password raspberry

3. Check if pi is already connected to the Wi-Fi using &quot;ifconfig&quot;

 [If there is a IP address mentioned then it shows that pi is connected to the Wi-Fi network]

4. Run &quot;sudo iwlist wlan0 scan&quot;

 This scans the available Wi-Fi networks and shows that Wi-Fi is turned on.

5. Open the Wi-Fi configuration file using &quot;sudo nano etcwpa_supplicantwpa_supplicant.conf&quot;

 This file will have the following details

  network={

      ssid=&quot;4112C-Wireless&quot;

      scan_ssid=1

      psk=&quot;U$DA2016!&quot;

  }

 ssid is the Wi-Fi name and psk is the password of that Wi-Fi.

6. Once you entered the details, press Ctrl-X and then Y and then hit Enter. This is save the modifications.

7. Run &quot;sudo wpa_cli -i wlan0 reconfigure&quot;

 This will make the pi scan for the WiFi networks.

8. Run &quot;ifconfig&quot; and check if the IP address is now present. If not, repeat steps 7 and 8.

9. From the laptop use SSH to run commands or use WinSCP to transfer files.

When you connect WinSCP, Please don&#39;t accept updates , this could be change the key host and It could give you some communications problems.

-------------

• Create a new file name &quot;autoboot.txt&quot; and write &quot;boot_partition=6&quot; in it. (This is required for proper functioning of the Witty Pi)

• Insert the SD card into the raspberry pi and turn the power ON. It should start the installation and follow the steps.

• Choose to download the &quot;Raspberry Pi OS Debian Desktop version if it asks during installation.

Step 3 Install OS in Raspberry

Step 4 Set up location time, language and connect a WiFi Network.

Step 5 Update files.



Step 7 Verify If camera model works properly

Step 8 Copy all programs files in pi folder

Step 9 Edit rc.local file in this location etcrc.local

Sudo nano etcrc.local

sudo python homepitakeImage.py &amp;

Step 9 Download wittyPi intallers

Step 10 Set Up wittyPi

Step 11 save autoboot.txt file in RECOVERY partition