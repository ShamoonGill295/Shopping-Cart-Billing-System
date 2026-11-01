name  = input("enter your name: ")
age = int(input("enter your age: "))
city = input("enter your city: ")
cus_id = input("enter your customer Id: ")

price_per_item= {
    "milk": 200,
    "toothpaste": 100,
    "bread": 150,
    "suger": 80,
    "cold drink":180,
    "basan": 150,
    "rice" : 400,
    "maggie": 50
}
avail_prods =["milk" , "toothpaste" , "bread" ,"suger" , "cold drink" , "basan" , "rice","maggie" ]

print("Available Products are................: ",avail_prods)

total_amount = 0
change = 0
for prod in range(1,6):
    print("product no ",prod)
    prod_name = input("enter your product name: ")
    if prod_name in avail_prods:
        print("product is available")
    else:
         print("product is not available")    
         continue
    prod_quantity = int(input("enter your product quantity: "))
    print("product quantity : ",prod_quantity)
    
    price = price_per_item[prod_name]
    print("your products price is :",price)
    
    total_amount = prod_quantity * price
    total_amount = total_amount + total_amount
dis_amount = 0
if total_amount >= 10000:
    dis =("you got 15% Discount")
    print(dis)
    dis_perc = 15
    dis_amount = total_amount * dis_perc/100
    discounted_bill = total_amount - dis_amount
elif total_amount >= 5000:
    dis =("you got 10% Discount")
    print(dis)
    dis_perc = 10
    dis_amount = total_amount * dis_perc/100
    discounted_bill = total_amount - dis_amount
elif total_amount >= 2000:
     dis =("you got 5% Discount")
     print(dis)
     dis_perc = 5
     dis_amount = total_amount * dis_perc/100
     discounted_bill = total_amount - dis_amount
else:
    dis_amount = 0
    dis_bill = total_amount
    print("no discount.....shop more than 2000 for discount !")

if age >= 60 :
    print("you got 5% more discount")
    more_disc_perc = 5
    more_disc = discounted_bill*more_disc_perc/100
    senior_discount = discounted_bill - more_disc 
else:
    senior_discount = discounted_bill
    more_disc = 0

pay_method = input("payment from CARD / CASH ? ")
if pay_method == "card":
    charge = ("2% Service charges are applied")
    print(charge)
    ser = 2
    service_charge = senior_discount * 2/100
    final_payment = senior_discount + service_charge
elif pay_method == "cash":
        service_charge = 0
        final_payment = senior_discount
        print("no charges ")
else:
   print("invalid payment method")
   final_payment = senior_discount
paid = int(input("how many cash do you paid ? "))
if final_payment > paid :
    insufficient = print("unsufficient payment !")
elif final_payment == paid:
    suc = print("payment successful")
elif final_payment < paid:
    change = paid - final_payment
    print("return amount: ",change)

if total_amount >= 10000 :
    catogry = ("Premium customer")
    print(catogry)
elif total_amount >= 5000 :
    catogry = ("Gold Customer")
    print(catogry)
elif total_amount >= 2000 :
    catogry = ("Silver Customer")
    print(catogry)
elif total_amount < 2000 :
    catogry = ("Regular Customer")
    print(catogry)

final_report = {
        "customer_info" :{
                "name" : name,
                "age" : age,
                "city": city,
                "customer ID" : cus_id
        },
        "products" :{
                "products" : prod_name,
                "product quantity" : prod_quantity,
                "product price" : price_per_item,
                "subtotal" : total_amount
        },
        "billing" : {
                "payment method" : pay_method,
                "total" : discounted_bill,
                "normal discount" : dis_amount,
                "senior discount" : more_disc,
                "service charge" : service_charge,
                "final payment" : final_payment,
                "change" : change,
                "customer status" : catogry
            },
        }




