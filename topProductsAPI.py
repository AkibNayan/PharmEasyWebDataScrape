import requests
import pandas as pd
import math

page = 1
data = []
while True:
  res = requests.get(
      f"https://pharmeasy.in/api/otc/getCategoryProducts?categoryId=9297&page={page}")
  response = res.json()
  totalProd = len(response["data"]["products"])
  if totalProd == 0:
    break
  for i in range(0, totalProd):
    try:
      name = response["data"]["products"][i]["name"]
    except:
      name = "Not Available"
    try:
      manufacturer = response["data"]["products"][i]["manufacturer"]
    except:
      manufacturer = "Not Available"
    try:
      mrpDecimal = response["data"]["products"][i]["mrpDecimal"]
    except:
      mrpDecimal = "Not Available"
    try:
      salePriceDecimal = response["data"]["products"][i]["salePriceDecimal"]
    except:
      salePriceDecimal = "Not Available"
    try:
      discountPercent = response["data"]["products"][i]["discountPercent"]
    except:
      discountPercent = "Not Available"
    try:
      totalRating = response["data"]["products"][i]["ratingDetails"]["count"]
    except:
      totalRating = "Not Available"
    try:
      avgRating = response["data"]["products"][i]["ratingDetails"]["value"]
      avgRating = math.trunc(avgRating)
    except:
      avgRating = "Not Available"
    try:
      maxQuantity = response["data"]["products"][i]["maxQuantity"]
    except:
      maxQuantity = "Not Available"
    try:
      minQuantity = response["data"]["products"][i]["minQuantity"]
    except:
      minQuantity = "Not Available"
    try:
      isAvailable = response["data"]["products"][i]["isAvailable"]
    except:
      isAvailable = "Not Available"
    dict_ = {
        "name": name,
        "manufacturer": manufacturer,
        "mrpDecimal": mrpDecimal,
        "salePriceDecimal": salePriceDecimal,
        "discountPercent": discountPercent,
        "totalRating": totalRating,
        "avgRating": avgRating,
        "maxQuantity": maxQuantity,
        "minQuantity": minQuantity,
        "isAvailable": isAvailable
    }
    data.append(dict_)
  page += 1

"""df = pd.DataFrame(data)
df.to_csv("topProductsAPIdata.csv", index=False)"""

print(data)