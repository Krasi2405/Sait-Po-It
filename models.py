from peewee import *
from flask_bcrypt import generate_password_hash
from flask_login import UserMixin

DATABASE = SqliteDatabase("database.db")

class Admin(UserMixin, Model):
	username = CharField(unique = True)
	password = CharField()

	class Meta:
		database = DATABASE

	@classmethod
	def create_admin(cls, username, password):
		try:
			cls.create(username = username, password = generate_password_hash(password))
		except IntegrityError:
			pass



def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Admin], safe = True)
	DATABASE.close()
	