import threading
import mysql.connector
import socket
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.constants import *
from time import sleep
import multiprocessing as mp
import queue
# def main():
# 	pass
file = open('reciepts.txt', 'w')
checking = {'checks': 0}
q = queue.Queue()
db = mysql.connector.connect(host="localhost",user="root",passwd="password",database="ClientLogin")
usernames, passwords, iphonestock, macstock, airpodstock, customers, numberinque, baskets = [],[],[],[],[],[],[],[]
# PORT = 5000
# HOST = socket.gethostbyname(socket.gethostname())	#gets ip address
# ADDR = (HOST, PORT)
cursor = db.cursor()
# 	conn.close()

# def startbasketchat(*args):	#handle new connections
# 	while True:
# 		server_socket.listen()
# 		conn, addr = server_socket.accept()	#allows the communication between server and host
# 		thread = threading.Thread(target=handlingbasketchat)  #will allow multiple connections from handling
# 		print(f'the active connections are{ threading.activeCount() -1}')	#shows whos connected
# 		thread.start()	
# print('Server is starting')
if __name__ == '__main__':
	cursor.execute("SELECT StockName from Stock where StockName LIKE 'iphone%'")
	for x in cursor:
		iphonestock.append(x)
	cursor.execute("SELECT StockName from Stock where StockName LIKE '%pod%'")
	for x in cursor:
		airpodstock.append(x)
	cursor.execute("SELECT StockName from Stock where StockName LIKE 'Mac%'")
	for x in cursor:
		macstock.append(x)
	cursor.execute("SELECT StockName from Stock where StockName LIKE 'DesktopMac%'")
	for x in cursor:
		macstock.append(x)
	cursor.execute("SELECT password FROM Staff") #Select function of course
	for x in cursor:
		passwords.append(x)
	cursor.execute("SELECT username FROM Staff")
	for x in cursor:
		usernames.append(x)
	
	def alwayschecking():
		for i in range(900):
			global iphone8stk, iphone10stk, iphone11stk, fstgenairstk, sndgenairstk, airpprostk,macbstk , dsktopmcstk, macprostk
			cursor.execute("SELECT Quantity from Stock WHERE StockName LIKE 'iphone8%'")
			output=cursor.fetchone()
			iphone8stk = int(output[0])
			cursor.execute("SELECT Quantity from Stock WHERE StockName LIKE 'iphone10%'")
			output2 = cursor.fetchone()
			iphone10stk = int(output2[0])
			cursor.execute("SELECT Quantity from Stock WHERE StockName LIKE 'iphone11%'")
			output3 = cursor.fetchone()
			iphone11stk = int(output3[0])
			cursor.execute("SELECT Quantity from Stock WHERE StockName LIKE 'airpodpros%'")
			output4 = cursor.fetchone()
			airpprostk = int(output4[0])
			cursor.execute("SELECT Quantity from Stock WHERE StockName LIKE 'fstgenpods%'")
			output5 = cursor.fetchone()
			fstgenairstk = int(output5[0])
			cursor.execute("SELECT Quantity from Stock WHERE StockName LIKE 'sndgenairpods%'")
			output6 = cursor.fetchone()
			sndgenairstk = int(output6[0])
			cursor.execute("SELECT Quantity from Stock WHERE StockName LIKE 'MacPro%'")
			output7 = cursor.fetchone()
			macprostk = int(output7[0])
			cursor.execute("SELECT Quantity from Stock WHERE StockName LIKE 'Macbook%'")
			output8 = cursor.fetchone()
			macbstk = int(output8[0])
			cursor.execute("SELECT Quantity from Stock WHERE StockName LIKE 'DesktopMac%'")
			output9 = cursor.fetchone()
			dsktopmcstk = int(output9[0])
			sleep(30)	#continus checks every 30 seconds
	
	chekingthread = threading.Thread(target=alwayschecking, daemon=True) 	#set to daemon as it should close with the program instead
	chekingthread.start()	#of it looping outside the main program
	
	lgnwndw = tk.Tk() #spawns a window/how to create a window
	lgnwndw.configure(bg='grey')
	lgnwndw.geometry('400x250')
	lgnwndw.title('Login')
	frameforwindow = tk.Frame(lgnwndw, relief=RIDGE, borderwidth=0, bg='grey')
	
	atxt = Label(lgnwndw, text='Username:', bg='grey', fg='black')
	atxt = atxt.place(x=65, y=50)
	enterusr = Entry(frameforwindow, bg='gray75', width=21, text='Username') 
	enterusr.place(x=125, y=50, width= 150)
	
	atxt = Label(lgnwndw, text='Password:', bg='grey', fg='black')
	atxt = atxt.place(x=65, y=100)
	enterpw = Entry(frameforwindow, bg='gray75', width=21, text='Password') 
	enterpw.place(x=125, y=100, width= 150)
	
	def logincheck(*args):
		if enterusr.get() not in usernames[0] and enterpw.get() not in passwords[0]:
			showinfo(
	        title='Wrong credentials!', 
	        message=f'Please double check before re-entering\n')
			checking['checks'] = checking['checks'] + 1
		if enterusr.get() in usernames[0] and enterpw.get() in passwords[0]:
			mwdw.deiconify()	#show the main window
			lgnwndw.destroy
			lgnwndw.withdraw()	#hide the login screen
			showinfo(title='Welcome!',message=f'You have now entered the main application')
			mwdw.mainloop()
		if checking['checks'] == 3:
			showinfo(title='Wrong credentials!', 
	    	message=f'You are now being exited from the application\n due to incorrect credentials')
			lgnwndw.destroy
			lgnwndw.withdraw()
	
	button = tk.Button(frameforwindow, text="Exit",command=(lgnwndw.quit) ,padx=10, pady=10, fg='black',bg='White', width=15)
	button2 = tk.Button(frameforwindow,text="Login",padx=10, pady=10,bg='White' ,fg='black',width=15)
	button2.bind('<Button-1>', logincheck)	#everytime its clicked it will check against the function
	button.bind('Button-1', chekingthread.join)
	button2.place(x=2, y=150)
	frameforwindow.pack(fill=BOTH,expand=1)
	button.place(x=265, y=150)
	
	mwdw = tk.Tk() #spawns a window/how to create a window
	mwdw.configure(bg='black')
	mwdw.geometry('400x350')
	mwdw.title('Main application')
	framemwdw = tk.Frame(mwdw, relief=RIDGE, borderwidth=0, bg='black')
	framemwdw.pack(fill=BOTH, expand=1)
	
	#Check stock sect
	cstk = tk.Tk() #spawns a window/how to create a window
	cstk.configure(bg='black')
	cstk.geometry('400x350')
	cstk.title('Stock check')
	framecstk = tk.Frame(cstk, relief=RIDGE, borderwidth=0, bg='black')
	framecstk.pack(fill=BOTH, expand=1)
	
	ipcb = ttk.Combobox(framecstk, value=iphonestock)
	ipcb['state'] = 'readonly'
	ipcbtxt = Label(cstk, text="Check iphone stock:",bg='black', fg='#40fd14')
	ipcbtxt.place(x=70,y=180)
	ipcb.place(x=215, y=180)
	
	
	macb = ttk.Combobox(framecstk,value=macstock)
	macb['state'] = 'readonly'
	macbtxt = Label(cstk, text="Check mac Stocks:", bg='black', fg='#40fd14')
	macbtxt.place(x=70,y=220)
	macb.place(x=125, y=220)
	
	apcb = ttk.Combobox(framecstk,value=airpodstock)
	apcb['state'] = 'readonly'
	macbtxt = Label(cstk, text="Check Airpod Stocks:", bg='black', fg='#40fd14')
	macbtxt.place(x=70,y=260)
	apcb.place(x=125, y=260)
	
	def getem():
		getting = [i for i in (apcb.get(), macb.get(), ipcb.get())]
		for i in getting:
			if i =='':
				pass
			else:
				cursor.execute("SELECT StockName, Prices,Quantity ,COLUMNColour FROM Stock WHERE StockName LIKE '{}%' ".format(i))
				for i in cursor:
					showinfo(title='Heres some stock we found!', message=f'we have {i}')
	
	def gotemall():
		cursor.execute("SELECT  StockName, Prices,Quantity ,COLUMNColour FROM Stock")
		for i in cursor:
			showinfo(title='Heres all the stock we found!', message=f'we have {i}')
	
	stockchecker = Button(framecstk, text='Pull stock from table from selection', command=getem, bg='white', fg='Green')
	ultimatestockchecker = Button(framecstk, text='Pull all stock info', command=gotemall,bg = 'white', fg='Green')
	stockchecker.place(x=2, y=300)
	ultimatestockchecker.place(x=265, y=300)
	
	#Update stock
	upstk = tk.Tk() 
	upstk.configure(bg='black')
	upstk.geometry('400x350')
	upstk.title('Stock updater')
	frameupstk = tk.Frame(upstk, relief=RIDGE, borderwidth=0, bg='black')
	frameupstk.pack(fill=BOTH, expand=1)
	def addstock():
		lookingfor = [i for i in (ipstkcombobox.get(), apstkcombobox.get(), mcstkcombobox.get())]
		for i in lookingfor:
			if i == '':
				continue
			elif 'iphone8' in i:	
				iphone8stockupdater = iphone8stk + int(ipstockentry.get())
				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(iphone8stockupdater, i))
				db.commit()
			elif 'iphone10' in i:	
				iphone10stockupdater = iphone10stk + int(ipstockentry.get())
				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(iphone10stockupdater, i))
				db.commit()
			elif 'iphone11' in i:	
				iphone11stockupdater = iphone11stk + int(ipstockentry.get())
				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(iphone11stockupdater, i))
				db.commit()
			elif 'Macbook' == i:	
				macbstkupdater = int(mcstkentry.get()) + macbstk
				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(macbstkupdater, i))
				db.commit()
			elif 'MacPro' == i:	
				macprostkupdater = int(mcstkentry.get()) + macprostk
				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(macprostkupdater, i))
				db.commit()
			elif 'DesktopMac' == i:	
				dsktopmcstkupdater = int(mcstkentry.get()) + dsktopmcstk
				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(dsktopmcstkupdater, i))
				db.commit()
			elif 'airpodpros' == i:
				airpodstockupdater = int(apstkentry.get()) + airpprostk
				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(airpodstockupdater, i))
				db.commit()
			elif 'fstgenpods' == i:
				fstgenairstkupdater = int(apstkentry.get()) + fstgenairstk
				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(fstgenairstkupdater, i))
				db.commit()
			elif 'sndgenairpods' == i:
				sndgenairstkupdater = int(apstkentry.get()) + sndgenairstk
				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(sndgenairstkupdater, i))
	
	def removestock():
		lookingfor = [i for i in (ipstkcombobox.get(), apstkcombobox.get(), mcstkcombobox.get())]
		for i in lookingfor:
			if i == '':
				continue
			elif 'iphone8' in i:	
				iphone8stockremover = iphone8stk - int(ipstockentry.get())
				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(iphone8stockremover, i))
				db.commit()
			elif 'iphone10' in i:	
				iphone10stockremover = iphone11stk - int(ipstockentry.get())
				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(iphone10stockremover, i))
				db.commit()
			elif 'iphone11' in i:	
				iphone11stockremover = iphone11stk - int(ipstockentry.get())
				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(iphone11stockremover, i))
				db.commit()
			elif 'Macbook' == i:	
				macbstkremover = int(mcstkentry.get()) - macbstk
				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(macbstkremover, i))
				db.commit()
			elif 'MacPro' == i:	
				macprostkremover = int(mcstkentry.get()) - macprostk
				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(macprostkremover, i))
				db.commit()
			elif 'DesktopMac' == i:	
				dsktopmcstkremover = int(mcstkentry.get()) - dsktopmcstkremover
				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(dsktopmcstkremover, i))
				db.commit()
			elif 'airpodpros' == i:
				airpodstockremover = int(apstkentry.get()) - airpprostk
				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(airpodstockremover, i))
				db.commit()
			elif 'fstgenpods' == i:
				fstgenairstkremover = int(apstkentry.get()) - fstgenairstk
				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(fstgenairstkremover, i))
				db.commit()
			elif 'sndgenairpods' == i:
				sndgenairstkremover = int(apstkentry.get()) - sndgenairstk
				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(sndgenairstkremover, i))
				db.commit()
	
	ipstkcombobox = ttk.Combobox(frameupstk, values=iphonestock)
	ipstkcombobox.place(x=100, y=40)
	ipstkcomboboxlbl = Label(frameupstk, text='iphones:')
	ipstkcomboboxlbl.place(x=10,y=40)
	ipstkcombobox['state'] = 'readonly'
	
	ipstockentry = Entry(frameupstk, bg='grey')
	ipstockentry.place(x=100, y=70)
	ipstockentrylbl = Label(frameupstk,text='How many')
	ipstockentrylbl.place(x=10, y=70)
	
	apstkcombobox = ttk.Combobox(frameupstk, values=airpodstock)
	apstkcombobox.place(x=100, y=120)
	apstkcomboboxlbl = Label(frameupstk, text='airpods:')
	apstkcomboboxlbl.place(x=10, y=120)
	apstkcombobox['state'] = 'readonly'
	
	apstkentry = Entry(frameupstk, bg='grey')
	apstkentry.place(x=100, y=150)
	apstkentrylbl = Label(frameupstk,text='How many')
	apstkentrylbl.place(x=10, y=150)
	
	mcstkcombobox = ttk.Combobox(frameupstk, values=macstock)
	mcstkcombobox.place(x=100, y=180)
	mcstkcomboboxlbl = Label(frameupstk, text='macbooks:')
	mcstkcomboboxlbl.place(x=10, y=180)
	mcstkcombobox['state'] = 'readonly'
	
	mcstkentry = Entry(frameupstk, bg='grey')
	mcstkentry.place(x=100, y=210)
	mcstkentrylbl = Label(frameupstk,text='How many')
	mcstkentrylbl.place(x=10, y=210)
	
	#update stock options
	upstkadd = Button(frameupstk, text='Add Stock', bg='green', fg='black', command=addstock)
	upstkadd.place(x=10, y=300)
	
	#remove stock options
	rmstkbtn = Button(frameupstk, text='Remove Stock', bg='green', fg='black', command=removestock)
	rmstkbtn.place(x=100, y=300)
	
	exitup = Button(frameupstk, text='Exit', bg='green', fg='black', command=upstk.quit)
	exitup.place(x=200, y=300)
	# clientele = tk.Tk() #spawns a window/how to create a window
	# clientele.configure(bg='black')
	# clientele.geometry('400x350')
	# clientele.title('Customer details')
	# clintframe = tk.Frame(clientele, relief=RIDGE, borderwidth=0, bg='grey')
	# clintframe.pack(fill=BOTH, expand=1)
	#make somewhere that we can see amount of current customers, add more customers and remove customers
	
	# chckwhatsleft = tk.Tk() #spawns a window/how to create a window
	# chckwhatsleft.configure(bg='black')
	# chckwhatsleft.geometry('400x350')
	# chckwhatsleft.title('Customer details')
	# chkframe = tk.Frame(chckwhatsleft, relief=RIDGE, borderwidth=0, bg='grey')
	# chkframe.pack(fill=BOTH, expand=1)
	
	# stocktosell = ttk.Combobox(chkframe, text='hmm', values=baskets)
	# stocktosell.place(x=100, y=10)
	# stocksold = Label(chkframe, text='Customers basket')
	# stocksold.place(x=10, y=10)
	# stocktosell['state'] = 'readonly'
	
	# finipstkcombobox = ttk.Combobox(chkframe, values=iphonestock)
	# finipstkcombobox.place(x=100, y=40)
	# finipstkcomboboxlbl = Label(chkframe, text='iphones:')
	# finipstkcomboboxlbl.place(x=10,y=40)
	# finipstkcombobox['state'] = 'readonly'
	
	# finipstockentry = Entry(chkframe, bg='grey')
	# finipstockentry.place(x=100, y=70)
	# finipstockentrylbl = Label(chkframe,text='How many')
	# finipstockentrylbl.place(x=10, y=70)
	
	# finapstkcombobox = ttk.Combobox(chkframe, values=airpodstock)
	# finapstkcombobox.place(x=100, y=120)
	# finapstkcomboboxlbl = Label(chkframe, text='airpods:')
	# finapstkcomboboxlbl.place(x=10, y=120)
	# finapstkcombobox['state'] = 'readonly'
	
	# finapstkentry = Entry(chkframe, bg='grey')
	# finapstkentry.place(x=100, y=150)
	# finapstkentrylbl = Label(chkframe,text='How many')
	# finapstkentrylbl.place(x=10, y=150)
	
	# finmcstkcombobox = ttk.Combobox(chkframe, values=macstock)
	# finmcstkcombobox.place(x=100, y=180)
	# finmcstkcomboboxlbl = Label(chkframe, text='macbooks:')
	# finmcstkcomboboxlbl.place(x=10, y=180)
	# finmcstkcombobox['state'] = 'readonly'
	
	# finmcstkentry = Entry(chkframe, bg='grey')
	# finmcstkentry.place(x=100, y=210)
	# finmcstkentrylbl = Label(chkframe,text='How many')
	# finmcstkentrylbl.place(x=10, y=210)
	
	#update stock options
	# finupstkadd = Button(chkframe, text='Add Stock', bg='green', fg='black', command=addstock)
	# finupstkadd.place(x=10, y=300)
	
	#remove stock options
	# finrmstkbtn = Button(chkframe, text='Remove Stock', bg='green', fg='black', command=removestock)
	# finrmstkbtn.place(x=100, y=300)
	
	# chkallbtn3 = Button(clintframe, text='Customers and baskets', bg='orange', fg='black', width=50, relief=SUNKEN, command=chckwhatsleft.deiconify)
	# chkallbtn4 = Button(clintframe, text='Exit', bg='Red', fg='black', width=50, relief=SUNKEN, command=clientele.quit)
	# chkallbtn3.pack(side=TOP, fill=BOTH,expand=True)
	# chkallbtn4.pack(side=TOP, fill=BOTH,expand=True)
	
	# def anothercheck():
	# 	for i in range(90000):
	# 		if len(customers) == len(baskets):
	# 			q.put(i)
	# 			for i in baskets:
	# 				q.get(i)
	# 				[file.writelines(f'{str(a)}\n') for a in zip(customers, numberinque, baskets)]
	# 		sleep(300)
	# notherthread = threading.Thread(target=anothercheck, daemon = True)
	# notherthread.start()
	mwdwbtn1 = Button(framemwdw, text='Check Stock', bg='green', fg='black', width=50, relief=SUNKEN, command=cstk.deiconify)
	mwdwbtn2 = Button(framemwdw, text='Update Stock', bg='yellow', fg='black', width=50, relief=SUNKEN, command=upstk.deiconify)
	# mwdwbtn3 = Button(framemwdw, text='Customer list/updater', bg='orange', fg='black', width=50, relief=SUNKEN, command=clientele.deiconify)
	mydwbtn4 = Button(framemwdw, text='Exit', bg='Red', fg='black', width=50, relief=SUNKEN, command=mwdw.quit)
	mwdwbtn1.pack(side=TOP, fill=BOTH,expand=True)
	mwdwbtn2.pack(side=TOP, fill=BOTH,expand=True)
	mydwbtn4.pack(side=TOP, fill=BOTH,expand=True)
	
	# chckwhatsleft.withdraw()
	# clientele.withdraw()
	upstk.withdraw()	#hides them
	cstk.withdraw()
	mwdw.withdraw()
	lgnwndw.mainloop()
	file.close()
