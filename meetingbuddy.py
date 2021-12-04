from rich import print, prompt, console, pretty, progress
from random import shuffle
from time import sleep


"""Utility to automatically and randomly select the next person to speak in a
meeting and alot a time based on meeting length"""


print("[green]Enter List of Attendees[/green]")
print("[green]Example input (seperated by spaces):[/green]")
print("[red]bob julian l1dge[/red]")

data = input("> ")

attendees = data.split()

print("[green]Enter length of meeting in minutes[/green]")
print("[green]Example for meeting of 2hours:[/green]")
print("[red]120[/red]")

timing = int(input("> "))

slot = round(timing / (len(attendees)+1))

shuffle(attendees)
for upnext in attendees:
    print(f"[blue]Up Next:[/blue] [red] {upnext}[/red] {slot}")
    for step in progress.track(range((slot*60))):
        sleep(1)
        step

        print("[blue]Are we ready for the next speaker?[/blue]")
        prompt.Prompt.ask("Press Enter to continue......")

#Next Speaker
def NextSpeaker():
    pass


#Countdown Display
def DisplayCountdown():
    pass


#End of speakers
def MeetingEnd():
    pass

