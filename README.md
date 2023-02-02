v3v
```
conda create --name amazon_env -c conda-forge python=3.10.8 pandas fastapi uvloop uvicorn python-multipart httptools aiofiles --force
```

pip install pandas fastapi uvloop uvicorn python-multipart httptools aiofiles

uvicorn python.app:app --reload