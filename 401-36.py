#!/usr/bin/python3
# Nick Alderete
# 





import subprocess




def banner_grabbing(target, port, grab_type):
    if grab_type == "netcat":
        command = f"nc -v {target} {port}"
    elif grab_type == "telnet":
        command = f"telnet {target} {port}"
    elif grab_type == "curl":
        command = f"curl {target}:{port}"
    else:
        command = f"nmap -p- {target}"
    
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error executing the command: {e.output.decode()}")

def main():
    while True:
        target = input("Enter the URL or IP address: ")
        port = input("Enter the port number: ")
        grab_type = input("Enter the banner grab type (netcat, telnet, curl, nmap): ")

        banner_grabbing(target, port, grab_type)

        choice = input("Do you want to run another scan? (yes/no): ")
        if choice.lower() != "yes":
            break

if __name__ == "__main__":
    main()
