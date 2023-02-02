# @app.get("/")
# async def create_files():
#     return {"message": "nice!"}

# @app.post("/upload/")
# async def create_files(file: UploadFile):
#     return {"file_data": file}

# @app.post("/files/")
# async def create_files(file1: UploadFile, file2: UploadFile):
#     return {"file1_name": file1.filename, "file2_name": file2.filename}

# import pandas as pd

# df_amazon = pd.read_csv("/home/daiki/Dropbox/v3v/amazon-assistant-api/sample/12345.txt", encoding = "cp932")

# print(df_amazon)

string = "abcdefghijklmnopqrstuvwxyz"
string = string[5:-5]
print(string)
