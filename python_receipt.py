productlist =[]
pricelist=[]
qtylist=[]
totallist=[]

staffname= input("Enter your staff name: ")
staffID= input("Enter your staff ID: ")

print(f"Welcome {staffID}_{staffname}")

while True:
    productInput = input("Product name:")
    priceInput = float(input("Product price: "))
    qtyInput = int(input("Product quantity: "))

    productlist.append(productInput)
    pricelist.append(priceInput)
    qtylist.append(qtyInput)
    totallist.append( priceInput * qtyInput )

    cmd = input("enter another list? [y/n]: ")
    if (cmd == "n"):
        break

overallprice = sum(totallist)
eachprice = (totallist)
listamount = len(productlist)
average = overallprice / sum(qtylist)
maxValue = max(pricelist)
minValue = min(pricelist)

indexMin = pricelist.index(minValue)
indexMax = pricelist.index(macValue))
nameMin = productlist[indexMin]
nameMax = productlist[indexMax]

print(f"The overall price is: {overallprice}")
print(f"The price for each product are: {totallist}")
print(f"The amount of lists made are: {listamount}")
print(f"The average price is: {average}")
print(f"The most expensive price is: {macValue}_{nameMax}")
print(f"The most cheapest price is: {minValue}_{name_Min}")
