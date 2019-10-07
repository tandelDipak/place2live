import os

import pandas as pd


def getCSVsAsList():
    """
    get all parsable CSV in project as full path

    :return: string list
    """
    fileList = []
    # CSVs to skip because country name is not a PK
    csvSkipList = [
        "university_rankings.csv",
        "traffic_index.csv",
    ]
    for root, _unuseddirs, files in os.walk(".."):
        for name in files:
            if name.find(".csv") != -1 and not (any(f in name for f in csvSkipList)):
                fileList.append(root + "\\" + name)

    return fileList


def findElementInList(passedList, elements):
    """

    :param passedList: column names of a data frame
    :param elements: elements to look for in the column names
    :return: index of first element found in the data frame column names
    """
    for i, item in enumerate(passedList):
        for element in elements:
            if str(item).lower() == str(element).lower():
                return i


def grabData(countryName):
    """

    :param countryName: country name as string (case insensitive)
    :return: data frame with country data
    """
    CSVs = getCSVsAsList()
    df = pd.DataFrame()
    for CSV in CSVs:
        print(CSV)
        data = pd.read_csv(CSV)
        # column names used to describe the country names
        columnNames = ["country", "name"]
        # column names of the data frame
        dataColumns = list(data.columns.values)
        country_col_index = findElementInList(dataColumns, columnNames)
        colName = data.columns[country_col_index]
        whereCountry = data[colName].str.lower() == countryName.lower()
        data = data.where(whereCountry).dropna()

        if df.empty:
            df = data
            key = colName
        else:
            df = df.join(
                data.set_index([colName], verify_integrity=True),
                on=[key], how='left',
            )

    return df


grabData("france")
