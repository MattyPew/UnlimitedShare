from filesplit.split import Split
import os
from cryptography.fernet import Fernet
import shutil
import config
import easygui
import unicodedata

cls = "os.system('cls')"
cwd = os.getcwd()
cwd_temp = cwd+"\\temp"
cwd_temp_copy_original = cwd_temp+"\\copy"
cwd_temp_upload = cwd_temp+"\\upload"
cwd_temp_download = cwd_temp+"\\download"

print("upload_v2.py by MattyPew_ (official extension).")
print()
directory = easygui.fileopenbox(title="Select file to be uploaded")
exec(cls)
shutil.copy(directory, cwd_temp_copy_original)
file_name = os.path.basename(directory)
directory = cwd_temp_copy_original+"\\"+file_name
os.chdir(cwd_temp_copy_original)
not_encrypted_size = os.path.getsize(file_name)
key = Fernet.generate_key()
default_name = file_name+".unshare"
output_file_name = easygui.filesavebox(filetypes=['*.unshare'], default=default_name, title="Save dictionary as")
print(output_file_name)
Us_dictionary_name = output_file_name

exec(cls)
print("File name: "+file_name)
print("Directory: "+directory)
print("Encryption key: "+str(key))
print("Size before encryption: "+str((not_encrypted_size)/1000000)+" MB")
os.chdir(cwd_temp_copy_original)
fernet = Fernet(key)
with open(file_name, 'rb') as file:
    original = file.read()
encrypted = fernet.encrypt(original)
with open(file_name, 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
encrypted_size = os.path.getsize(file_name)
print("Size after encryption: "+str((encrypted_size)/1000000)+" MB")
print()

if input("Continue? (y/n): ").lower() != "y":
    exit()

split = Split(directory, cwd_temp_upload)
split.bysize(config.discord_bytes_limit, False, False, None)

metadata = "head;"+file_name+";"+key.decode("utf-8")+';'+str(not_encrypted_size)+";"+str(encrypted_size)
os.chdir(cwd)                                                                               
with open("output.data", "a") as torent_list:
    torent_list.write(metadata)


exec(cls)


import os 
from os import listdir
from os.path import isfile, join
import discord
from discord.ext import commands
import random
import string
import shutil
import config
cwd = os.getcwd()
cls = "os.system('cls')"
cwd_temp = cwd+"\\temp"
cwd_temp_upload = cwd_temp+"\\upload"
output_file_name = "output.data"
os.chdir(cwd)
#   UPLOAD
guild = config.guild
#   ZÍSKAT SEZNAM SOUBORŮ V "UPLOAD"
files_for_upload = [f for f in listdir(cwd_temp_upload) if isfile(join(cwd_temp_upload, f))]            
#   VYPSAT METADATA DO PRVNÍ ŘÁDKY
os.chdir(cwd)                                                                               


#   STARTNOUT BOTA
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
@bot.event
async def on_ready():
    print("Bot je online")
#   ZÍSKAT ID SERVERU, VYTVOŘIT NOVÝ CHANNEL 
    bot.guild = await bot.fetch_guild(guild)
    random_string = ''.join(random.choice(string.ascii_letters) for i in range(16))
    channel = await bot.guild.create_text_channel(random_string)
    channel_id = channel.id
#   NAHRÁVÁNÍ SOUBORU
    global index
    index = 0
    while True:
        bot.channel = await bot.fetch_channel(channel_id)
        exec(cls)
        print("Nahrávám part: ",index+1,"/",len(files_for_upload))
        upload_file = files_for_upload[index]
        os.chdir(cwd_temp_upload)
        uploaded = await bot.channel.send(file=discord.File(upload_file))
        print("Nahráno")
        id = uploaded.id
        print("Id:", id)
        message = await bot.channel.fetch_message(id)
        print("Odkaz:",message.attachments[0].url)
        url = message.attachments[0].url
#   PŘIDAT LINK DO TORENT LISTU
        os.chdir(cwd)
        with open(output_file_name, "a") as output_file:
            output_file.write("\n"+str(url))
        if index+1 == len(files_for_upload):
            break
        else:
            index = index+1
        print("Done")
    os.chdir(cwd)
    print("Upload extension unloaded!")
    exec(cls)
    print("Closing Upload Handler!")
    os.rename("output.data", Us_dictionary_name)
    exit()
bot.run(config.bot_token)