from pymongo import MongoClient
import xlrd

mongo_uri = "mongodb+srv://admin:admin@cluster0-njvqs.mongodb.net/test?retryWrites=true"

client = MongoClient(mongo_uri)
ielts_database = client.db_ielts
reading_test = ielts_database["reading_test"]

wb = xlrd.open_workbook("Data.xlsx")
sheet_names = wb.sheet_names()

for sheet_name in sheet_names:
    sheet_data = wb.sheet_by_name(sheet_name)
    collection_on_mongo = ielts_database[sheet_name]
    # reading_sheet = wb.sheet_by_index(0)
    # print(sheet.cell_value(2, 1)) #row, #column ==> value of cell from 0
    # print(reading_sheet.row_values(0)) # value of row
    # print(sheet.nrows) # number of rows
    # print(sheet.ncols) # number of row
    # print(wb.nsheets)
    # print(wb.sheet_names())

    Header = sheet_data.row_values(0)

    for i in range(sheet_data.nrows-1):
        data_row = sheet_data.row_values(i+1)
        record = dict(zip(Header,data_row))
        Passage_ID = sheet_data.cell_value(i+1, 0)
        exist_testing = collection_on_mongo.find_one({"Passage_ID": Passage_ID})
        if exist_testing == None:
                collection_on_mongo.insert_one(record)


