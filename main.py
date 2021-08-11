import discord
import os
from discord.ext import commands


def main():
    prefix = '!'
    intents = discord.Intents.all()

    client = commands.Bot(command_prefix=prefix, intents=intents)

    @client.command(name = 'ping')
    async def _ping(ctx):
        await ctx.send("pong")
    
    @client.command(name = '이름')
    async def _ping(ctx):
        await ctx.send("명령어를 입력하신 분의 이름은 "+ ctx.author.name+"이네요!")



    with open('token.txt', 'r') as f:
        token = f.read()

    client.run(token)




if __name__ == '__main__':
    main()
