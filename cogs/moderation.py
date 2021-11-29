import discord
from discord.ext import commands
import asyncio
command = commands.command


class moderation(commands.Cog):

	def __init__(self, client):
		self.client = client
	
	@command()
	@commands.has_permissions(view_audit_log=True)
	async def кик(self,ctx,member:discord.Member,reason):
		channel = self.client.get_channel(847089976318754826)
		emb = discord.Embed(title="Кик")
		emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
		emb.add_field(name='Нарушитель',value=member.mention,inline=False)
		emb.add_field(name='Причина',value=reason,inline=False)
		await member.kick()
		await channel.send(embed = emb)
	@command()
	@commands.has_permissions(view_audit_log=True)
	async def бан(self,ctx,member:discord.Member,reason):
		channel = self.client.get_channel(847089976318754826)
		emb = discord.Embed(title="Бан")
		emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
		emb.add_field(name='Нарушитель',value=member.mention,inline=False)
		emb.add_field(name='Причина',value=reason,inline=False)
		await member.ban()
		await channel.send(embed = emb)
	@command()
	@commands.has_permissions(view_audit_log=True)
	async def очистить(self,ctx,amount=10):
		await ctx.message.channel.purge(limit=amount + 1)

	@command()
	async def репорт(self, ctx, *, message: str):
		await ctx.send("Ваше сообщение отправлено модераторам сервера")
		channel = self.client.get_channel(847096864040943647)
		if channel:
			await channel.send("{} репортнул : {}".format(ctx.message.author.mention, message))

	@command()
	@commands.has_permissions(view_audit_log=True)
	async def мут(self, ctx,member:discord.Member,time:int,reason):
		role = discord.utils.get(ctx.guild.roles,id=872222214093676584)
		channel = self.client.get_channel(869980383888965653)
		await member.add_roles(role)
		emb = discord.Embed(title="Мут",color=0x2f3136)
		emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
		emb.add_field(name='Нарушитель',value=member.mention,inline=False)
		emb.add_field(name='Причина',value=reason,inline=False)
		emb.add_field(name="Время",value=time,inline=False)
		await channel.send(embed = emb)
		await asyncio.sleep(time*60 )
		emb = discord.Embed(title="Анмут",color=0x2f3136)
		emb.add_field(name='Модератор',value='<@709725675711496233>',inline=False)
		emb.add_field(name='Нарушитель',value=member.mention,inline=False)
		emb.add_field(name='Причина',value="Время мута вышло",inline=False)
		await channel.send(embed=emb)
		await member.remove_roles(role)
	@command()
	@commands.has_permissions(view_audit_log=True)
	async def размут(self, ctx,member:discord.Member):
		channel = self.client.get_channel(869980383888965653)
		muterole = discord.utils.get(ctx.guild.roles,id=872222214093676584)
		emb = discord.Embed(title="Анмут",color=0xff0000)
		emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
		emb.add_field(name='Нарушитель',value=member.mention,inline=False)
		await channel.send(embed = emb)
		await member.remove_roles(muterole)

	@command()
	async def embed(self, ctx, *, text):
		emb = discord.Embed(description=text)
		await ctx.send(embed = emb)

	@command()
	@commands.has_permissions(view_audit_log=True)
	async def варн(self, ctx,member:discord.Member, reason):
		channel = self.client.get_channel(869980383888965653)
		muterole = discord.utils.get(ctx.guild.roles,id=893132629107433533)
		emb = discord.Embed(title="Предупреждение")
		emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
		emb.add_field(name='Нарушитель',value=member.mention,inline=False)
		emb.add_field(name='Причина',value=reason,inline=False)
		await channel.send(embed = emb)
		await member.add_roles(muterole)

	@command()
	@commands.has_permissions(view_audit_log=True)
	async def варн2(self, ctx,member:discord.Member, reason):
		channel = self.client.get_channel(869980383888965653)
		muterole = discord.utils.get(ctx.guild.roles,id=893132766978408468)
		emb = discord.Embed(title="Предупреждение")
		emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
		emb.add_field(name='Нарушитель',value=member.mention,inline=False)
		emb.add_field(name='Причина',value=reason,inline=False)
		await channel.send(embed = emb)
		await member.add_roles(muterole)

def setup(client):
	client.add_cog(moderation(client))
