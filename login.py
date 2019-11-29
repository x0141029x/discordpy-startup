# coding: utf-8
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


@bot.command(name="ミミッキュ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")


@bot.command(name="さようなら")
async def goodbye(ctx):
    await ctx.send(f"じゃあね、{ctx.message.author.name}さん！")


bot.run('NjQ5NjQwMDE4NjY2ODQ4Mjcx.XeEfIA.GZxuyoYKxLwky_CmCF77CRVUpwg')
