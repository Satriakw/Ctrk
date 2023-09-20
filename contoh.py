import os,sys,requests
os.system("clear")
os.system("figlet Spam WhatsApp\n")
nomor = input("Nomor (8×××):")
api=requests.post("https://flask-production-9752.up.railway.app/api/spam",data={"nomor":nomor})
print (api)
