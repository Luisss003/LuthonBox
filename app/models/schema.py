from pydantic import BaseModel

class SampleUpload(BaseModel):
    filename: str
    content_base64: str
