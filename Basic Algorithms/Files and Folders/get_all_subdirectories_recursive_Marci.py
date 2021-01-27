import os

def getChildFolders(fold_path):
    subfolders = [ f.path for f in os.scandir(fold_path) if f.is_dir() ]
    return subfolders

def collect_folders(start, depth=-1):
    """ negative depths means unlimited recursion """
    folder_ids = []

    # recursive function that collects all the ids in `acc`
    def recurse(current, depth):
        if depth != 0:
            for folder in getChildFolders(current):
                # recursive call for each subfolder
                folder_ids.append(folder)
                recurse(folder, depth-1)

    recurse(start, depth) # starts the recursion
    return folder_ids

print(collect_folders('C:\STB Biswajit Das'))