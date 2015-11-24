import subprocess
import argparse
subprocess.call("date")

print "Usage: python SCRIPT server_username server_ip/hostname client_username client_ip/hostname\n"

print "For example: python LinuxToLinuxNodejsTest.py yduan am14-09 yduan am14-09-vm\n"


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
clientLogin = args.client_username + "@" + args.client_hostname

copyDestOnServer = serverLogin + ":/tmp"

subprocess.call(["./pscp.exe", "main.js", copyDestOnServer])

copyDestOnClient = clientLogin + ":/tmp"

subprocess.call(["./pscp.exe", "nodejsClient.js", copyDestOnClient])

print "Executing scripts on both server and client sides"

subprocess.call(["ssh", "-n", "-f", serverLogin, "sh -c 'nohup nodejs /tmp/main.js &'"])

subprocess.call(["ssh", clientLogin, "nodejs", "/tmp/nodejsClient.js", args.server_hostname])
