import requests
import discord

TOKEN = 'BOT TOKEN'

client = discord.Bot()
@client.slash_command(name="gyazo")
async def convert_to_gyazo(ctx,file: discord.Attachment):
    ppap=str(file)
    file_name = "ppap"
    responser = requests.get(ppap)
    image = responser.content
    with open(file_name, "wb") as aaa:
        aaa.write(image)
    await ctx.respond("uploading...")
    URL="https://upload.gyazo.com/api/upload"
    headers = {'Authorization': "Bearer {}".format('GSiLKFRuu-2LR8iybvM2yNycBEqgwrhzw4tPB-bv1lk')}
    with open(file_name,"rb") as f:
        files = {'imagedata':f.read()}
        response = requests.request('post', URL, headers=headers, files=files)
        await ctx.respond(response.text[response.text.find('"url":"'):response.text.find('","access_policy":null}')])
client.run(TOKEN)
