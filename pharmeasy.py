import requests as re
import pandas as pd
page = 1
data = []
while True:
    url = f"https://pharmeasy.in/api/otc/getCategoryProducts?categoryId=145&page={page}"
    res = re.get(url)
    response = res.json()
    totalProducts = len(response['data']['products'])
    if totalProducts != 0:
        for i in range(totalProducts):
            try:
                title = response['data']['products'][i]["name"]
                mrp = response['data']['products'][i]["mrpDecimal"]
                salesPrice = response['data']['products'][i]["salePriceDecimal"]
                discount = response['data']['products'][i]["discountDecimal"]
                discountPercent = response['data']['products'][i]["discountPercent"]
            except:
                title = "Not Available"
                mrp = "Not Available"
                salesPrice = "Not Available"
                discount = "Not Available"
                discountPercent = "Not Available"
            dict = {
                "title" : title,
                "mrp" : mrp,
                "salesPrice" : salesPrice,
                "discount" : discount,
                "discountPercent" : discountPercent 
            }
            data.append(dict)
    else:
        break
    page += 1
df = pd.DataFrame(data)
df.to_csv("PharmEasy Diabetic Care Data", index=False)