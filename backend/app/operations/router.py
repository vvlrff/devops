from fastapi import APIRouter, File, UploadFile

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)

@router.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    # Здесь можно выполнить необходимую обработку загруженного файла
    return {"filename": file.filename}
