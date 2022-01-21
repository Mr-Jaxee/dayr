import discord
from discord.ext import commands
from pymongo import MongoClient
import random

"""
1. balance -> вывод баланса пользователя
2. pay -> перевод денег
3. LVL-System
"""

class Economic(commands.Cog):

	def __init__(self, client):
		self.client = client
		self.cluster = MongoClient("mongodb+srv://Jaxee:zB3DV6wTS24m6MH@cluster0.2pfpp.mongodb.net/dayr?retryWrites=true&w=majority")
		self.collection = self.cluster.dayr.dayrcoll

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self.client.user:
			return

		user = message.author
		data = self.collection.find_one({"_id": user.id})

		if data == None:
			post = {
			"_id": user.id,
			"balance": 0,
			"xp": 0,
			"lvl": 1
			}

			if self.collection.count_documents({"_id": user.id}) == 0:
				self.collection.insert_one(post)
		else:
			if data["xp"] == 500 + 100 * data["lvl"]:
				self.collection.update_one({"_id": user.id},
					{"$set": {"lvl": data["lvl"] + 1}})
				self.collection.update_one({"_id": user.id},
					{"$set": {"xp": 0}})

				await message.channel.send(f"{user.mention} + 1 lvl")

				if self.collection.find_one({'_id': 	message.author.id})['lvl'] == 1:
					role = message.author.guild.get_role(869500876673417257)
					await message.author.add_roles(role)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 6:
					role = message.author.guild.get_role(869501078364905482)
					role1 = message.author.guild.get_role(869500876673417257)
					await message.author.remove_roles(role1)
					await message.author.add_roles(role)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 11:
					role = message.author.guild.get_role(869501333814792203)
					role1 = message.author.guild.get_role(869501078364905482)
					await message.author.add_roles(role)
					await message.author.remove_roles(role1)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 16:
					role = message.author.guild.get_role(869501441461612544)
					role1 = message.author.guild.get_role(869501333814792203)
					await message.author.add_roles(role)
					await message.author.remove_roles(role1)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 21:
					role = message.author.guild.get_role(869501436986290176)
					role1 = message.author.guild.get_role(869501441461612544)
					await message.author.add_roles(role)
					await message.author.remove_roles(role1)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 26:
					role = message.author.guild.get_role(869501613696483338)
					role1 = message.author.guild.get_role(869501436986290176)
					await message.author.add_roles(role)
					await message.author.remove_roles(role1)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 31:
					role = message.author.guild.get_role(869501701055471666)
					role1 = message.author.guild.get_role(8869501613696483338)
					await message.author.add_roles(role)
					await message.author.remove_roles(role1)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 36:
					role = message.author.guild.get_role(869501701055471666)
					role1 = message.author.guild.get_role(869501701055471666)
					await message.author.add_roles(role)
					await message.author.remove_roles(role1)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 41:
					role = message.author.guild.get_role(869535656655876136)
					role1 = message.author.guild.get_role(869501701055471666)
					await message.author.add_roles(role)
					await message.author.remove_roles(role1)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 46:
					role = message.author.guild.get_role(869536685157933056)
					role1 = message.author.guild.get_role(869535656655876136)
					await message.author.add_roles(role)
					await message.author.remove_roles(role1)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 51:
					role = message.author.guild.get_role(869546579986640936)
					role1 = message.author.guild.get_role(869536685157933056)
					await message.author.add_roles(role)
					await message.author.remove_roles(role1)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 56:
					role = message.author.guild.get_role(869546780788924426)
					role1 = message.author.guild.get_role(869546579986640936)
					await message.author.add_roles(role)
					await message.author.remove_roles(role1)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 61:
					role = message.author.guild.get_role(869547648632360990)
					role1 = message.author.guild.get_role(869546780788924426)
					await message.author.add_roles(role)
					await message.author.remove_roles(role1)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 66:
					role = message.author.guild.get_role(869547779561750538)
					role1 = message.author.guild.get_role(869547648632360990)
					await message.author.add_roles(role)
					await message.author.remove_roles(role1)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 71:
					role = message.author.guild.get_role(869547966933905448)
					role1 = message.author.guild.get_role(869547779561750538)
					await message.author.add_roles(role)
					await message.author.remove_roles(role1)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 76:
					role = message.author.guild.get_role(869548409357479986)
					role1 = message.author.guild.get_role(869547966933905448)
					await message.author.add_roles(role)
					await message.author.remove_roles(role1)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 81:
					role = message.author.guild.get_role(869548411903438868)
					role1 = message.author.guild.get_role(869548409357479986)
					await message.author.add_roles(role)
					await message.author.remove_roles(role1)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 86:
					role = message.author.guild.get_role(869548701826302012)
					role1 = message.author.guild.get_role(869548411903438868)
					await message.author.add_roles(role)
					await message.author.remove_roles(role1)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 91:
					role = message.author.guild.get_role(869548705232080926)
					role1 = message.author.guild.get_role(869548701826302012)
					await message.author.add_roles(role)
					await message.author.remove_roles(role1)

				if self.collection.find_one({'_id': message.author.id})['lvl'] == 96:
					role = message.author.guild.get_role(869548707945795584)
					role1 = message.author.guild.get_role(869548705232080926)
					await message.author.add_roles(role)
					await message.author.remove_roles(role1)
			else:
				self.collection.update_one({"_id": user.id},
					{"$set": {"xp": data["xp"] + 25}})


	@commands.command(
		name = "баланс",
		aliases = ["balance", "cash"],
		brief = "Вывод баланса пользователя",
		usage = "balance <@user>"
	)
	async def user_balance(self, ctx, member: discord.Member = None):
		if member is None:
			await ctx.send(embed = discord.Embed(
				description = f"Баланс пользователя __{ctx.author}__: **{self.collection.find_one({'_id': ctx.author.id})['balance']}**"
			))
		else:
			await ctx.send(embed = discord.Embed(
				description = f"Баланс пользователя __{member}__: **{self.collection.find_one({'_id': member.id})['balance']}**"
			))

	@commands.command(
		name = "уровень",
		aliases = ["lvl"],
		brief = "Вывод уровня пользователя",
		usage = "lvl <@user>"
	)
	async def user_lvl(self, ctx, member: discord.Member = None):
		if member is None:
			await ctx.send(embed = discord.Embed(
				description = f"Уровень пользователя __{ctx.author}__: **{self.collection.find_one({'_id': ctx.author.id})['lvl']}**, **{self.collection.find_one({'_id': ctx.author.id})['xp']}**"
			))
		else:
			await ctx.send(embed = discord.Embed(
				description = f"Уровень пользователя __{member}__: **{self.collection.find_one({'_id': member.id})['lvl']}**, **{self.collection.find_one({'_id': member.id})['xp']}**"
			))


	@commands.command(
		name = "перевод",
		aliases = ["pay", "givecash"],
		brief = "Перевод денег другому пользователю",
		usage = "pay <@user> <amount>"	
	)
	async def pay_cash(self, ctx, member: discord.Member, amount: int):
		ubalance = self.collection.find_one({"_id": ctx.author.id})["balance"]
		mbalance = self.collection.find_one({"_id": member.id})["balance"]

		if amount <= 0:
			await ctx.send(embed = discord.Embed(
				description = f"__{ctx.author}__, конечно извините меня, но проход хацкерам сегодня закрыт."
			))
		else:
			self.collection.update_one({"_id": ctx.author.id},
				{"$set": {"balance": ubalance - amount}})

			self.collection.update_one({"_id": member.id},
				{"$set": {"balance": mbalance + amount}})

			await ctx.message.add_reaction("✅")

	@commands.command(
		name = "пополнить",
		aliases = ["donate"],
		brief = "Пополнить гризкоины",
		usage = "donate <@user> <amount>"	
	)
	@commands.has_permissions(view_audit_log=True)
	async def donate_cash(self, ctx, member: discord.Member, amount: int):
		mbalance = self.collection.find_one({"_id": member.id})["balance"]

		if amount <= 0:
			await ctx.send(embed = discord.Embed(
				description = f"__{ctx.author}__, конечно извините меня, но проход хацкерам сегодня закрыт."
			))
		else:

			self.collection.update_one({"_id": member.id},
				{"$set": {"balance": mbalance + amount}})

			await ctx.message.add_reaction("✅")

	@commands.command(
		name = "снять",
		aliases = ["undonate"],
		brief = "Снять гризкоины",
		usage = "undonate <@user> <amount>"	
	)
	@commands.has_permissions(view_audit_log=True)
	async def undonate_cash(self, ctx, member: discord.Member, amount: int):
		mbalance = self.collection.find_one({"_id": member.id})["balance"]

		if amount <= 0:
			await ctx.send(embed = discord.Embed(
				description = f"__{ctx.author}__, конечно извините меня, но проход хацкерам сегодня закрыт."
			))
		else:

			self.collection.update_one({"_id": member.id},
				{"$set": {"balance": mbalance - amount}})

			await ctx.message.add_reaction("✅")


	@commands.command(
		name = "казино",
		aliases = ["casino"],
		brief = "Сыграть в казино",
		usage = "casino <cout>"	
	)
	async def casino(self, ctx, cout:int):
		ubalance = self.collection.find_one({"_id": ctx.author.id})["balance"]
		mbalance = self.collection.find_one({"_id": 869133894849531934})["balance"]
		if ubalance >= cout and cout > 0:
		
			rand = int(random.randint(0,2))
			
			if rand == 0:
				
				self.collection.update_one({"_id": ctx.author.id},
				{"$set": {"balance": ubalance - cout}})

				self.collection.update_one({"_id": 869133894849531934},
				{"$set": {"balance": mbalance + cout}})

				await ctx.send(f"Вы проиграли {cout}")
			
			if rand == 1:
			
				await ctx.send("Вы остались при своих монетах")
			
			if rand == 2:
			
				await ctx.send("Вы выйграли")
			
				self.collection.update_one({"_id": ctx.author.id},
				{"$set": {"balance": ubalance + cout}})

				self.collection.update_one({"_id": 869133894849531934},
				{"$set": {"balance": mbalance - cout}})
		else:

			await ctx.send('У вас недостаточно денег')

	@commands.command(
		name = "help",
		aliases = ["помощь", "хелп"],
		brief = "Показывает доступные команды",
		usage = "!хелп"
		)
	async def help(self, ctx):
		emb = discord.Embed(title="Список команды")
		emb.add_field(name='Модерация',value=None,inline=False)
		emb.add_field(name='Система уровней',value=None,inline=False)
		await ctx.send(embed = emb)

	@commands.command()
	async def test(self, ctx):
		data = self.collection.find_one({"_id": ctx.author.id})
		await ctx.send(f'{data}')
def setup(client):
	client.add_cog(Economic(client))