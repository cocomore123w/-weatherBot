import discord
from discord.ext import commands
#####
import reply
import Lib
#####
#
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    game = discord.Game('今日も小さい～')

    ######
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    ##
    ##
    await bot.change_presence(activity=game)

##################################
@bot.event
async def on_message(message):
    ##

    #print(message.content)
    #
    if message.content[0] != "!":
        return
    ##
    if message.author == bot.user:
        return
    ##
    user = message.author
    userCtx = message.content.split("!")[1]
    #print(user)
    #print((userCtx))
    ## 辭庫
    if message.content != "":
        await message.channel.send(reply._replyAns(user,userCtx))


bot.run(Lib.token)
