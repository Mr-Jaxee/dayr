import discord
from discord.ext import commands
from discord_components import *
from pymongo import MongoClient
import os

client = commands.Bot(command_prefix = "!", intents = discord.Intents(messages = True, guild_messages = True, members = True, guilds = True))
cluster = MongoClient("mongodb+srv://Jaxee:zB3DV6wTS24m6MH@cluster0.2pfpp.mongodb.net/dayr?retryWrites=true&w=majority")
collection = cluster.dayr.dayrcoll


@client.event
async def on_ready():
	print("Bot connected to the server")
	DiscordComponents(client)
	while True:
		  await client.change_presence( status=discord.Status.online, activity=discord.Game( "Day R Premium" ) )
	
	for guild in client.guilds:
		for member in guild.members:
			post = {
				"_id": member.id,
				"balance": 0,
				"xp": 0,
				"lvl": 1
			}

			if collection.count_documents({"_id": member.id}) == 0:
				collection.insert_one(post)


@client.event
async def on_member_join(member):
	post = {
		"_id": member.id,
		"balance": 0,
		"xp": 0,
		"lvl": 1
	}

	if collection.count_documents({"_id": member.id}) == 0:
		collection.insert_one(post)


@client.event
async def on_command_error(ctx, error):
	print(error)	

	if isinstance(error, commands.UserInputError):
		await ctx.send(embed = discord.Embed(
			description = f"Правильное использование команды: `{ctx.prefix}{ctx.command.name}` ({ctx.command.brief}): `{ctx.prefix}{ctx.command.usage}`"
		))
		
@client.command()
async def load(ctx, extension):
	client.load_extension(f"cogs.{extension}")
	await ctx.send("cogs is load...")

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")
	await ctx.send("cogs is unload...")

@client.command()
async def reload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")
	client.load_extension(f"cogs.{extension}")
	await ctx.send("cogs is reload...")


for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")


client.run("ODY5MTMzODk0ODQ5NTMxOTM0.YP5yBA.tjRgIt2LTKX5s4PSl4iFX6GImEc")
