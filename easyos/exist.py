import os

def exist_file(path=os.getcwd()):
    first=os.path.exists(path)
    second=os.path.isfile(path)
    if first:
        if second:
            return True
        elif not second:
            return False
        else:
            return TypeError
    elif not first:
        return False
    else:
        return TypeError

def exist_path(path=os.getcwd()):
    first=os.path.exists(path)
    second=os.path.isdir(path)
    if first:
        if second:
            return True
        elif not second:
            return False
        else:
            return TypeError
    elif not first:
        return False
    else:
        return TypeError

def exists(path,way):
    if way==1 or way=='p' or way=='path':
        _bool=exist_path(path)
    elif way==2 or way=='f' or way=='file':
        _bool=exist_file(path)
    else:
        _bool=None
    if _bool:
        return True
    elif not _bool:
        not_found.append(path)
        return False
    else:
        return TypeError

def exist(path=os.getcwd()):
    if exist_path(path):
        return 1
    elif exist_file(path):
        return 2
    else:
        return TypeError
