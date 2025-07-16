from datetime import datetime
print(20*" ","WELCOME",20*" ")
name=input("enter the name:")
list='''
Rice            50/kg
Sugar           30/kg
Oil             90/kg
Cumin Seeds     300/kg
Coriander       70/kg
Ginger          100/kg
Garlic          90/kg
Mustard Seeds   60/kg
Brush           20/each
Dabur           20/each
Salt            20/kg
Chilli Powder   540/kg
'''
price=0
pricelist=[]
totalprice=0
ilist=[]
qlist=[]
plist=[]
finalamount=0
items={"rice":50,"sugar":30,"oil":90,"cumin seeds":300,
       "coriander":70,"ginger":100,"garlic":90,"mustard seeds":60,
       "brush":20,"dabur":20,"salt":20,'chilli powder':540}
inp=int(input("for list of items press 1:"))
if inp==1:
    print(list)
for i in range(len(items)):
    input1=int(input("If you want to buy press 1 or press 2 for exit:"))
    if input1==2:
        break
    if input1==1:
        item=input("enter the item you want:")
        quant=int(input("enter the quantity you want:"))
        if item in items.keys():
            price=(items[item])*quant
            pricelist.append((item,quant,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quant)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=totalprice+gst
    else:
        print("you entered wrong number")
    inpu=input("Can i bill the items yes or No:")
    if inpu=="yes":
        pass
        if finalamount!=0:
            print(25*"=","D-Mart",25*"=")
            print(28*" ","Ethamukkala",28*" ")
            print("Name:",name,28*" ","date:",datetime.now)
            print(70*"-")
            print("S.No",8*" ","Items",8*" ","Quantity",8*" ","Price")
            for i in range(len(pricelist)):
                print(i,8*" ",ilist[i],8*" ",qlist[i],8*" ",plist[i])
            print(70*"-")
            print(50*" ","TotalAmount:",totalprice)
            print(50*" ","GST Amount",gst)
            print(70*"-")
            print(50*" ","FinalAmount:",finalamount)
            print(70*"-")
            print(50*" ","Thanks for Visiting")
            print(70*"-")
    else:
        break

            












