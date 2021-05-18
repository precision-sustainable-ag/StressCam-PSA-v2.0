import subprocess

bashCmd = "sudo wpa_cli -i wlan0 reconfigure"

process = subprocess.Popen(bashCmd.split(), stdout=subprocess.PIPE)

output, error = process.communicate()

print("OUTPUT:",output)
print("Error:",error)
