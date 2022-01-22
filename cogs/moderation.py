import discord
from discord.ext import commands
import asyncio
command = commands.command


class moderation(commands.Cog):

	def __init__(self, client):
		self.client = client
	
	@commands.command(
		name = "kick",
		aliases = ['кик'],
		brief = "Кикает игрока",
		usage = "кик [пинг игрока] [причина]"
		)
	@commands.has_permissions(view_audit_log=True)
	async def кик(self,ctx,member:discord.Member,reason):
		channel = self.client.get_channel(847089976318754826)
		emb = discord.Embed(title="Кик")
		emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
		emb.add_field(name='Нарушитель',value=member.mention,inline=False)
		if reason == None:
			emb.add_field(name='Причина',value="Не указана",inline=False)
		else:
			emb.add_field(name='Причина',value=reason,inline=False)
		await member.kick()
		await channel.send(embed = emb)
	@commands.command(
		name = "ban",
		aliases = ['бан'],
		brief = "Банит игрока",
		usage = "бан [пинг игрока] [причина]"
		)
	@commands.has_permissions(view_audit_log=True)
	async def бан(self,ctx,member:discord.Member,reason):
		channel = self.client.get_channel(847089976318754826)
		emb = discord.Embed(title="Бан")
		emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
		emb.add_field(name='Нарушитель',value=member.mention,inline=False)
		if reason == None:
			emb.add_field(name='Причина',value="Не указана",inline=False)
		else:
			emb.add_field(name='Причина',value=reason,inline=False)
		await member.ban()
		await channel.send(embed = emb)
	@commands.command(
		name = "clear",
		aliases = ['очистить'],
		brief = "Удаляет сообщения",
		usage = "очистить [кол-во сообщений]"
		)
	@commands.has_permissions(view_audit_log=True)
	async def очистить(self,ctx,amount=10):
		await ctx.message.channel.purge(limit=amount + 1)

	@commands.command(
		name = "report",
		aliases = ['репорт'],
		brief = "Репорт",
		usage = "репорт [текст]"
		)
	async def репорт(self, ctx, *, message: str):
		await ctx.send("Ваше сообщение отправлено модераторам сервера")
		channel = self.client.get_channel(847096864040943647)
		if channel:
			await channel.send("{} репортнул : {}".format(ctx.message.author.mention, message))

	@commands.command(
		name = "Mute",
		aliases = ['мут'],
		brief = "Мутит игрока",
		usage = "мут [пинг игрока] [время в минутах] [причина]"
		)
	@commands.has_permissions(view_audit_log=True)
	async def мут(self, ctx,member:discord.Member,time:int,reason=None):
		role = discord.utils.get(ctx.guild.roles,id=872222214093676584)
		channel = self.client.get_channel(869980383888965653)
		await member.add_roles(role)
		emb = discord.Embed(title="Мут")
		emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
		emb.add_field(name='Нарушитель',value=member.mention,inline=False)
		if reason == None:
			emb.add_field(name='Причина',value="Не указана",inline=False)
		else:
			emb.add_field(name='Причина',value=reason,inline=False)
		emb.add_field(name="Время",value=time,inline=False)
		await channel.send(embed = emb)
		await asyncio.sleep(time*60 )
		emb = discord.Embed(title="Анмут")
		emb.add_field(name='Модератор',value=ctx.author.mention,inline=False)
		emb.add_field(name='Нарушитель',value=member.mention,inline=False)
		emb.add_field(name='Причина',value="Время мута вышло",inline=False)
		await channel.send(embed=emb)
		await member.remove_roles(role)
	@commands.command(
		name = "Размут",
		aliases = ['размут'],
		brief = "Размучивает игрока",
		usage = "размут [пинг игрока]"
		)
	@commands.has_permissions(view_audit_log=True)
	async def размут(self, ctx,member:discord.Member):
		channel = self.client.get_channel(869980383888965653)
		muterole = discord.utils.get(ctx.guild.roles,id=872222214093676584)
		emb = discord.Embed(title="Анмут")
		emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
		emb.add_field(name='Нарушитель',value=member.mention,inline=False)
		await channel.send(embed = emb)
		await member.remove_roles(muterole)

	@commands.command(
		name = "embed",
		brief = "Красивый текст",
		usage = "embed [текст]"
		)
	async def embed(self, ctx, *, text):
		emb = discord.Embed(description=text)
		await ctx.send(embed = emb)

def setup(client):
	client.add_cog(moderation(client))
