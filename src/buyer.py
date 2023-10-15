import pandas as pd

def clean_data(data):
    # removes unneeded columns
    for _ in range(3):
        data.drop(data.columns[0], axis=1, inplace=True)
    data.to_csv("output/Buyer.csv", index=False)

def quantify(data, LEN):
    items = {}

    # adds items to dictionary and strips number from beginning of item name
    for i in range(LEN):
        item = data.loc[i]
        if item["choiceName"][0].isnumeric():
            count = int(item["choiceName"][0])
            data.loc[i, "choiceName"] = item["choiceName"][2:]
            data.loc[i, "quantity"] = count * item["quantity"]

    # combines duplicate items + adds their quantities to store in dictionary
    for i in range(LEN):
        item = data.loc[i]
        if items.get(item["choiceName"]) is not None:
            items[item["choiceName"]][1] += item["quantity"]
        else:
            items[item["choiceName"]] = [item["choiceCost"], item["quantity"]]

    # wipes old data (since it exists in items dictionary)
    data = pd.DataFrame(columns=["Item", "Price", "Quantity", "Total"])

    # adds title value for each row    
    for i in items:
        data.loc[len(data)] = [i, items[i][0], items[i][1], f"${format(float(items[i][0][1:]) * items[i][1], '.2f')}"]

    data.to_csv("output/Buyer.csv", index=False)


def buyer(data, LEN):
    clean_data(data)
    quantify(data, LEN)
    print("Check out Buyer.csv for the results!")