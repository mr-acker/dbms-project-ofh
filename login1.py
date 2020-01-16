
from bottle import get, run, jinja2_view, post, request, redirect, response,route
from models import User,Billings,Contact,Cart,Admin ,db
from bottle import static_file,template
import random

db.connect()

@get("/")
@jinja2_view("views/signup.html")
def home():
	return
@get("/home")
@jinja2_view("views/home.html")
def home():
	return

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./img')


@post("/signup")
def signup():
	username = request.forms.get('username')
	password = request.forms.get('password')

	users = User.select().where(User.username == username)

	if len(users) != 0:
		return "User already exists!"
	else:
		User.create(username=username, password=password)
	return redirect("/login")

@get("/login")
@jinja2_view("views/login.html")
def login():
	return

@post("/login")
def login():
	username = request.forms.get('username')
	password = request.forms.get('password')

	try:
		user = User.get(User.username == username)
	except:
		return "User does not exist!"

	if user.password == password:
		response.set_cookie("user_id", str(user.id))
		return redirect("/home")
	else:
		return "Invalid Credentials!!"


@post("/admin")
def login():
	username = request.forms.get('username')
	password = request.forms.get('password')

	try:
		user = Admin.get(Admin.username == username)
	except:
		return "User does not exist!"

	if user.password == password:
		response.set_cookie("user_id", str(user.id))
		return redirect("/adminq")
	else:
		return "Invalid Credentials!!"



@get("/admin")
@jinja2_view("views/admin.html")
def admin():
	return





@get("/adminq")
@jinja2_view("adminq.html")
def adminq():
	uid = request.get_cookie("user_id")
	items = User.select()
	print items
	return {"items":items}



@get("/logout")
@jinja2_view("login.html")
def logout():
	return
ran = random.randint(0, 1000)

@post("/book")
def book():
	proid=request.forms.get('proid')
	price=request.forms.get('price')
	radio=request.forms.get('radio')
	quantity=request.forms.get('quantity')
	uid = request.get_cookie("user_id")
	# user = User.get(User.id == uid)
	Bookings1.create(orderid=ran,userid=uid,proid=proid,price=price,radio=radio,quantity=quantity)
	return redirect("/billing")

@post("/contacts")
def contacts():
	firstname=request.forms.get('firstname')
	phone=request.forms.get('phone')
	subject=request.forms.get('subject')
	Contact.create(firstname=firstname,phone=phone,subject=subject)
	return redirect("/home")


@post("/billing")
def billing():
	firstname=request.forms.get('firstname')
	phone=request.forms.get('phone')
	address=request.forms.get('address')
	city=request.forms.get('city')
	state=request.forms.get('state')
	cardname=request.forms.get('cardname')
	cardnumber=request.forms.get('cardnumber')
	expmonth=request.forms.get('expmonth')
	expyear=request.forms.get('expyear')
	cvv=request.forms.get('cvv')
	Billings.create(orderid=ran,firstname=firstname,phone=phone,address=address,city=city,state=state,cardname=cardname,cardnumber=cardnumber,expmonth=expmonth,expyear=expyear,cvv=cvv)
	return redirect("/thankyou")	
	

@post("/book")
def cart():
	proid=request.forms.get('proid')
	price=request.forms.get('price')
	size=request.forms.get('radio')
	quantity=request.forms.get('quantity')
	uid = request.get_cookie("user_id")
	# user = User.get(User.id == uid)
	Cart.create(userid=uid,proid=proid,price=price,size=size,quantity=quantity)
	return redirect("/home")


# @post("/add")
# def add():
# 	uid = request.get_cookie("user_id")
# 	Cart.select(PROID,PRICE,SIZE,QUANTITY).where(Cart.userid_id == uid)
# 	return redirect ("/billing")



# @post("/cart")
# def cart():
# 	Cart.select()
	

@get("/add")
@jinja2_view("cart.html")
def cart():
	uid = request.get_cookie("user_id")
	items = Cart.select().where(Cart.userid_id == uid)
	print items
	return {"items":items}
# deleting code

@get("/del/<item_proid>")
@jinja2_view("views/cart.html")
def delete_instance(item_proid):
	item = Cart.get(Cart.proid == item_proid)
	uid = request.get_cookie("user_id")
	user = User.get(User.id == uid)

	if User.id == user:
		item.delete_instance()
		return redirect("/home")
	else:
		return "Operation Not Permitted!<br><a href='/home'>Go to Home</a>"
# editing code

@get("/change/<item_proid>")
@jinja2_view("edit.html")
def edit_expense(item_proid):
	item = Cart.get(Cart.proid == item_proid)
	uid = request.get_cookie("user_id")
	user = User.get(User.id == uid)

	if User.id == user:
		return {"item" : item}
	else:
		return redirect("/home")

@post("/change/<item_proid>")
def item_quantity(item_proid):
	item = Cart.get(Cart.proid == item_proid)
	uid = request.get_cookie("user_id")
	user = User.get(User.id == uid)
	if User.id == user:
		quantity = request.forms.get("quantity")
		item.quantity = quantity
		item.save()
	return redirect("/home")

@get("/aboutus")
@jinja2_view("aboutus.html")
def contact():
	return


@get("/contact")
@jinja2_view("Contacts.html")
def contact():
	return

@get("/mens")
@jinja2_view("views/mensclothing.html")
def mens():
	return

@get("/womens")
@jinja2_view("views/womensclothings.html")
def womensmens():
	return

@get("/home")
@jinja2_view("home.html")
def home():
	return


@get("/cart")
@jinja2_view("cart.html")
def add():
	return


@get("/kids")
@jinja2_view("views/kidsclothings.html")
def kids():
	return


@get("/MANAYAVAR1")
@jinja2_view("views/MANAYAVAR1.html")
def MANAYAVAR():
	return 

@get("/thankyou")
@jinja2_view("views/thanku.html")
def thankyou():
	return

@get("/buy")
@jinja2_view("views/paymentpage.html")
def payment():
	return



@get("/jackandjones")
@jinja2_view("views/jackandjones.html")
def jackandjones():
	return


@get("/BUFFALOE")
@jinja2_view("views/BUFFALOE'S.html")
def BUFFALOE():
	return



@get("/peter-england")
@jinja2_view("views/PETER-ENGLAND.html")
def PETERENGLAND():
	return


@get("/VANAARMANI")
@jinja2_view("views/VAN-ARMANI.html")
def VANARMANI():
	return


@get("/allensolly")
@jinja2_view("views/allensolly.html")
def allensolly():
	return



@get("/USPOLOASSN")
@jinja2_view("views/USPOLOASSN.html")
def USPOLOASSIN():
	return


@get("/MANAYAVAR")
@jinja2_view("views/MANAYAVAR.html")
def MANAYAVAR():
	return


@get("/ARVIND")
@jinja2_view("views/ARVIND.html")
def ARVIND():
	return



@get("/TOPSHOP")
@jinja2_view("views/TOPSHOP.html")
def TOPSHOP():
	return


@get("/AMERICANPERL")
@jinja2_view("views/AMERICAN%20PERL.html")
def PERL():
	return



@get("/PETER-ENGLAND1")
@jinja2_view("views/PETER-ENGLAND1.html")
def PETER():
	return


@get("/UNIQLO")
@jinja2_view("views/UNIQLO.html")
def UNIQLO():
	return

@get("/INDIAFABINDIA")
@jinja2_view("views/INDIAFABINDIA.html")
def INDIAFABINDIA():
	return


@get("/USPOLOASSIN1")
@jinja2_view("views/USPOLOASSIN1.html")
def USPOLOASSIN1():
	return


@get("/UNIQLO1")
@jinja2_view("views/UNIQLO1.html")
def UNIQLO1():
	return


@get("/SAHO")
@jinja2_view("views/SAHO.html")
def SAHO():
	return



@get("/ALLENSOLLY")
@jinja2_view("views/ALLENSOLLY.html")
def ALLENSOLLY():
	return



@get("/AMERICANPERL1")
@jinja2_view("views/AMERICANPERL1.html")
def payment():
	return


@get("/ARMYSTYLEZ")
@jinja2_view("views/ARMYSTYLEZ.html")
def ARMYSTYLEZ():
	return


@get("/UNIQLO2")
@jinja2_view("views/UNIQLO2.html")
def UNIQLO2():
	return


@get("/billing")
@jinja2_view("views/paymentpage.html")
def payment():
	return



@get("/INDIAFABINDIA1")
@jinja2_view("views/INDIAFABINDIA1.html")
def INDIAFABINDIA1():
	return



@get("/USPOLOASSIN2")
@jinja2_view("views/USPOLOASSIN2.html")
def USPOLOASSIN2():
	return



@get("/UNIQLO3")
@jinja2_view("views/UNIQLO3.html")
def UNIQLO3():
	return




@get("/SAHO1")
@jinja2_view("views/SAHO1.html")
def SAHO1():
	return




@get("/MANAYAVAR1")
@jinja2_view("views/MANAYAVAR1.html")
def MANAYAVAR1():
	return


@get("/MANAYAVAR2")
@jinja2_view("views/MANAYAVAR2.html")
def MANAYAVAR2():
	return

@get("/MANAYAVAR3")
@jinja2_view("views/MANAYAVAR3.html")
def MANAYAVAR3():
	return


@get("/KANCHIPURAMSILKS")
@jinja2_view("views/KANCHIPURAMSILKS.html")
def KANCHIPURAMSILKS():
	return


@get("/INDIAFABINDIA2")
@jinja2_view("views/INDIAFABINDIA2.html")
def INDIAFABINDIA2():
	return


@get("/MANAYAVAR4")
@jinja2_view("MANAYAVAR4.html")
def MANAYAVAR4():
	return


@get("/UNIQLO4")
@jinja2_view("views/UNIQLO4.html")
def UNIQLO4():
	return


@get("/MANAYAVAR5")
@jinja2_view("views/MANAYAVAR5.html")
def MANAYAVAR5():
	return


@get("/mensclothing")
@jinja2_view("views/mensclothing.html")
def mensclothing():
	return


@get("/womensclothings")
@jinja2_view("views/womensclothings.html")
def womensclothing():
	return



@get("/kidsclothings")
@jinja2_view("views/kidsclothings.html")
def kidsclothings():
	return




run(host="localhost", 
	port="8000", 
	debug=True)


