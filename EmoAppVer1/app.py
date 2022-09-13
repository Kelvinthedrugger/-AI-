# -*- coding:utf-8 -*-
from flask import Flask, render_template, make_response, request, url_for, flash, redirect, jsonify
import os
import time
import sqlite3
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from werkzeug.exceptions import abort
import requests
import json
from selenium.common.exceptions import NoSuchElementException
#from flask_apscheduler import APScheduler
from flask_socketio import SocketIO, emit
from gevent.pywsgi import WSGIServer
#from flask_ngrok import run_with_ngrok

app = Flask(__name__, template_folder='./templates')
app.config['SECRET_KEY'] = 'secret!'
#app.config["DEBUG"]=True
socketio = SocketIO(app)
#run_with_ngrok(app)
thePrevWrd=""
RecievedChange = False
CurrentPerson = ""
VA1 = [0.0,0.0]
VA2 = [0.0,0.0]
Field = [0.0,0.0]
Speak = [0.0,0.0]
SendTimes = 0
optionla = Options()
optionla.add_argument("--window-size=1920,1080")
optionla.add_argument("--start-maximized")
optionla.add_argument("disable-notifications")
optionla.add_argument("--headless")
#driver = webdriver.Chrome(ChromeDriverManager().install(), options=optionla)
driver = webdriver.Chrome(executable_path=r'C:\Users\sam\Desktop\EmoAppVer1\chromedriver.exe', options=optionla)
driver.get('https://www.google.com')
#http_server = WSGIServer(('', 5000), app)
#http_server.serve_forever()

def login_FB(usrwrd,passwrd):
	driver.get('https://www.facebook.com/')
	print ("Opened facebook")
	sleep(1)
	username_box = driver.find_element('id','email')
	username_box.send_keys(usrwrd)
	print ("Email Id entered")
	sleep(1)
	password_box = driver.find_element('id','pass')
	password_box.send_keys(passwrd)
	print ("Password entered")
	login_box = driver.find_element('name','login')
	login_box.click()
	print ("Done")
	sleep(5)
	driver.get('https://www.facebook.com/messages/t/')

def Search_Person(person):
	driver.find_element(By.XPATH,"//span[text()='"+person+"']").click()
	print("Person Exist")
	sleep(3)

def DisplayMessages(person):
	all_dialogs = driver.find_elements(By.XPATH,"//div[@data-scope='messages_table']")
	#SaveDialogForm=[["",""]]*len(all_dialogs)
	SaveDialogForm = []
	for i in range(len(all_dialogs)):
		TempDialog = ["",""]
		"""
		try:
			all_dialogs[i].find_element(By.XPATH,".//span[text()='"+person+"' or text()='你傳送了']")
			#print(".//span[text()='"+person+"' or text()='你傳送了']")
			#print('有近來')
			try:
				all_dialogs[i].find_element(By.XPATH,".//span[text()='你傳送了']")
				TempDialog[0]='我'
				TempDialog[1]=all_dialogs[i].find_element(By.XPATH,".//div[@role='none' and @dir='auto']").text
				#print(SaveDialogForm[i])
			except:
				#all_dialogs[i].find_element(By.XPATH,".//span[text()='你傳送了']")
				#print('有我')
				TempDialog[0]=person
				TempDialog[1]=all_dialogs[i].find_element(By.XPATH,".//div[@role='none' and @dir='auto']").text
				#print(SaveDialogForm[i])
		except:
			print('this is not what i want')
		"""
		try:
			all_dialogs[i].find_element(By.XPATH,".//div[@role='none' and @dir='auto']")
			try:
				all_dialogs[i].find_element(By.XPATH,".//span[text()='你傳送了']")
				TempDialog[0]='我'
				TempDialog[1]=all_dialogs[i].find_element(By.XPATH,".//div[@role='none' and @dir='auto']").text
			except:
				TempDialog[0]=person
				TempDialog[1]=all_dialogs[i].find_element(By.XPATH,".//div[@role='none' and @dir='auto']").text
		except:
			print("0")
		if TempDialog[0]!="" and TempDialog[1]!="":
			SaveDialogForm.append(TempDialog)
	return SaveDialogForm

def CheckUpdate(person):
	global thePrevWrd
	global RecievedChange
	#print('被呼叫了！')
	try:
		thelastwrd = (driver.find_elements(By.XPATH,".//div[@role='none' and @dir='auto']"))[-1].text
		if thelastwrd!=thePrevWrd:
			print('更新了！')
			thePrevWrd = thelastwrd
			#DisplayMessages(person)
			#chatroom()
			#driver.navigate().refresh()
			RecievedChange = True
		else:
			print("沒更新")
			RecievedChange = False
	except:
		print('上面函式運行失敗')
	

def SendChatRoom(message):
	driver.find_element(By.CSS_SELECTOR,"[aria-label='訊息']").send_keys(message)
	sleep(1)
	driver.find_element(By.CSS_SELECTOR,"[aria-label='按 Enter 即可傳送']").click()

def SendToModel(text):
	global Speak
	global SendTimes
	global VA1
	global VA2
	global Field
	print(Speak[0])
	URL = "https://hf.space/embed/KLeedrug/EMO_AI_alpha/+/api/predict"
	body = {"data":[text]}
	bodyheaders={
	'content-type': 'application/json'
	}
	returnbody = {"data":[0.125,0.567],"duration":0.123,"average_duration":0.234}
	jsonData=requests.post(URL,headers=bodyheaders,data=json.dumps(body)).json()
	Speak[0] = jsonData["data"][0]
	Speak[1] = jsonData["data"][1]
	if SendTimes>=1:
		SendtoLoop()
	else:
		#做事
		VA1[0] = Speak[0]*0.01 
		VA1[1] = Speak[1]*0.01 
		VA2[0] = Speak[0]*0.01 
		VA2[1] = Speak[1]*0.01 
		Field[0] = Speak[0]*0.1 
		Field[1] = Speak[1]*0.1 
	SendTimes+=1
	#return jsonData["data"]

def SendtoLoop():
	global Speak
	global VA1
	global VA2
	global Field
	#loopURL = "https://hf.space/embed/KLeedrug/EMO_AI_SECRET_WEAPON/+/api/predict"
	loopURL = "https://hf.space/embed/KLeedrug/EMO_AI_EXPERIMENTAL_WEAPON/+/api/predict"
	loopbody = {"data":[Speak[0],Speak[1],VA1[0],VA1[1],VA2[0],VA2[1],Field[0],Field[1]]}
	bodyheaders={
	'content-type': 'application/json'
	}
	loopreturnbody = {"data":[0.125,0.567,0.123,0.546,0.567,0.995],"duration":0.123,"average_duration":0.234}
	loopjsonData=requests.post(loopURL,headers=bodyheaders,data=json.dumps(loopbody)).json()
	VA1[0] = loopjsonData["data"][0]
	VA1[1] = loopjsonData["data"][1]
	VA2[0] = loopjsonData["data"][2]
	VA2[1] = loopjsonData["data"][3]
	Field[0] = loopjsonData["data"][4]
	Field[1] = loopjsonData["data"][5]
	return loopjsonData["data"]

def CheckIfLogged():
	driver.get('https://www.facebook.com')
	try:
		driver.find_element(By.CSS_SELECTOR,"[aria-label='你的個人檔案']")
	except NoSuchElementException:
		print("這個東西不存在")
		return False
	return True

@app.route('/',methods=('GET','POST'))
def index():
	if request.method == 'POST':
		usrwrd = request.form['FB_usr']
		passwrd = request.form['pass']
		login_FB(usrwrd,passwrd)
		return redirect(url_for('loggedin'))
	if request.method == 'GET':
		Islogged = CheckIfLogged()
		if Islogged == True:
			driver.find_element(By.CSS_SELECTOR,"[aria-label='你的個人檔案']").click()
			sleep(1)
			driver.find_element(By.XPATH,"//span[text()='登出']").click()
	return render_template('index.html')

@app.route('/loggedin', methods=('GET','POST'))
def loggedin():
	global CurrentPerson
	if request.method == 'POST':
		CurrentPerson = request.form['person']
		if not CurrentPerson:
			flash('請輸入一個對話對象的名稱！請注意，必須完全符合他的對話名稱！')
		else:
			print(CurrentPerson)
			Search_Person(CurrentPerson)
			return redirect(url_for('chatroom'))
	return render_template('loggedin.html')

@app.route('/chatroom', methods=('GET','POST'))
def chatroom():
	global CurrentPerson
	global RecievedChange
	global Speak
	global VA1
	global VA2
	global Field
	if request.method == 'GET':
		print("成功進入ChatRoom")
		#ThePerson=request.args['theperson']
		thelist = DisplayMessages(CurrentPerson)
		#thelist.remove(['',''])
		messagelist = [""]*len(thelist)
		for i in range(len(thelist)):
			messagelist[i]=thelist[i][0]+":"+thelist[i][1]
		SendToModel(thelist[-1][1])

	if request.method =='POST':
		newmessage = request.form['newmessage']
		SendChatRoom(newmessage)
		sleep(1)
		thelist = DisplayMessages(CurrentPerson)
		#thelist.remove(['',''])
		messagelist = [""]*len(thelist)
		for i in range(len(thelist)):
			messagelist[i]=thelist[i][0]+":"+thelist[i][1]
		SendToModel(thelist[-1][1])
	#CheckUpdate(request.args['theperson'])
	CheckUpdate(CurrentPerson)
	return render_template('chatroom.html', messagelist = messagelist, emotion = [Speak,VA1,VA2,Field], renewbool = RecievedChange)

@socketio.on('connect')
def Connect():
	print("連結成功了By App")

@socketio.on('CheckIfUpdated')
def CheckThat():
	global RecievedChange
	global Speak
	global VA1
	global VA2
	global Field
	CheckUpdate(CurrentPerson)
	if RecievedChange == True:
		thelist = DisplayMessages(CurrentPerson)
		#thelist.remove(['',''])
		messagelist = [""]*len(thelist)
		for i in range(len(thelist)):
			messagelist[i]=thelist[i][0]+":"+thelist[i][1]
		SendToModel(thelist[-1][1])
		SendtoLoop()
		socketio.emit('DialogChanged',{"data":messagelist,"emotion":[Speak,VA1,VA2,Field]})

@socketio.on('emitnewmessage')
def EmitNewText(data):
	SendChatRoom(data);

if __name__ == '__main__':
    #app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
	#scheduler = APScheduler()
	#scheduler.add_job(func=CheckUpdate,args = [CurrentPerson], trigger = 'interval',id = 'test', seconds = 5)
	#scheduler.start()
	#app.run()
	socketio.run(app, debug=True, host='127.0.0.1', port=5000)