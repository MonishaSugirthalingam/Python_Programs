costomers=int(input())
category=input()
cv2={}
cf2={}
cv1={}
cf1={}
common_veg={}
common_fru={}
common_List=[]
count1=count2=count3=count4=0
for i in range(costomers):
    if category=="Vegitables":
        while True:
            v=input()
            if v=="Fruits":
                break
            cost=float(input())
            cv2[v]=cost
       
        if i==0:
            cv1=cv2.copy()
            cv2.clear()
        if v=="Fruits":
            while True:
                f=input()
                if f=="Vegitables":
                    break
                cost=float(input())
                cf2[f]=cost
                if i==1 and cost==0.75:
                    break
            if i==0:
                cf1=cf2.copy()
                cf2.clear()
v1=list(cv1.keys())
v2=list(cv2.keys())
for veg in v1:
    if veg in v2:
        a=cv1.get(veg)
        b=cv2.get(veg)
        c=a+b
        common_veg[veg]=c
        common_List.append(veg)
        count1=count1+a
        count2=count2+b
        v1.remove(veg)
        v2.remove(veg)
for veg in v1:
    c=cv1.get(veg)
    common_veg[veg]=c
for veg in v2:
    c=cv2.get(veg)
    common_veg[veg]=c
f1=list(cf1.keys())
f2=list(cf2.keys())
for fru in f1:
    if fru in f2:
        x=cf1.get(fru)
        y=cf2.get(fru)
        z=x+y
        common_fru[fru]=z
        common_List.append(fru)
        count3=count3+x
        count4=count4+y
        f1.remove(fru)
        f2.remove(fru)
for fru in f1:
    z=cf1.get(fru)
    common_fru[fru]=z
for fru in f2:
    z=cf2.get(fru)
    common_fru[fru]=z
total_quantity1=count1+count3
total_quantity2=count2+count4
print("Total Quantity Sold under Vegitables")
print(set(common_veg.items()))
print("Total Quantity Sold under fruits")
print(set(common_fru.items()))
print("List of common items are",common_List)
if total_quantity1>total_quantity2:
    print("Customer 1 is the lucky winner")
else:
    print("Customer 2 is the lucky winner")
