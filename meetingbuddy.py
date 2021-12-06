from rich import print, prompt, console, pretty, progress
from random import shuffle
from time import sleep


print("[green]Enter List of Attendees[/green]")
print("[green]Example input (seperated by spaces):[/green]")
print("[red]bob julian l1dge[/red]")

data = input("> ")

attendees = data.split()

print("[green]Enter length of meeting in minutes (must be 10 or greater)[/green]")
print("[green]Example for meeting of 2 hours:[/green]")
print("[red]120[/red]")

timing = int(input("> "))

slot = round(timing / (len(attendees)+1))



shuffle(attendees)
for upnext in attendees:
    print("")
    print("[blue]Are we ready for the next speaker?[/blue]")
    prompt.Prompt.ask("[red]Press Enter to continue......[/red]")
    print("")
    print(f"[blue]Up Next:[/blue] [red] {upnext}[/red] {slot}")
    for step in progress.track(range((slot*60))):
        sleep(1)
        step

print("")
print("[blue]Are we ready for the next speaker?[/blue]")
print(f"[blue]Handing back to the Chair[/blue]")
prompt.Prompt.ask("[red]Press Enter to continue......[/red]")
print("")

for step in progress.track(range((slot*60))):
    sleep(1)
    step


