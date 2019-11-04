# How to setup raspberry pi

Raspberry pi comes with the raspberry pi board and the operating system is already present in the memory card. Follow the below steps to install the operating system and configure camera.

- Insert the SD card into the raspberry pi.
- Connect keyboard, monitor and the power cord into the pi and make sure to connect keyboard to the port named &#39;USB&#39;. Monitor should be connected using HDMI cable.
- Switch on the power supply and installation will start automatically.
- Once installation completes, follow the steps and choose the location and region settings if prompted.
- By default, the username is **&quot;pi&quot;** and the password is **&quot;raspberry&quot;**.

## Setting up WiFi

- When the desktop shows, click on the WiFi icon on the top left corner of the screen.
- Choose the wifi network that you wish to connect to and enter password.

## Setting up time zone and country

If the system time is not correct then you might need to setup the time zone and country also. Follow the below steps for this:

- Click on the terminal icon present in the taskbar on the top.
- Type &#39;sudo raspi-config&#39; and hit &#39;enter&#39;.
- A menu will be displayed
- Choose &quot;Localization Options&quot;:
  - Select &quot;Change TimeZone&quot;, and choose &quot;US&quot; from the list and then select appropriate time zone in US
  - If the time is still not set, choose &quot;Change Wi-Fi country&quot; from the &quot;Localization Options&quot; and choose US from the list.

## Fetching the IP address of the raspberry pi

For connecting with the raspberry pi over the WiFi, it is required that both pi and laptop/desktop are connected to the same Wi-Fi network. IP address will be used to access pi from the system.

Type **&quot;ifconfig&quot;** on the terminal in pi and see the number written after _&quot;inet&quot;_ in the _&quot;wlan0&quot;_ section. It is usually of the form 192.xxx.xxx.xxx

## Enabling SSH and Camera on pi

- Click on the terminal icon present in the taskbar on the top.
- Type &#39;sudo raspi-config&#39; and hit &#39;enter&#39;.
- A menu will be displayed
- Choose &quot;Interfacing Options&quot;:
  - Select &quot;Camera&quot; and choose &quot;yes&quot; to enable camera.
  - Select &quot;SSH&quot; and choose &quot;yes&quot; to enable SSH.

## Installing required software on the personal computer

Software is required for communicating with the raspberry pi and transferring files between the laptop/desktop and the raspberry pi. One application is required to remotely run codes and scripts on the pi which is **Putty**. Another software named &quot; **WinSCP**&quot; will be used to transfer files between pi and the laptop/desktop. Links to both the software are mentioned below. There are lot of software available for free and can be used to do the same task.

Putty: [https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

WinSCP: [https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)

### Running codes from system remotely into pi

Once the software are downloaded, run putty on the system and enter the IP address of the raspberry pi. Click _connect_ and terminal will be opened. If any pop-up window opens, choose _&quot;yes&quot;_ to indicate that you want to connect to pi from system.

Now, you can run all the codes from system into the pi.

### Transferring files from system to/from pi

WinSCP (or any other file transfer software) will be used for this task. For this, open WinSCP and enter all the details like IP Address, username, and the password of pi.

Once this connection is successful, you can see the file directory on the system and in the pi. Drag and drop the files that you want to transfer from one place to the other. If same name files are present the files in the destination location will be replaced.