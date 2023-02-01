from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os


def rename_file(filename_uploaded, new_name="unshipped.txt"):
    old_path = f'./static/{filename_uploaded}'
    new_path = f'./static/{new_name}'
    os.rename(old_path, new_path)
    return new_path



app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name='static')

# set CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

@app.post('/up')
def get_uploadfile(upload_file: UploadFile = File(...)):
    import checksheet

    print(upload_file.file)

    path = f'static/{upload_file.filename}'

    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
        unshipped_path = rename_file(upload_file.filename, "unshipped.txt")

        checksheet.generate(unshipped_path)

    return {'filename': path,
            'type': upload_file.content_type}


@app.get('/down/{name}', response_class=FileResponse)
def get_file(name: str):
    path = f'static/{name}'
    return path


if __name__ == "__main__":
    app.run()
