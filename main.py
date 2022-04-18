import discord
import os
import random
from replit import db
import csv


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-commands'):
        await message.channel.send('tae ka')
        return

    writeCsv()
    convertToPng()
    await sendImage(message)
    await message.channel.send(randomFormat(message.content))
      

def randomFormat(c):
  word = '';
  for element in range(0, len(c)):
    word += randomupper(c[element]);
  return word

def randomupper(c):
    if random.random() > 0.5:
        return c.upper()
    return c.lower()



def convertToPng():
  #test
  return


async def sendImage(message):
  my_files = [
    discord.File('csv.csv'),
    discord.File('image.png')
  ]
  await message.channel.send(files=my_files)



  
def writeCsv():
  return
  # with open('employee_file.csv', mode='w') as employee_file:
  #   employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  #   employee_writer.writerow(['John Smith', 'Accounting', 'November'])
  #   employee_writer.writerow(['Erica Meyers', 'IT', 'March'])



client.run(os.getenv('TOKEN'))