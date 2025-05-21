from fastapi import APIRouter, UploadFile, File, HTTPException
from executor import execute_malware
from vm_manager import start_vm, stop_vm
from schema import ExecuteRequest 

router = APIRouter()

@router.post("/upload/")
async def upload_sample(file: UploadFile = File(...)):
    try:
        file_path = f"/home/sputnik/LuthonBoxTests/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())
        return {"message": "File uploaded successfully", "path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/execute/")
async def execute(request: ExecuteRequest):
    result = await execute_malware(request.file_path)
    return {"result": result}

@router.post("/start_vm/")
async def start_vm_endpoint():
    start_vm()
    return {"message": "VM started"}

@router.post("/stop_vm/")
async def stop_vm_endpoint():
    stop_vm()
    return {"message": "VM stopped"}
