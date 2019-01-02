import subprocess

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

def main():
    sendmessage("Have a good day")

main()
