from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name='static')

# set CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/")
# async def create_files():
#     return {"message": "nice!"}

# @app.post("/upload/")
# async def create_files(file: UploadFile):
#     return {"file_data": file}

# @app.post("/files/")
# async def create_files(file1: UploadFile, file2: UploadFile):
#     return {"file1_name": file1.filename, "file2_name": file2.filename}



@app.post('/upload')
def get_uploadfile(upload_file: UploadFile = File(...)):
    path = f'static/{upload_file.filename}'
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return {
        'filename': path,
        'type': upload_file.content_type
    }



if __name__ == "__main__":
    app.run()
