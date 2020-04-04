import discord
import random
import json
import os

from discord.ext import commands
client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Discord Macro | -help'))
    print('LvlUpBot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'I am feeling bad. {round(client.latency) * 1000} ms.')

os.chdir(r'D:\BOT')

@client.event
async def on_member_join(member):
    with open('money.json', 'r') as f:
        users = json.load(f)


    await update_data(users, member)


    with open('money.json', 'w') as f:
        json.dump(users, f)



@client.event
async def on_message(message):
    if message.author.bot == False:
        with open('money.json', 'r') as f:
            users = json.load(f)


        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message)


        with open('money.json', 'w') as f:
            json.dump(users, f)


async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1
        users[f'{user.id}']['name'] = f'{user.name}'


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp

async def level_up(users, user, message):
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1/4))
    if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
        users[f'{user.id}']['level'] = lvl_end


client.run('Njk1NzIxMTUwMDI1NTY0Mjgw.XoeS3A.WXO8wzczIydFRXe6HebYGVpcsU8')
