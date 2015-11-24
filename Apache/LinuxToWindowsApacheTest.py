import argparse
import sys
import subprocess

print "Usage: python SCRIPT mode server_username server_ip/hostname client_username client_ip/hostname\n"
print "Mode here can be either mp or sp. mp stands for multi process mode and sp stands for single process mode\n"

print "For example: python LinuxToWindowsApacheTest.py mp/sp yduan am14-09 asitester asitester-pc\n"
print "Please do remember this test case requires apache server being installed on server side. And Node.js being installed on client side\n"

parser = argparse.ArgumentParser()

parser.add_argument("mode", help="configure the apache server as single-process or multi-process mode")

parser.add_argument("server_username", help="the username of the machine on which you would like to deploy the apache server")

parser.add_argument("server_hostname", help="the hostname or ip of the machine on which you would like to deploy the apache server")

parser.add_argument("client_username", help="the username of the machine on which you would like to deploy the client")

parser.add_argument("client_hostname", help="the hostname or ip of the machine on which you would like to deploy the client")

args = parser.parse_args()
print ("server mode is: " + args.mode)
print ("server username is: " + args.server_username)
print ("server hostname/ip is: " + args.server_hostname)
print ("client username is: " + args.client_username)
print ("client hostname/ip is: " + args.client_hostname + "\n\n")


serverLogin = args.server_username + "@" + args.server_hostname
clientLogin = args.client_username + "@" + args.client_hostname

copyDestOnServer = serverLogin + ":/tmp"


print "Copying the configuration files over to the server"

serverCommands=""

if args.mode == "mp":
	serverCommands=" 'sudo ln -s /tmp/mpm_MultiProcess.conf /etc/apache2/mods-enabled/mpm_MultiProcess.conf;sudo ln -s /tmp/mpm_MultiProcess.load /etc/apache2/mods-enabled/mpm_MultiProcess.load;sudo /etc/init.d/apache2 restart'"
	subprocess.call(["./pscp.exe", "mpm_MultiProcess.conf", copyDestOnServer])
	subprocess.call(["./pscp.exe", "mpm_MultiProcess.load", copyDestOnServer])
elif args.mode == "sp":
	serverCommands=" 'sudo ln -s /tmp/mpm_singleProcess.conf /etc/apache2/mods-enabled/mpm_singleProcess.conf;sudo ln -s /tmp/mpm_singleProcess.load /etc/apache2/mods-enabled/mpm_singleProcess.load;sudo /etc/init.d/apache2 restart'"
	subprocess.call(["./pscp.exe", "mpm_singleProcess.conf", copyDestOnServer])
	subprocess.call(["./pscp.exe", "mpm_singleProcess.load", copyDestOnServer])
else:
	print "mode is wrong!"
	sys.exit(0)

print "Configuring apache server"



subprocess.call("ssh -t " + serverLogin + " 'sudo -S rm /etc/apache2/mods-enabled/mpm_*'", shell=True)
subprocess.call("ssh -t " + serverLogin + serverCommands, shell=True)


#serverCommands="chmod a+x /tmp/serverDeployment.sh;sudo -S rm /etc/apache2/mods-enabled/mpm_*"

#ssh = subprocess.Popen(["ssh", "%s" % serverLogin, serverCommands],
#                       shell=True,
#                       stdout=subprocess.PIPE,
#                       stderr=subprocess.PIPE)
#result = ssh.stdout.readlines()
#if result == []: 
#    error = ssh.stderr.readlines()
#    print >>sys.stderr, "ERROR: %s" % error
#else:
#    print result


print "Deploy client script and exetute"


copyDestOnClient = clientLogin + ":C:/Users/" + args.client_username + "\Downloads";

subprocess.call(["scp", "-oHostKeyAlgorithms=+ssh-dss", "apacheClient.js", copyDestOnClient])

cpCmd=r'cp "C:\Program Files\nodejs\node.exe" "C:\Users\"' + args.client_username + "\Downloads"

subprocess.call(["ssh", "-oHostKeyAlgorithms=+ssh-dss","asitester@asitester-pc", cpCmd ])

clientCmd="C:\Users\\" + args.client_username + "\Downloads\\node.exe C:\Users\\" + args.client_username + "\Downloads\\apacheClient.js " + args.server_hostname

subprocess.call(["ssh", "-oHostKeyAlgorithms=+ssh-dss",clientLogin, clientCmd ])