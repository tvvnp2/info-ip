from ast import Try
from email import header
import requests
from time import sleep
# Bold
BBlack="\033[1;30m"       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White

print(f'''{BRed}
     ____                      ,
    /---.'.__             ____//
         '--.\           /.---'
    _______  \\         //
   /.------.\  \|      .'/  ______
  //  ___  \ \ ||/|\  //  _/_----.\__
|/  /.-.\  \ \:|< >|// _/.'..\   '--
   //   \'. | \'.|.'/ /_/ /  \\
  //     \ \_\/" ' ~\-'.-'    \\
 //       '-._| :H: |'-.__     \\
//           (/'==='\)'-._\     ||
||                        \\    \|
||                         \\    '
|/                          \\
                             ||
                             ||
                             \\
                              ' 
instagram : https://instagram.com/fx_py3?igshid=YzAyZWRlMzg=
telegram :  https://t.me/tvvnu
{BYellow}[1] - {BCyan}   [ iphone ]                                                                                                                                                                                                                
{BYellow}[2] - {BCyan}   [ other ] 
''')
try:
	c=int(input(f'{BYellow}[+]{BCyan} - Choose : '))
except :
	print('قلنا اختار 1 او 2 بلا عبط')
	exit()
def iphone(ip):
	print('=========START=========')
	url=f'https://demo.ip-api.com/json/{ip}?fields=66842623&lang=en'
	headers={
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9',
	'Connection': 'keep-alive',
	'Host': 'demo.ip-api.com',
	'Origin': 'https://ip-api.com',
	'Referer': 'https://ip-api.com/',
	'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': "Windows",
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'same-site',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
	 }
	
	req=requests.post(url,headers=headers)
	
	print(f'[+] - status : '+req.json()['status'])
	sleep(0.2)
	print(f'[+] - continent : '+req.json()['continent'])
	sleep(0.2)
	print('[+] - continentCode : '+req.json()['continentCode'])
	sleep(0.2)
	print('[+] - country : '+req.json()['country'])
	sleep(0.2)
	print('[+] - countryCode : '+req.json()['countryCode'])
	sleep(0.2)
	print('[+] - region : '+req.json()['region'])
	sleep(0.2)
	print('[+] - regionName : '+req.json()['regionName'])
	sleep(0.2)
	print('[+] - city : '+req.json()['city'])
	sleep(0.2)
	print('[+] - district : '+req.json()['district'])
	sleep(0.2)
	print('[+] - zip : '+req.json()['zip'])
	sleep(0.2)
	print('[+] - timezone : '+req.json()['timezone'])
	sleep(0.2)
	print('[+] - currency : '+req.json()['currency'])
	sleep(0.2)
	print('[+] - isp : '+req.json()['isp'])
	sleep(0.2)
	print('[+] - as : '+req.json()['as'])
	sleep(0.2)
	print('[+] - asname : '+req.json()['asname'])
	sleep(0.2)
	print('[+] - query : '+req.json()['query'])
	sleep(0.2)
	print('[+] - lat : '+str(req.json()['lat']))
	sleep(0.2)
	print('[+] - lon : '+str(req.json()['lon']))
	sleep(0.2)
	print('[+] - offset : '+str(req.json()['offset']))
	sleep(0.2)
	print('[+] - mobile : '+str(req.json()['mobile']))
	sleep(0.2)
	print('[+] - proxy : '+str(req.json()['proxy']))
	sleep(0.2)
	print('[+] - hosting : '+str(req.json()['hosting']))
	sleep(0.2)
	
	
	
	
	
	
	url1=f'https://ipwhois.pro/{ip}?key=Sxd2AkU2ZL0YtkSR&security=1&lang=en'
	headers1={
	    'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9',
	'Connection': 'keep-alive',
	'Host': 'ipwhois.pro',
	'Origin': 'https://ipwhois.io',
	'Referer': 'https://ipwhois.io/',
	'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': "Windows",
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'cross-site',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36ed-with'
	
	}
	req1=requests.get(url1,headers=headers1)
	
	print('[+] - calling_code : +'+str(req1.json()['calling_code']))
	sleep(0.2)
	print('[+] - img country : '+str(req1.json()['flag']['img']))
	sleep(0.2)
	print('[+] - vpn : '+str(req1.json()['security']['vpn']))
	sleep(0.2)
	print('[+] - tor : '+str(req1.json()['security']['tor']))
	sleep(0.2)
	print('[+] - anonymous : '+str(req1.json()['security']['anonymous']))
	sleep(0.2)
	
	
	req3=requests.get(f'https://ipapi.co/{ip}/json/')
	print('[+] - version : '+str(req3.json()['version']))
	sleep(0.2)
	print('[+] - asn : '+str(req3.json()['asn']))
	sleep(0.2)
	print('[+] - Location : '+str(req.json()['lat'])+','+str(req.json()['lon']))
if c == 1 :
	ip=input('[+] - ip : ')
	iphone(ip)




def other(ip):
	
	url=f'https://demo.ip-api.com/json/{ip}?fields=66842623&lang=en'
	headers={
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9',
	'Connection': 'keep-alive',
	'Host': 'demo.ip-api.com',
	'Origin': 'https://ip-api.com',
	'Referer': 'https://ip-api.com/',
	'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': "Windows",
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'same-site',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
	 }
	
	req=requests.post(url,headers=headers)
	try:
		print(f'{BYellow}[+]{BCyan} - status : {BRed} '+req.json()['status'])
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - continent : {BRed} '+req.json()['continent'])
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - continentCode : {BRed}'+req.json()['continentCode'])
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - country : {BRed}'+req.json()['country'])
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - countryCode : {BRed}'+req.json()['countryCode'])
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - region : {BRed} '+req.json()['region'])
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - regionName : {BRed}'+req.json()['regionName'])
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - city : {BRed}'+req.json()['city'])
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - district : {BRed}'+req.json()['district'])
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - zip : {BRed}'+req.json()['zip'])
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - timezone : {BRed}'+req.json()['timezone'])
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - currency : {BRed}'+req.json()['currency'])
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - isp : {BRed}'+req.json()['isp'])
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - as : {BRed}'+req.json()['as'])
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - asname : {BRed}'+req.json()['asname'])
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - query : {BRed}'+req.json()['query'])
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - lat : {BRed}'+str(req.json()['lat']))
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - lon : {BRed}'+str(req.json()['lon']))
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - offset : {BRed}'+str(req.json()['offset']))
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - mobile : {BRed}'+str(req.json()['mobile']))
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - proxy : {BRed}'+str(req.json()['proxy']))
		sleep(0.2)
		print(f'{BYellow}[+]{BCyan} - hosting : {BRed}'+str(req.json()['hosting']))
		sleep(0.2)
	except:
		print('ip not fuond')
		exit()	
	
	
	
	
	
	url1=f'https://ipwhois.pro/{ip}?key=Sxd2AkU2ZL0YtkSR&security=1&lang=en'
	headers1={
	    'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9',
	'Connection': 'keep-alive',
	'Host': 'ipwhois.pro',
	'Origin': 'https://ipwhois.io',
	'Referer': 'https://ipwhois.io/',
	'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': "Windows",
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'cross-site',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36ed-with'
	
	}
	req1=requests.get(url1,headers=headers1)
	
	print(f'{BYellow}[+]{BCyan} - calling_code : {BRed}'+str(req1.json()['calling_code']))
	sleep(0.2)
	print(f'{BYellow}[+]{BCyan} - img country :  {BRed} '+str(req1.json()['flag']['img']))
	sleep(0.2)
	print(f'{BYellow}[+]{BCyan} - vpn : {BRed} '+str(req1.json()['security']['vpn']))
	sleep(0.2)
	print(f'{BYellow}[+]{BCyan} - tor : {BRed} '+str(req1.json()['security']['tor']))
	sleep(0.2)
	print(f'{BYellow}[+]{BCyan} - anonymous : {BRed} '+str(req1.json()['security']['anonymous']))
	sleep(0.2)
	
	
	req3=requests.get(f'https://ipapi.co/{ip}/json/')
	print(f'{BYellow}[+]{BCyan} - version : {BRed} '+str(req3.json()['version']))
	sleep(0.2)
	print(f'{BYellow}[+]{BCyan} - asn : {BRed} '+str(req3.json()['asn']))
	sleep(0.2)
	print(f'{BYellow}[+]{BCyan} - Location : {BRed}'+str(req.json()['lat'])+','+str(req.json()['lon']))
	
if c == 2:
	ip=input(f'{BYellow}[+]{BCyan} - ip : {BRed}')
	print(f'{BYellow}========={BRed}START{BYellow}=========')
	other(ip)
