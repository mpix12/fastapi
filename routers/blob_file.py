from fastapi import APIRouter, File, UploadFile
import shutil
from fastapi.responses import FileResponse

router = APIRouter(
    prefix="/file",
    tags=['file']
)


@router.post('/')
def get_file(file: bytes = File(...)):
    content = file.decode('utf-8')
    lines = content.split('\n')
    return {'lines': lines}


@router.post('/upload')
def upload_file(upload_file: UploadFile = File(...)):
    file_path = f"media/{upload_file.filename}"
    print(file_path)
    with open(file_path, 'w+b') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return {'name': file_path,
            'type': upload_file.content_type}


@router.get('/download/{file_name}', response_class=FileResponse)
def download_file(file_name: str):
    file_path = f"media/{file_name}"
    return file_path

