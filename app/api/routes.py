from fastapi import APIRouter, HTTPException
from app.models.schema import SampleUpload
from app.core.executor import execute_sample
from app.utils.file_utils import save_sample_file

router = APIRouter()

@router.post("/submit")
async def submit_sample(sample: SampleUpload):
    try:
        path = save_sample_file(sample.filename, sample.content_base64)
        result = execute_sample(path)
        return {"status": "submitted", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
