import subprocess
import argparse


server_password="Asi12345"
client_password="Asi12345"



print "Usage: python SCRIPT server_username server_ip/hostname client_username client_ip/hostname\n"

print "For example: python.exe WindowsToWindowsNodejsTest.py a-yduan am13-02 asitester asitester-pc\n"


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

serverscp = args.server_hostname + "+" + args.server_username + "@" + args.server_hostname
serverssh = args.server_username + "@" + args.server_hostname
clientLogin = args.client_username + "@" + args.client_hostname

# This is a hack since the account I used is a local account.
# In order to use scp on cygwin, I need to use account name: am13-02+a-yduan other than just a-yduan
copyDestOnServer = serverscp + ":C:/Program\ Files/nodejs/"

# Copy server script over and run
subprocess.call(["scp", "-oHostKeyAlgorithms=+ssh-dss", "main.js", copyDestOnServer])

print "Executing scripts on both server and client sides"

psExecServerHost = "\\\\" + args.server_hostname
subprocess.call(["./PsExec.exe","-d", psExecServerHost, "-u", args.server_username, "-p", server_password,
	"c:\Program Files\\nodejs\\node.exe", "c:\Program Files\\nodejs\main.js"])

	

	
# This is another hack :(
# Because of the path problem for C:\Program Files\ in ssh command (surpringly scp works just fine).
# I decide to copy the client side node.exe to ~\Downloads first, and execute it with the script. Dont know why it just works

# Copy client script over and run

clientLogin = args.client_username + "@" + args.client_hostname

copyDestOnClient = clientLogin + ":/tmp"

subprocess.call(["./pscp.exe", "nodejsClient.js", copyDestOnClient])

subprocess.call(["ssh", clientLogin, "nodejs", "/tmp/nodejsClient.js", args.server_hostname])
