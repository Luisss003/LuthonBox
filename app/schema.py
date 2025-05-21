from pydantic import BaseModel

class ExecuteRequest(BaseModel):
    file_path: str

class UploadResponse(BaseModel):
    message: str
    path: str
