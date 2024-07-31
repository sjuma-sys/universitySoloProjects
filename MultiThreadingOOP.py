import threading
import mysql.connector
import socket
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.constants import *
from time import sleep
import queue
def main():
	pass

db = mysql.connector.connect(host="localhost",user="root",passwd="password",database="ClientLogin")
cursor = db.cursor()
usernames, passwords, iphonestock, macstock, airpodstock, customers, numberinque, baskets, send =[], [],[],[],[],[],[],[],[]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
checking = {'checks' : 0}
q = queue.Queue

class Blueprint(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x350')
        self.configure(bg='black')
        self.Frame = tk.Frame(self, relief=RIDGE, borderwidth=0, bg='grey')
        self.Frame.pack(fill=BOTH, expand=1)
send = []
def sendover():
	cursor.execute("SELECT * FROM Stock")
	for i in cursor:
		send.append(i)
if __name__ == "__main__":

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
		print(x)
	cursor.execute("SELECT username FROM Staff")
	for x in cursor:
		usernames.append(x)
		print(x)

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
	checkstock = Blueprint()			#checkstocks
	checkstock.title('Stock check')
	checkstock.ipcb = ttk.Combobox(checkstock.Frame, value=iphonestock)
	checkstock.ipcb['state'] = 'readonly'
	checkstock.ipcbtxt = Label(checkstock, text="Check iphone stock:",bg='black', fg='#40fd14')
	checkstock.ipcbtxt.place(x=70,y=180)
	checkstock.ipcb.place(x=215, y=180)
	checkstock.macb = ttk.Combobox(checkstock.Frame,value=macstock)
	checkstock.macb['state'] = 'readonly'
	checkstock.macbtxt = Label(checkstock, text="Check mac Stocks:", bg='black', fg='#40fd14')
	checkstock.macbtxt.place(x=70,y=220)
	checkstock.macb.place(x=125, y=220)
	checkstock.apcb = ttk.Combobox(checkstock.Frame,value=airpodstock)
	checkstock.apcb['state'] = 'readonly'
	checkstock.macbtxt = Label(checkstock, text="Check Airpod Stocks:", bg='black', fg='#40fd14')
	checkstock.macbtxt.place(x=70,y=260)
	checkstock.apcb.place(x=125, y=260)
	updatestock = Blueprint()					#update stockages
	updatestock.title('Stock updater')
	updatestock.ipstkcombobox = ttk.Combobox(updatestock.Frame, values=iphonestock)
	updatestock.ipstkcombobox.place(x=100, y=40)
	updatestock.ipstkcomboboxlbl = Label(updatestock.Frame, text='iphones:')
	updatestock.ipstkcomboboxlbl.place(x=10,y=40)
	updatestock.ipstkcombobox['state'] = 'readonly'
	updatestock.ipstockentry = Entry(updatestock.Frame, bg='grey')
	updatestock.ipstockentry.place(x=100, y=70)
	updatestock.ipstockentrylbl = Label(updatestock.Frame,text='How many')
	updatestock.ipstockentrylbl.place(x=10, y=70)
	updatestock.apstkcombobox = ttk.Combobox(updatestock.Frame, values=airpodstock)
	updatestock.apstkcombobox.place(x=100, y=120)
	updatestock.apstkcomboboxlbl = Label(updatestock.Frame, text='airpods:')
	updatestock.apstkcomboboxlbl.place(x=10, y=120)
	updatestock.apstkcombobox['state'] = 'readonly'
	updatestock.apstkentry = Entry(updatestock.Frame, bg='grey')
	updatestock.apstkentry.place(x=100, y=150)
	updatestock.apstkentrylbl = Label(updatestock.Frame,text='How many')
	updatestock.apstkentrylbl.place(x=10, y=150)
	updatestock.mcstkcombobox = ttk.Combobox(updatestock.Frame, values=macstock)
	updatestock.mcstkcombobox.place(x=100, y=180)
	updatestock.mcstkcomboboxlbl = Label(updatestock.Frame, text='macbooks:')
	updatestock.mcstkcomboboxlbl.place(x=10, y=180)
	updatestock.mcstkcombobox['state'] = 'readonly'
	updatestock.mcstkentry = Entry(updatestock.Frame, bg='grey')
	updatestock.mcstkentry.place(x=100, y=210)
	updatestock.mcstkentrylbl = Label(updatestock.Frame,text='How many')
	def addstock():
  		lookingfor = [i for i in (updatestock.ipstkcombobox.get(), updatestock.apstkcombobox.get(), updatestock.mcstkcombobox.get())]
  		for i in lookingfor:
  			if i == '':
  				continue
  			elif 'iphone8' in i:	
  				iphone8stockupdater = iphone8stk + int(updatestock.ipstockentry.get())
  				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(iphone8stockupdater, i))
  				db.commit()
  			elif 'iphone10' in i:	
  				iphone10stockupdater = iphone10stk + int(updatestock.ipstockentry.get())
  				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(iphone10stockupdater, i))
  				db.commit()
  			elif 'iphone11' in i:	
  				iphone11stockupdater = iphone11stk + int(updatestock.ipstockentry.get())
  				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(iphone11stockupdater, i))
  				db.commit()
  			elif 'Macbook' == i:	
  				macbstkupdater = int(updatestock.mcstkentry.get()) + macbstk
  				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(macbstkupdater, i))
  				db.commit()
  			elif 'MacPro' == i:	
  				macprostkupdater = int(updatestock.mcstkentry.get()) + macprostk
  				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(macprostkupdater, i))
  				db.commit()
  			elif 'DesktopMac' == i:	
  				dsktopmcstkupdater = int(updatestock.mcstkentry.get()) + dsktopmcstk
  				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(dsktopmcstkupdater, i))
  				db.commit()
  			elif 'airpodpros' == i:
  				airpodstockupdater = int(updatestock.apstkentry.get()) + airpprostk
  				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(airpodstockupdater, i))
  				db.commit()
  			elif 'fstgenpods' == i:
  				fstgenairstkupdater = int(updatestock.apstkentry.get()) + fstgenairstk
  				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(fstgenairstkupdater, i))
  				db.commit()
  			elif 'sndgenairpods' == i:
  				sndgenairstkupdater = int(updatestock.apstkentry.get()) + sndgenairstk
  				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(sndgenairstkupdater, i))
  				db.commit()
	def removestock():
  		lookingfor = [i for i in (updatestock.ipstkcombobox.get(), updatestock.apstkcombobox.get(), updatestock.mcstkcombobox.get())]
  		for i in lookingfor:
  			if i == '':
  				continue
  			elif 'iphone8' in i:	
  				iphone8stockremover = iphone8stk - int(updatestock.ipstockentry.get())
  				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(iphone8stockremover, i))
  				db.commit()
  			elif 'iphone10' in i:	
  				iphone10stockremover = iphone11stk - int(updatestock.ipstockentry.get())
  				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(iphone10stockremover, i))
  				db.commit()
  			elif 'iphone11' in i:	
  				iphone11stockremover = iphone11stk - int(updatestock.ipstockentry.get())
  				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(iphone11stockremover, i))
  				db.commit()
  			elif 'Macbook' == i:	
  				macbstkremover = int(updatestock.mcstkentry.get()) - macbstk
  				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(macbstkremover, i))
  				db.commit()
  			elif 'MacPro' == i:	
  				macprostkremover = int(updatestock.mcstkentry.get()) - macprostk
  				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(macprostkremover, i))
  				db.commit()
  			elif 'DesktopMac' == i:	
  				dsktopmcstkremover = int(updatestock.mcstkentry.get()) - dsktopmcstkremover
  				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(dsktopmcstkremover, i))
  				db.commit()
  			elif 'airpodpros' == i:
  				airpodstockremover = int(updatestock.apstkentry.get()) - airpprostk
  				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(airpodstockremover, i))
  				db.commit()
  			elif 'fstgenpods' == i:
  				fstgenairstkremover = int(updatestock.apstkentry.get()) - fstgenairstk
  				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(fstgenairstkremover, i))
  				db.commit()
  			elif 'sndgenairpods' == i:
  				sndgenairstkremover = int(updatestock.apstkentry.get()) - sndgenairstk
  				cursor.execute("UPDATE Stock SET Quantity = {} WHERE StockName LIKE '{}%'".format(sndgenairstkremover, i))
  				db.commit()
	updatestock.mcstkentrylbl.place(x=10, y=210)
	updatestock.add = Button(updatestock.Frame, text='Add Stock', bg='green', fg='black', command=addstock)
	updatestock.add.place(x=10, y=300)
	updatestock.rmstkbtn = Button(updatestock.Frame, text='Remove Stock', bg='green', fg='black', command=removestock)
	updatestock.rmstkbtn.place(x=100, y=300)
	updatestock.exit = Button(updatestock.Frame, text='Exit', bg='green', fg='black', command=updatestock.withdraw)
	updatestock.exit.place(x=200, y=300)
	
	mainwindow = Blueprint()		#main window
	mainwindow.title('Main Menu')
	mainwindow.mwdwbtn1 = Button(mainwindow.Frame, text='Check Stock', bg='green', fg='black', width=50, relief=SUNKEN, command=checkstock.deiconify)
	mainwindow.mwdwbtn2 = Button(mainwindow.Frame, text='Update Stock', bg='yellow', fg='black', width=50, relief=SUNKEN, command=updatestock.deiconify)
	mainwindow.mydwbtn4 = Button(mainwindow.Frame, text='Exit', bg='Red', fg='black', width=50, relief=SUNKEN, command=mainwindow.quit)
	mainwindow.mwdwbtn1.pack(side=TOP, fill=BOTH,expand=True)
	mainwindow.mwdwbtn2.pack(side=TOP, fill=BOTH,expand=True)
	mainwindow.mydwbtn4.pack(side=TOP, fill=BOTH,expand=True)
	checkstock.configure(bg='black')
	updatestock.configure(bg='black')
	def getem():
  		getting = [i for i in (checkstock.apcb.get(), checkstock.macb.get(), checkstock.ipcb.get())]
  		for i in getting:
  			if i =='':
  				pass
  			else:
  				cursor.execute("SELECT StockName,Quantity FROM Stock WHERE StockName LIKE '{}%' ".format(i))
  				for i in cursor:
  					showinfo(title='Heres some stock we found!', message=f'we have {i}')
	def gotemall():
  		cursor.execute("SELECT StockName,Quantity FROM Stock")
  		for i in cursor:
  			showinfo(title='Heres all the stock we found!', message=f'we have {i}')	
	checkstock.stockchecker = Button(checkstock.Frame, text='Pull stock from table from selection', command=getem, bg='white', fg='Green')
	checkstock.ultimatestockchecker = Button(checkstock.Frame, text='Pull all stock info', command=gotemall,bg = 'white', fg='Green')
	checkstock.stockchecker.place(x=2, y=300)
	checkstock.ultimatestockchecker.place(x=265, y=300)

	loginwindow = Blueprint()				#loginwindow
	loginwindow.title('Login')
	loginwindow.atxt = Label(loginwindow, text='Username:', bg='grey', fg='black')
	loginwindow.atxt.place(x=65, y=50)
	loginwindow.enterusr = Entry(loginwindow.Frame, bg='gray75', width=21, text='Username') 
	loginwindow.enterusr.place(x=125, y=50, width= 150)
	loginwindow.atxt = Label(loginwindow, text='Password:', bg='grey', fg='black')
	loginwindow.atxt.place(x=65, y=100)
	loginwindow.enterpw = Entry(loginwindow.Frame, bg='gray75', width=21, text='Password') 
	loginwindow.enterpw.place(x=125, y=100, width= 150)
	def logincheck(*args):
  		if loginwindow.enterusr.get() not in usernames[0] and loginwindow.enterpw.get() not in passwords[0]:
  			showinfo(title='Wrong credentials!', message=f'Please double check before re-entering\n')
  			checking['checks'] = checking['checks'] + 1
  		if loginwindow.enterusr.get() in usernames[0] and loginwindow.enterpw.get() in passwords[0]:
  			mainwindow.deiconify()	#show the main window
  			loginwindow.destroy
  			loginwindow.withdraw()	#hide the login screen
  			showinfo(title='Welcome!',message=f'You have now entered the main application')
  			mainwindow.mainloop()
  		if checking['checks'] == 3:
  			showinfo(title='Wrong credentials!',message=f'You are now being exited from the application\n due to incorrect credentials')
  			loginwindow.destroy
  			loginwindow.withdraw()
	loginwindow.button = tk.Button(loginwindow.Frame, text="Exit",command=loginwindow.quit ,padx=10, pady=10, fg='black',bg='White', width=15)
	loginwindow.button2 = tk.Button(loginwindow.Frame,text="Login",padx=10, pady=10,bg='White' ,fg='black',width=15)
	loginwindow.button2.bind('<Button-1>', logincheck)
	loginwindow.button.place(x=265, y=150)
	loginwindow.button2.place(x=2, y=150)
	loginwindow.geometry('400x250')

	mainwindow.withdraw()
	updatestock.withdraw()
	checkstock.withdraw()
	loginwindow.mainloop()
