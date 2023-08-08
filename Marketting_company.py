s={"Chennai","Bengaluru","Kolkata","Ahmedabath","Pune","Hydrabad","Jaipur","New Delhi","Lucknow","Surat"}
s1=set()
Company_one=int(input("How many cities company_one had visited"))
Company_two=int(input("How many cities company_two had visited"))
Company_three=int(input("How many cities company_three had visited"))
for i in range(Company_one):
    Name_of_the_cities=input("Enter the name of the cities  which are company_one had visited")
    s1.add( Name_of_the_cities)
    s.remove( Name_of_the_cities)
for i in range(Company_two):
    Name_of_the_cities=input("Enter the name of the cities which are company_two had visited")
    s1.add( Name_of_the_cities)
    s.remove( Name_of_the_cities)
for i in range(Company_three):
    Name_of_the_cities=input("Enter the name  name of the cities which are company_one had visited")
    s1.add( Name_of_the_cities)
    s.remove( Name_of_the_cities)
print("Already visited cities")
print(s1)
print("Yet to be visited cities")
print(s)
