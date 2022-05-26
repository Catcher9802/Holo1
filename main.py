import requests
import random
import os,time

os.system('clear')

print("สมัครสมาชิก Catcher")
print("")
user = input("ชื่อผู้ใช้ : ")
password = input("รหัสผ่าน : ")
password_two = input("ยืนยันรหัสผ่าน : ")
if (password == "" or password_two == ""):
	print("")
	print("รหัสผ่านไม่ถูกต้อง !")
elif (password_two == password):
	num = str(random.randint(1000,9999))
	email = input("อีเมล : ")
	requests.post("https://mail.google.com/mail/u/0/s/?v=or&ik=de5cb35406&at=AF6bupOpYnaPcrkam6IwbptIb3evr_HZyA&subui=android&wjt=p&orwas=1&cfact=7694&suim=true&wasmp=963&ui=savannah&hl=th&ts=1653583484748",headers={"content-type": "application/x-www-form-urlencoded;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","referer": "https://mail.google.com/mail/mu/mp/963/","cookie": "GM_IMP=sp-ca-etresp-cnt-1%2Fsp-brb-ar-1%2Fmc-ht-1%2Ftl-ar-1%2Fsp-smms-b-1%2Fspn-br-qm-cnt-26%2Fspn-ql-cnt-2%2Fspn-brb-c-cnt-607%2Fspn-cl-cnt-604%2Fspn-mth0-10000000%2Fspn-muh0-10000000%2Fsp-upload-apm-0%2Fspn-ql-cnt-289%2Fspn-brb-c-cnt-1256%2Fspn-cl-cnt-1252%2Fspn-br-qm-cnt-35%2Fspn-ql-cnt-50%2Fspn-brb-c-cnt-1017%2Fspn-cl-cnt-1014;COMPASS=gmail=CooBAAlriVc1dHGCp5YJlaYZjFpzdqO9rljJTRYJ-S8VO0aVQXCzydgjejpGdtUJWUCsyUfBz-i9424q3zM4hxuMvFbyy4KQsKEZgYR1d40GxAxgGwNZLw8-f3-T-vAJJraGIV1-vyjfb-ZrJwKEIIQRhzCYEAE9iWVxQ7sZ9cbQcXn71QMfm_qtluWuEJn4vpQGGpwBAAlriVeZQIuj_eMP7594sUKnou8xG50CBs-vzVoipR81wWu1Z5i9MU-6dbaR0dcFZue1amDJTfA-sfrpWxIE_jPDVPJzlMMxOFbfX_jFrXeJSDF4JkPRoLtaCC1KQ1G_UJzAZ7EiAeqU72J7WZRRJVBGsygMemYvM5dt6he3FvpngRjPD98ST4LYc_Ev4EgHyHRIIiKh5ff3qZit;GX=DUMMY;WML=1653583409511#yamasuy55@gmail.com:963:0;SEARCH_SAMESITE=CgQIvpUB;AEC=AakniGMt5joXbhAYubtCOUC3BTTaGBxdfJ1_0shSIjyfg5aoPshyK30qwl0;SID=KQi9lzz00LRvEN_47ZcEKgfgLpK0qSfwegJFbD3NnBGBBMccvbHEqsNHcztyXUS9jtwziw.;__Secure-1PSID=KQi9lzz00LRvEN_47ZcEKgfgLpK0qSfwegJFbD3NnBGBBMccSp9vY8dGGSB4N8I1CYc5Pw.;__Secure-3PSID=KQi9lzz00LRvEN_47ZcEKgfgLpK0qSfwegJFbD3NnBGBBMccSDIhilfj4a5WtmBYJsMLng.;HSID=AO1Adc_4mov6UG0dO;SSID=Ax7Qlw_zV-G_nGj15;APISID=jgrIJsqUeMe98KDR/AeRKfby3e-knYu9f2;SAPISID=65LximrpWDKTZgdd/A2gENSfZj-QsQEg8p;__Secure-1PAPISID=65LximrpWDKTZgdd/A2gENSfZj-QsQEg8p;__Secure-3PAPISID=65LximrpWDKTZgdd/A2gENSfZj-QsQEg8p;NID=511=VenM_5Xd50ExiD9_CfmfEoYBsnFUIuRxCK2xRZqdCi8_R6pYSsWombn8ChsvIpKlSaOP4kasThHfrhHAaNfuSnsJ9838VgsXP9XQ5XmmUVEgghw26tmRh9S_6Pokf38sXHcWJf9DnEvby8nET17hnrScRlaO38d3dk9qWGtnKmeUcGHDe3C9hYQxRzU14GKrD_9tnMPuqGFlchV3uz8pcP1Soeen607_kWCUDLxqiUajxUaHoXFXJ2ZR;1P_JAR=2022-05-26-16;OSID=KQi9l6h_th0DTG4ZiD6IqwCtvJ-CGjDsD1ZOROU5G21sxiWOMFEHNWbHuiqReomkzfsU_Q.;__Secure-OSID=KQi9l6h_th0DTG4ZiD6IqwCtvJ-CGjDsD1ZOROU5G21sxiWOpuq0xG7GqLe5-wQOnZLMEQ.;SIDCC=AJi4QfHJ4avFb0KLnzUJojeYEsODz3HxiMaX59vTO23kV12_z_K2Oy-m1oE2WE2h7-e8HO4H8Kw;__Secure-3PSIDCC=AJi4QfGuBambFi2qscZpL7UMNP6ZYSNrCBp1sdsrcBM0n1S_lInphed-Pg1AuT6H138LPumdtik"},data=f"s_jr=%5Bnull%2C%5B%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5Bnull%2C%5Bnull%2C%5B%5Bnull%2C%22{email}%22%2C%22%22%2Cnull%5D%5D%2C%5B%5D%2C%5B%5D%2C%5Bnull%2C%22yamasuy55%40gmail.com%22%2Cnull%2Cnull%5D%2C%5B%5D%2C%22%5Cu0e2a%5Cu0e21%5Cu0e31%5Cu0e04%5Cu0e23%5Cu0e2a%5Cu0e21%5Cu0e32%5Cu0e0a%5Cu0e34%5Cu0e01%20Catcher%22%2C%22%5Cu0e01%5Cu0e23%5Cu0e38%5Cu0e13%5Cu0e32%5Cu0e22%5Cu0e37%5Cu0e19%5Cu0e22%5Cu0e31%5Cu0e19%5Cu0e01%5Cu0e32%5Cu0e23%5Cu0e2a%5Cu0e21%5Cu0e31%5Cu0e04%5Cu0e23%5Cu0e2a%5Cu0e21%5Cu0e32%5Cu0e0a%5Cu0e34%5Cu0e01%5Cu0e02%5Cu0e2d%5Cu0e07%5Cu0e04%5Cu0e38%5Cu0e13%5Cu0e42%5Cu0e14%5Cu0e22%5Cu0e43%5Cu0e0a%5Cu0e49%5Cu0e02%5Cu0e49%5Cu0e2d%5Cu0e21%5Cu0e39%5Cu0e25%20OTP%3D{num}%20Ref%3DYZIt%22%2C1%2Cnull%2Cnull%2Cnull%2Ctrue%2Cnull%2C%22byueir90179t%22%2Cfalse%2C%5B%5D%5D%2Cnull%5D%5D%5D%2C2%2Cnull%2Cnull%2Cnull%2C%22de5cb35406%22%5D")
	print("")
	otp = input("กรุณากรอกรหัส OTP จากอีเมล : ")
	if (otp == num):
		print("")
		print("_____________________5 วินาที__________________")
		time.sleep(4)
		os.system("clear")
		print("ข้อมูลสมาชิก")
		print(f"Username : {user}")
		print(f"Email    : {email}")
		print("")
		print("     Discord Servers")
		print("")
		print("Servers : Rose Catcher")
		print("› https://discord.gg/aQghUv4qWF")
		print("")
		print("Servers : EH4404")
		print("› https://discord.gg/PGNaGNcFTh")
		print("")
		print("Servers : HG.WORKSHOP")
		print("› https://discord.gg/8CyZhYq9Ce")
		print("")
		print("Servers : HG.HIGHGOD")
		print("› https://discord.gg/rVpRdAXQ7J")
		print("")
		print("Servers : RabbitSQ - Community")
		print("› https://discord.gg/n2AZww3gAt")
		print("")
		print("Servers : CYBER SAFE")
		print("› https://discord.gg/dsPp5ZpUvr")
	elif (otp == ""):
		print("")
		print("""{"error": code not found,"code": 504,"message": "an error occurred"}""")
	else:
		print("")
		print("""{"error": code not found,"code": 1020,"message": "wrong"}""")
else:
	print("")
	print("รหัสผ่านไม่ตรงกัน !")