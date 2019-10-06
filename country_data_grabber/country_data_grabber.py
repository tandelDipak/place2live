import pandas as pd
import os


def getCSVsAsList():
    fileList = []
    # CSVs to skip because country name is not a PK
    csvSkipList=[
        "university_rankings.csv",
        "traffic_index.csv"
    ]
    for root, dirs, files in os.walk(".."):
        for name in files:
            if name.find(".csv") != -1 and not(any(f in name for f in csvSkipList)):
                fileList.append(root + "\\" + name)

    return fileList


def findIndexOfElementInList(list, elements):
    for i in range(len(list)):
        e = list[i]
        for element in elements:
            if str(e).lower() == str(element).lower():
                return i


def grabData(countryName):
    CSVs = getCSVsAsList()
    df = pd.DataFrame()
    for CSV in CSVs:
        print(CSV)
        data = pd.read_csv(CSV)
        # column names used to describe the country names
        columnNames = ["country", "name"]
        country_col_index = findIndexOfElementInList(list(data.columns.values), columnNames)
        colName = data.columns[country_col_index]
        whereCountry = data[colName].str.lower() == countryName.lower()
        data = data.where(whereCountry).dropna()

        if df.empty:
            df = data
            key = colName
        else:
            df = df.join(data.set_index([colName], verify_integrity=True),
                         on=[key], how='left')

    return(df)

grabData("france")
