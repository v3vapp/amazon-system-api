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

@app.post('/up')
def get_uploadfile(upload_file: UploadFile = File(...)):
    # try:
        os.makedirs(f'{root}/static/', exist_ok=True)

        app.mount('/static', StaticFiles(directory="static"), name='static')

        path = f'{root}/static/{upload_file.filename}'

        with open(path, 'w+b') as buffer:

            shutil.copyfileobj(upload_file.file, buffer)

            unshipped_path = rename_file(upload_file.filename, "unshipped.txt")

        AmazonCheckSheet(unshipped_path).generate()

        return {'filename': upload_file.filename,
                'type': upload_file.content_type}

    # except Exception as e:

        # raise JSONResponse(status_code=status.HTTP_201_CREATED, content=e)

#_____________________________________________________________________________


@app.get('/down/{name}', response_class=FileResponse)
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
