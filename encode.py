# encoding algorithm
l,z=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],""
try:
	d,k=input("\ndata(en[a~z]) >> "),int(input("key >> "))
	for c in d:z+=l[(l.index(c)+k)%26 if l.index(c)+k>25 else l.index(c)+k]
except:
	quit("error\n")
print("\n--> "+z+"\n")
input("enter for exit\n")
