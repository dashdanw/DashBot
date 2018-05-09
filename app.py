# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import re
from rr import RussianRoulette

TOKEN = 'NDQzNjM4ODUyNDE0ODY1NDE5.DdQVgA.Gw0lk69aKjCLmn85K8JVXegL_Lk'

client = discord.Client()
delimiter = '$'
rr = None

@client.event
async def on_message(message):
    d, params = message.content[0], message.content[1:]
    #do not respond to stupid SHIT
    if d != delimiter:
        return
    # we do not want the bot to reply to itself
    elif message.author == client.user:
        return

    action, *params = re.split(r'\s+', params)

    if action == 'rr':
        global rr
        if params[0] == 'start':
            if rr is None:
                rr = RussianRoulette()
                await client.send_message(
                    message.channel,
                    f'Russian Roulette has started! type `{delimiter}rr trigger` to take a shot pussy.'
                )
            else:
                await client.send_message(
                    message.channel,
                    f'Russian Roulette is already running! type `{delimiter}rr trigger` to take a shot,'
                    f'or `{delimiter}rr end` to delete the current game'
                )
        elif params[0] == 'end':
            if rr is None:
                await client.send_message(
                    message.channel,
                    f'Russian Roulette isn\'t running! type `{delimiter}rr start` to make a new game.'
                )
            else:
                rr = None
                await client.send_message(
                    message.channel,
                    f'Russian Roulette game deleted! type `{delimiter}rr start` to make a new game.'
                )
        elif params[0] == 'restart':
            rr = RussianRoulette()
            await client.send_message(
                message.channel,
                f'Russian Roulette has started! type `{delimiter}rr trigger` to take a shot pussy.'
            )
        elif params[0] == 'trigger':
            if rr is None or not isinstance(rr, RussianRoulette):
                await client.send_message(
                    message.channel,
                    f'Russian Roulette is not running! type `{delimiter}rr start` to make a new game!'
                )
            else:
                is_bullet = rr.trigger()
                if is_bullet:
                    rr = None
                    await client.send_message(
                        message.channel,
                        f'BANG!'
                    )
                    await client.kick(
                        message.author
                    )
                else:
                    await client.send_message(
                        message.channel,
                        f'CLICK!'
                    )



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
