import subprocess
from .models import AnalysisJob

def run_analysis(sample_path, job: AnalysisJob):
    """
    Runs the malware sample inside a QEMU VM for analysis.
    """
    qemu_cmd = [
        "qemu-system-x86_64",
        "-m", "512M",
        "-snapshot",
        "-hda", "/path/to/vm/image.qcow2",
        "-drive", f"file={sample_path},format=raw,if=virtio",
        "-net", "none",
    ]

    try:
        proc = subprocess.run(qemu_cmd, capture_output=True, text=True, timeout=300)
        job.log = proc.stdout + "\n" + proc.stderr
        job.success = proc.returncode == 0
    except subprocess.TimeoutExpired:
        job.log = "Analysis timed out."
        job.success = False
    job.finished_at = timezone.now()
    job.save()
