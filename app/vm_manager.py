import subprocess

def start_vm():
    try:
        subprocess.Popen(["qemu-system-x86_64", "-m", "2G", "-hda", "/path/to/vm.img"])
    except Exception as e:
        print(f"Error starting VM: {e}")

def stop_vm():
    try:
        subprocess.Popen(["pkill", "qemu-system-x86_64"])
    except Exception as e:
        print(f"Error stopping VM: {e}")
