import subprocess
import argparse
subprocess.call("date")

print "Usage: python SCRIPT server_username server_ip/hostname client_username client_ip/hostname\n"

print "For example: python LinuxToWindowsNodejsTest.py yduan am14-09 a-yduan am13-02\n"


parser = argparse.ArgumentParser()
parser.add_argument("server_username", help="the username of the machine on which you would like to deploy the Node.js server")

parser.add_argument("server_hostname", help="the hostname or ip of the machine on which you would like to deploy the Node.js server")

parser.add_argument("client_username", help="the username of the machine on which you would like to deploy the Node.js client")

parser.add_argument("client_hostname", help="the hostname or ip of the machine on which you would like to deploy the Node.js client")

args = parser.parse_args()
print ("server username is: " + args.server_username)
print ("server hostname/ip is: " + args.server_hostname)
print ("client username is: " + args.client_username)
print ("client hostname/ip is: " + args.client_hostname + "\n\n")

print "Copying Node.js scripts to the server and client"


serverLogin = args.server_username + "@" + args.server_hostname

# copy script to server and run
copyDestOnServer = serverLogin + ":/tmp"

subprocess.call(["./pscp.exe", "main.js", copyDestOnServer])

subprocess.call(["ssh", "-n", "-f", serverLogin, "sh -c 'nohup nodejs /tmp/main.js &'"])



# copy script to client and run
clientLogin = args.client_username + "@" + args.client_hostname

copyDestOnClient = clientLogin + ":C:/Users/" + args.client_username + "\Downloads";

subprocess.call(["scp", "-oHostKeyAlgorithms=+ssh-dss", "nodejsClient.js", copyDestOnClient])


cpCmd=r'cp "C:\Program Files\nodejs\node.exe" "C:\Users\"' + args.client_username + "\Downloads"

subprocess.call(["ssh", "-oHostKeyAlgorithms=+ssh-dss","asitester@asitester-pc", cpCmd ])

clientCmd="C:\Users\\" + args.client_username + "\Downloads\\node.exe C:\Users\\" + args.client_username + "\Downloads\\nodejsClient.js " + args.server_hostname

subprocess.call(["ssh", "-oHostKeyAlgorithms=+ssh-dss",clientLogin, clientCmd ])
