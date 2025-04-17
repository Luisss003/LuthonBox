import os
import base64
import uuid

UPLOAD_DIR = "/tmp/luthonbox_samples"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_sample_file(filename: str, content_b64: str) -> str:
    unique_name = f"{uuid.uuid4()}_{filename}"
    path = os.path.join(UPLOAD_DIR, unique_name)
    with open(path, "wb") as f:
        f.write(base64.b64decode(content_b64))
    return path

