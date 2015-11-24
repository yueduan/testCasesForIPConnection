import subprocess


#subprocess.call(["./PsExec.exe","-d", "\\\\am13-02", "-u", "a-yduan", "-p", "Asi12345"
#	"c:\Program Files\\nodejs\\node.exe", "c:\Program Files\\nodejs\main.js"])

#subprocess.call(["./PsExec.exe", "\\\\asitester-pc", "-u", "asitester", "-p", "Asi12345",
#	"c:\Program Files\\nodejs\\node.exe"])
	
#, "c:\Program Files\\nodejs\nodejsClient.js", "am13-02"])


#dir=r"C:\Program"+ ' ' + "Files\\nodejs"
	
	
#client_username = "asitester"

cpCmd=r'cp "C:\Program Files\nodejs\node.exe" "C:\Users\"' + "asitester" + "\Downloads"

print cpCmd

#subprocess.call(["ssh", "-oHostKeyAlgorithms=+ssh-dss","asitester@asitester-pc", cpCmd ])

#, "/tmp/nodejsClient.js", "am13-02"])
#
