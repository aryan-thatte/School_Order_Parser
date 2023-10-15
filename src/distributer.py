import pandas as pd


def clean_data(data):
    # removing unneeded columns
    for _ in range(11):
        data.drop(data.columns[0], axis=1, inplace=True)
    data.drop(data.columns[1], axis=1, inplace=True)
    for _ in range(10):
        data.drop(data.columns[2], axis=1, inplace=True)
    data.drop(data.columns[3], axis=1, inplace=True)
    data.drop(data.columns[3], axis=1, inplace=True)

    # rename HomeroomName to Homeroom
    data.rename(columns={"HomeroomName": "Homeroom"}, inplace=True)

    data.to_csv("output/Teacher.csv", index=False)


def separate_first_last_names(data, LEN):
    # adding Last Name and First Name columns
    data.insert(0, "Last Name", "")
    data.insert(1, "First Name", "")

    # taking Student Name and inputting it into Last Name and First Name columns
    for i in range(LEN):
        name = data.loc[i, "Student Name"]
        name = name.split()
        name[0] = name[0].replace(",", "")
        data.loc[i, "Last Name"] = name[0]
        data.loc[i, "First Name"] = name[1]

    # removing Student Name column
    data.drop("Student Name", axis=1, inplace=True)
    data.to_csv("output/Teacher.csv", index=False)


def sort_by_homeroom(data):
    data.sort_values("Homeroom", axis=0, ascending=True, inplace=True)
    data.to_csv("output/Teacher.csv", index=False)


def distributer(data, LEN):
    clean_data(data)
    separate_first_last_names(data, LEN)
    sort_by_homeroom(data)
    print("Check out Teacher.csv for the results!")
