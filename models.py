# TABLES CREATION FOR BACKEND
from peewee import *

db = SqliteDatabase("dbmslabsexternal.db")

class User(Model):
	username = TextField()
	password = CharField()

	class Meta:
		database = db



class Billings(Model):
	orderid=TextField()
	firstname=CharField()
	phone=CharField()
	address=CharField()
	city=CharField()
	state=CharField()
	cardname=CharField()
	cardnumber=CharField()
	expmonth=CharField()
	expyear=CharField()
	cvv=IntegerField()

	class Meta:
		database = db


class Contact(Model):
	firstname=TextField()
	phone=TextField()
	subject=TextField()

	class Meta:
		database=db

class Cart(Model):
	userid=ForeignKeyField(User)
	proid=TextField()
	price=TextField()
	size=FixedCharField()
	quantity=TextField()
	class Meta:
		database=db

class Admin(Model):
	username=TextField()
	password=CharField()
	class Meta:
		database=db

# class Record(Model):
# 	orderid=TextField();
# 	daterecord=TextField();
# 	class Meta:
# 		database=db
		# """docstring for Meta:
		#  __init__(self, arg):
		# 	super(Meta:
		# 	_init__()
		# 	self.arg = arg
			
		




if __name__=="__main__":
	db.connect()
	db.create_tables([User,Billings,Contact,Cart,Admin])


