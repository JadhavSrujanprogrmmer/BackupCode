import sys,time,os

message = "A story is the telling of an event, either true or fictional, in such a way that the listener experiences or learns something just by the fact that he heard the story. A story is a means of transferring information, experience, attitude or point of view.\n Every story has a teller and a listener"

def typwrite(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

os.system("cls")
typwrite(message)