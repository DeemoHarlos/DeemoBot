'''
加上@bot.command()裝飾器正常運作的話可以回傳圖表，其中產生圖表的function來自plot_test2
'''
from weather import plot_test_2
import discord
from discord.ext.commands import Context as Ctx
from os import remove as rm
# @bot.command()


async def plot(ctx: Ctx):
    try:
        await plot_test_2.get_plot()
        with open('plot.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
            rm('plot.png')
    except:
        await ctx.send("failed")
