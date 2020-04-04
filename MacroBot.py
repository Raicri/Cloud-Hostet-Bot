import discord
import random
import json
import os

from discord.ext import commands
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Discord Macro | .help'))
    print('Bot is online.')

@client.command()
async def ping(ctx):
    await ctx.send(f'I am not lagging!!! {round(client.latency) * 1000} ms.')

@client.command(aliases=['8ball','eightball'])
async def _8ball(ctx, *, question):
    responses = ['Probably',
    'I would not be so sure about that.',
    'My answer is no.',
    'Probably not',
    'Of course!',
    'Why not?',
    'My answer is yes.',
    'This is true, and it will stay like that.',
    'Not even in a million years.',
    'I mean, I do not see the point in saying no.',
    'Why this question? The answer is a definitive no.',
    'As my grandma used to say... no.',
    'As my great great grandfather used to say... what even is this question?',
    'I do not know.',
    'Sources say no.',
    'I do not know, but if there is something I know is that Marcelo is beautifull']

    await ctx.send(f'Question: {question}\nAnswer: {random.choices(responses)}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(manage_roles=True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason=reason)
    await ctx.send(f'{user.mention} was kicked.')

@client.command()
@commands.has_permissions(manage_roles=True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason=reason)
    await ctx.send(f'{user.mention} was banned.')

@client.command()
@commands.has_permissions(manage_roles=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} was unbanned.')
            return

client.run('Njk1NjgxNjU1ODQyNjY4NjI0.XodvyQ.xloRl5K79NS2hYzfoANC3N5Bmt4')
