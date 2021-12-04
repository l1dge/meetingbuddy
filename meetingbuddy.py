from rich import print, inspect, console, pretty, progress
import argparse
from random import shuffle


"""Utility to automatically and randomly select the next person to speak in a
meeting and alot a time based on meeting length"""


#Argparser
#parser = argparse.ArgumentParser(description='Selects next speaker')

#parser.add_argument('attendees', metavar='attendees', type=list, help='Enter list of attendees')
#parser.add_argument('meetinglength', metavar='meetinglength', type=int, help='Enter length of meeting slot in minutes')

#args = parser.parse_args()

#attendees = args.attendees
#meetinglength = args.meetinglength


#UserInput
print("[green]Enter List of Attendees[/green]")
print("[green]Example input (seperated by spaces):[/green]")
print("[red]bob julian l1dge[/red]")

data = input("> ")

attendees = data.split()

print("[green]Enter length of meeting in minutes[/green]")
print("[green]Example for meeting of 2hours:[/green]")
print("[red]120[/red]")

timing = int(input("> "))


#Meeting Attendees
def Attendees(who):
    shuffle(who)
    for upnext in who:
        print(f"[blue]Up Next:[/blue] [red] {upnext}[/red]")


#Speaker Timer
def SlotTimer(mLength):
    slot = mLength /  len(attendees)
    print(slot)

#Next Speaker
def NextSpeaker():
    pass


#Countdown Display
def DisplayCountdown():
    pass


#End of speakers
def MeetingEnd():
    pass


Attendees(attendees)
SlotTimer(timing)
