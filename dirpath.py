from pathlib import Path
import sys

if len(sys.argv) < 2:
    print("Need a directory name as first arg")
    sys.exit(2)

dirname = sys.argv[1]

dirPath = Path(dirname)
if dirPath.exists() and dirPath.is_dir():
    print(dirPath, 'is a directory')
else:
    print(dirPath, "doesn't exist or is not a directory")
    sys.exit(1)

print(dirPath, 'has type',type(dirPath))