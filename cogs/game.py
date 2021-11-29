import discord
from discord.ext import commands


class game(commands.Cog):

	def __init__(self, client):
		self.client = client
	@commands.command(
		aliases = ["нюхать", "Нюхать"]
	)
	async def bebra(self, ctx, text):
		if text == 'бебру':

			await ctx.send(f"{ctx.author.mention} понюхал бебру!")
		else:
			await ctx.send("Что вы хотели понюхать?")

def setup(client):
	client.add_cog(game(client))