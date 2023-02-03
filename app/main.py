from fastapi import FastAPI, File, UploadFile, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import shutil
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
import os
from app.cs import AmazonCheckSheet
from app.config import take_me_root

root = take_me_root()
#_____________________________________________________________________________


def rename_file(filename_uploaded, new_name="unshipped.txt"):
    old_path = f'{root}/static/{filename_uploaded}'
    new_path = f'{root}/static/{new_name}'
    os.rename(old_path, new_path)
    return new_path

#_____________________________________________________________________________

app = FastAPI()

# set CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

#_____________________________________________________________________________

@app.get('/')
def get_file():
    return {"message":"Oh, Hi there! (v3v)<3"}

@app.post('/upload')
def get_uploadfile(file1: UploadFile, file2: UploadFile):

    os.makedirs(f'{root}/static/', exist_ok=True)

    app.mount('/static', StaticFiles(directory="static"), name='static')

    path_unshipped = f'{root}/static/{file1.filename}'
    path_neworder = f'{root}/static/{file2.filename}'

    with open(path_unshipped, 'w+b') as buffer:
        shutil.copyfileobj(file1.file, buffer)
        unshipped_path = rename_file(file1.filename, "unshipped.txt")

    with open(path_neworder, 'w+b') as buffer:
        shutil.copyfileobj(file2.file, buffer)
        neworder_path = rename_file(file2.filename, "neworder.txt")

    sheet = AmazonCheckSheet(unshipped_path, neworder_path)
    
    export_filename = sheet.generate()

    return {'export_filename':export_filename}


#_____________________________________________________________________________


@app.get('/download/{name}', response_class=FileResponse)
def get_file(name: str):

    path = f'{root}/static/{name}'

    return path
#_____________________________________________________________________________


@app.get('/clear')
def get_file():

    shutil.rmtree(f"{root}/static/")

    return {"message":"done"}

#_____________________________________________________________________________

if __name__ == "__main__":
    app.run()
