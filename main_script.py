# # #main script
# # # Admin log in page
Company_name = input("Input your Company Name ! ")
print(Company_name.upper())

def Admin_login(fname):
    """
    this function gets the name of the user and checks if the users name is a registered admin.
    If yes, it will print a welcome message and a the users Admin number
    if no, it will an erroe message, telling the user that he/she must be register admin to log in

    Arg: fname
     
    returns fname
    """
    admin_names = {"Victor":1, "Marvel":2, "Mercy":3}
    if fname in admin_names:
        return f"Welcome dear {fname}, Admin no: " + str(admin_names[fname])

    
    return fname +" you must be an Admin to log in !"


first_name = str(input("Please Enter your Admin name to login: "))
print(Admin_login(first_name))



#getting the items
Grocery_list = {}
x = 1
while True:
    try:
        items = str(input(f"Enter the item bought {x}: "))
        if items == "Done":
            break

        prices = float(input(f"Enter the price of {items} {x}: "))

        qauntity = int(input(f"Enter quantity of {items} {x}: "))
        x = x+1

        if items not in Grocery_list:
            Grocery_list[items] =prices*qauntity
    except Exception as e:
        print(f"you must enter a number for prices and quantity and words for items !")



#final results
Company_list_summary  =f"~{Company_name.upper()} purchase list ~"
print (Company_list_summary)
print("==================================================")
details = {
    "contact":"Uyo, Oron Road", "phone no":"09121368136", "Email":f"{Company_name}@gmail.com",
    "Customer_care":"09121368136" }
for info, about in details.items():
    print(info.upper()+" : "+about,end = "   ")
    pass
print(' ', end = "\n")
print(" ")

Ticket = f"purchase ID:kxxi{x}8d3{x}{x+1}831d"
Date = "Date: 09-05-2023"
Captions = ["QNT", "ITEM", "PRICE", "AMOUNT"]
print(Ticket,Date, sep = "   ")
total = float()
no = 1

# getting the data from the dictionary and summing them 
for items, Prices in Grocery_list.items():
    print(f"{no}. " + items.upper() + "        =  " +"N "+str(Prices))
    no += 1
    total+= float(Prices)

#value added tax
total_vat = total - 4.4
vat = 2.1
consumption_tax = 1.3

#total Arrangements
print("                  ===========")
print("SUB TOTAL      = ",total_vat)
print(f"VAT               {vat}")
print(f"consumption tax   {consumption_tax}           ")
print("                  ===========")
print(F"TOTAL          =  {total}")
print("                  ===========")
admin = f'Admin: {first_name}'
print("Thank you for purchasing with us ! ", " ", "Outstanding Service Everytime !", " ",admin," ",sep = "\n")
