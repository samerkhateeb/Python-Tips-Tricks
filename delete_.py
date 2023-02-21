import os
import shutil

path = "move"
try:
    # os.remove(path) # delete file
    # os.rmdir(path) # delete empty directory
    shutil.rmtree(path)  # delete file with all of its content
    print('deleted successfully.:)')
except FileNotFoundError:
    print('the file is not found')

except PermissionError:
    print('you dont have proper permission to delete the file')

except OSError:
    print('the folder is not empty, pleas clean it')
