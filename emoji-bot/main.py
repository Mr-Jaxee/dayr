import discord 
from discord.ext import commands
import time
import os


intents = discord.Intents.default()
intents.members = True


client = commands.Bot( command_prefix = '!', intents = intents )

@client.event
async def on_ready():
	print( 'Ready!' )
	print( 'Logged in as ---->', client.user )
	print( 'ID:', client.user.id )
	while True:
		  await client.change_presence( status=discord.Status.online, activity=discord.Game( "Day R Premium" ) )

@client.event
async def on_raw_reaction_add(payload):
	channel = client.get_channel(payload.channel_id)
	message = await channel.fetch_message(payload.message_id)
	guild = client.get_guild(payload.guild_id)
	reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)

	# only work if it is the client
	if payload.member.id == client.user.id:
		return

	if payload.message_id == 869178139274788894 and reaction.emoji == '🌿':
		role = discord.utils.get(guild.roles, name='Травник')
		await payload.member.add_roles(role)
		
	if payload.message_id == 869178139274788894 and reaction.emoji == '😑':
		role = discord.utils.get(guild.roles, name='Крафтер')
		await payload.member.add_roles(role)
		
	if payload.message_id == 869178139274788894 and reaction.emoji == '🌲':
		emoji = '✅'
		role = discord.utils.get(guild.roles, name='Лесоруб')
		await payload.member.add_roles(role)

	if payload.message_id == 869178139274788894 and reaction.emoji == '💧':
		role = discord.utils.get(guild.roles, name='Водо-качка')
		await payload.member.add_roles(role)
		
	if payload.message_id == 869178139274788894 and reaction.emoji == '😇':
		role = discord.utils.get(guild.roles, name='Торговец')
		await payload.member.add_roles(role)
		
	if payload.message_id == 869178139274788894 and reaction.emoji == '🛵':
		role = discord.utils.get(guild.roles, name='Курьер')
		await payload.member.add_roles(role)

	if payload.message_id == 869178139274788894 and reaction.emoji == '💀':
		role = discord.utils.get(guild.roles, name='Охотник')
		await payload.member.add_roles(role)

	if payload.message_id == 869178139274788894 and reaction.emoji == '⛑':
		role = discord.utils.get(guild.roles, name='Перегонщик')
		await payload.member.add_roles(role)

	if payload.message_id == 869200867121848321 and reaction.emoji == '📙':
		role = discord.utils.get(guild.roles, name='Премиум')
		await payload.member.add_roles(role)

	if payload.message_id == 869200867121848321 and reaction.emoji == '📘':
		role = discord.utils.get(guild.roles, name='Не премиум')
		await payload.member.add_roles(role)

	if payload.message_id == 869499032999952474 and reaction.emoji == '🚛':
		role = discord.utils.get(guild.roles, name='Белочник')
		await payload.member.add_roles(role)

	if payload.message_id == 900367882179973140 and reaction.emoji == '💵':
		role = discord.utils.get(guild.roles, name='Гость-торговец')
		await payload.member.edit(roles=[])
		await payload.member.add_roles(role)
		
client.run("ODY5MTMzODk0ODQ5NTMxOTM0.YP5yBA.tjRgIt2LTKX5s4PSl4iFX6GImEc")

'''
0-5 дух
6-10 рядовой
11-15 выживальщик
16-20 умелый 
21-25 опытный 
26-30 про
31-35 невозможно крут
36-40 монстр
41-45 демон
46-50 сатана во плоти
51-55 обнуление
56-60 щенок 
61-65 псина сутулая
66-70 волчара
71-75 украінска розвідка
76-80 кабанчик
81-85 человек с отсутствием личной жизни
86-90 личная жизнь в игре
91-95 игра это жизнь
96-100 дикое уважение от Grizzli
'''