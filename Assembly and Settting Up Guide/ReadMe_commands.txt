## Sequence of commands for setting up tranfer of images from pi to laptop

1. Interrupt the raspberry pi startup

2. When the login screen shows enter the credentials
	Username: pi
	Password: raspberry

3. Check if pi is already connected to the WiFi using: "ifconfig"
	[If there is a IP address mentioned then it shows that pi is connected to the WiFi network]

4. Run: "sudo iwlist wlan0 scan"
	This scans the available WiFi networks and shows that WiFi is turned on.

5. Open the WiFi configuration file using: "sudo nano /etc/wpa_supplicant/wpa_supplicant.conf"
	This file will have the following details:
		network={
		    ssid="4112C-Wireless"
		    scan_ssid=1
		    psk="U$DA2016!"
		}
	ssid is the WiFi name and psk is the password of that WiFi.

6. Once you entered the details, press Ctrl-X and then Y and then hit Enter. This is save the modifications.

7. Run: "sudo wpa_cli -i wlan0 reconfigure"
	This will make the pi scan for the WiFi networks.

8. Run: "ifconfig" and check if the IP address is now present. If not, repeat steps 7 and 8.

9. From the laptop use SSH to run commands or use WinSCP to transfer files. 

