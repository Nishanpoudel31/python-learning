items_price = {
    "SamsungM11":"500",
    "SamsungM13":"750",
    "SamsungM15":"800",
    "SamsungS2511":"1000",
    "SamsungA25":"45000"
    
}
for k,v in items_price.items():
    print(f"The price of {k} is {v}.")

for v in items_price.values():#This prints values only
    print(v)

vegetables={
    "Cauliflower":"150",
    "Potato":"80",
    "Carrot":"75",
    "Radish":"125",
    "Saag":"220",
    "Tomato":"42",
    "Gourd":"187",
    "Pumpkin":"147"
}

vegetables['masu']=1000
vegetables['khasi']=1500
del vegetables['Saag']
for k,v in vegetables.items():
    print(f"The price of {k} is {v}.")

for k in vegetables.keys():#tHISS PRINT keys only.
    print(k)