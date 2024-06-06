import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

fromdir="C:/Users/Dhananjoy/Downloads"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self , event):
        print(f"Hey , {event.src_path} has been created")

    def on_deleted(self , event):
        print(f"Hey , {event.src_path} has been deleted")

    def on_modified(self , event):
        print(f"Hey , {event.src_path} has been modified")
    def on_moved(self , event):
        print(f"Hey , {event.src_path} has been moved")

eventHandler = FileEventHandler()
observer = Observer()
observer.schedule(eventHandler , fromdir , recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running")
except:
    print("stopped")
    observer.stop()
  