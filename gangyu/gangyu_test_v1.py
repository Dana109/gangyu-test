import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import asyncio
import time

from gangyu_const import *



Client = discord.Client()
client = commands.Bot(command_prefix = ">")

server_whitelist = [gu_server_id]


#START UP EVENTS
@client.event
async def on_ready():
    print("Bot is ready.")

#assigns new users with the 'solitaries' role
@client.event
async def on_member_join(member):
	role = discord.utils.get(member.server.roles, name='Solitaries')
	await client.add_roles(member, role)


#COMMANDS
#revise in code clean up later

#pat pat
@client.command()
async def pats():
    await client.say('*Gangyu Bot pats you back*')

#Join Gang
@client.command(pass_context=True)
async def join(cmd):
    member = cmd.message.author
    server= cmd.message.server
    msg = cmd.message
    role_msg = cmd.message.content.lower()
    role_msg = role_msg.split(' ', 1)[1]
    role_msg = role_msg.capitalize()

    print(cmd)

    old_role=discord.utils.get(server.roles, id = sol_role_id)
    new_role=discord.utils.get(server.roles, name= role_msg)

    if old_role in member.roles:
        if new_role in server.roles:
            await client.say("You have joined {}".format(new_role))
            await client.replace_roles(member, new_role)
        else:
            await client.say('Gang does not exist.')
    else:
        await client.say("You're already part of a gang you filthy traitor.")



client.run(TOKEN)