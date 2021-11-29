import discord
from discord.ext import commands
from discord_components import *
from simpledemotivators import Demotivator
import os



class demotivator(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def demotivator(self, ctx):
		def check(message):
			return message.author.id == ctx.author.id
		await ctx.send('Сколько строк в демотиваторе делать?', components=[
			Button(style=ButtonStyle.green, label='Две'),
			Button(style=ButtonStyle.red, label='Одну')])
		mode = await self.client.wait_for('button_click', check=check)
		await ctx.send(content='Напиши первую строку демотиватора')
		one = await self.client.wait_for('message', check=check)
		if mode.component.label == 'Две':
			await ctx.send('Напиши вторую строку демотиватора')
			two = await self.client.wait_for('message', check=check)
		await ctx.send('Пришли картинку для демотиватора')
		picture = await self.client.wait_for('message', check=check)
		if mode.component.label == 'Две':
			dem = Demotivator(one.content, two.content)
		if mode.component.label == 'Одну':
			dem = Demotivator(one.content)
		for attach in picture.attachments:
			await attach.save('picture.jpg')
		await ctx.send('Делать вотермарку?', components=[
			Button(style=ButtonStyle.green, label='Нет'),
			Button(style=ButtonStyle.red, label='Да')])
		water_logic = await self.client.wait_for('button_click', check=check)
		if water_logic.component.label == 'Да':
			await ctx.send('Пришли текст для вотермарки')
			water_text = await self.client.wait_for('message', check=check)
			dem.create('picture.jpg', colorfill='black', fonttext='times.ttf', line=water_text.content)
		if water_logic.component.label == 'Нет':
			dem.create('picture.jpg', colorfill='black', fonttext='times.ttf')
		await ctx.send(file=discord.File('demresult.jpg'))
		os.remove('demresult.jpg')


def setup(client):
	client.add_cog(demotivator(client))