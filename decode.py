# decoding algorithm
import os
print(": use the magic key to exit : ")
l,z=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],""
result,e = "",""
search = False
k = int(input("key(max:52) >> "))
if(k == 0 or k == 00): search = True
while(True and not search):
	try:
		d=input("\ndata(en) >> ")
		e+=d+" "
		if(d == ":wq"): f = open("result.txt","w");f.write(z);f.close();print("saved");exit()
		if(d == ":ck"): k = int(input("key(max:52) >> "));continue
		for c in d:z+=l[len(l)+(l.index(c)-k) if l.index(c)-k<0 else l.index(c)-k]
	except:
		quit("error\n")
	print("\n--> "+z+"\n")
	z += " "
	os.system("clear")
	print(f"key >> {k}")
	print(f"entry >> {e}")
	print(f"data >> {z}")
f.close()

if(search):
	k=str(k)
	d=input("\ndata(en) >> ")
	for k in range(len(l)+1):
		for c in d:z+=l[len(l)+(l.index(c)-k) if l.index(c)-k<0 else l.index(c)-k]
		v = (z[::-1] if k=="00" else z)
		print(f"key : {k}, data : ",v )
		z = ""
