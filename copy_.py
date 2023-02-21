# copyfile() = copies contents of a file
# сору () =copyfile) + permission mode + destination can be a directory
# сору2 () = copy() + copies metadata(file's creation and modification times)

import shutil

shutil. copy2('test. txt', 'copy.txt')  # src, dst
