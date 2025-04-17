from loguru import logger
import subprocess

def start_vm():
    logger.info("Starting VM...")
    subprocess.call(["VBoxManage", "startvm", "LuthonVM", "--type", "headless"])

def stop_vm():
    logger.info("Stopping VM...")
    subprocess.call(["VBoxManage", "controlvm", "LuthonVM", "poweroff"])

def restore_snapshot():
    logger.info("Restoring VM snapshot...")
    subprocess.call(["VBoxManage", "snapshot", "LuthonVM", "restorecurrent"])
