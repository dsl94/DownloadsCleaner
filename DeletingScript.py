import os, time, sys, shutil

# Paths of folder I want to clean
paths = ["/Users/Nemanja/Downloads", "/Users/Nemanja/Documents/ViberDownloads"]
# Current time
now = time.time()
# File extension or file or folder names that I don't want to delete
skip = ["Udemy"]


def check_for_skip(file_check):
    for s in skip:
        if file_check.__contains__(s):
            return True
    return False

deletedTotal = 0
for path in paths:
    print("-----------------------------------------------------------------------------------------------------------")
    print("Deleting in: ", path)
    deleted = 0
    for f in os.listdir(path):
        file = os.path.join(path, f)
        if not check_for_skip(file):
            # Older then 7 days, change 7 with number of days
            if os.stat(file).st_mtime < now - 7*86400:
                deleted += 1
                print("Deleting: ", file)
                if os.path.isfile(file):
                    os.remove(file)
                else:
                    shutil.rmtree(file)
    print("Number of deleted files or folders: ", deleted)
    deletedTotal += deleted
    print("-----------------------------------------------------------------------------------------------------------")

print("-----------------------------------------------------------------------------------------------------------")
print("COMPLETED")
print("TOTAL DELETED: ", deletedTotal)
print("-----------------------------------------------------------------------------------------------------------")
