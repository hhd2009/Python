import os
import exist

recursive_remove_time=0

def bool_print(msg,bool_=True):
    if bool_:
        print(msg)

def remove(name,bool_=True,work_path=os.getcwd(),way=0):
    if way==0:
        way=exist.exist(work_path)

    import os

    bool_print('>'+work_path,bool_)
    try:
        os.chdir(work_path)
    except FileNotFoundError:
        bool_print('Not found '+work_path+'.',bool_)
        return
    if way==1 or way=='p' or way=='path':
        try:
            all_=os.listdir(name)
            bool_print(all_, bool_)
            if all_==[]:
                os.rmdir(name)
            else:
                bool_print(name+' is not empty.',bool_)
                for i in all_:
                    bool_print('Removed '+name+'\\'+i+' on '+work_path+'.',bool_)
                    try:
                        os.remove(name+'\\'+i)
                    except PermissionError:
                        remove(name+'\\'+i,bool_,work_path,1)
                    bool_print('Removing '+name+'\\'+i+' on '+work_path+'.',bool_)
                remove(name,bool_,work_path,1)
            bool_print('Removed '+name+' on '+work_path+'.', bool_)
            return True
        except FileNotFoundError:
            bool_print('Not found '+name+' on '+work_path+'.',bool_)
            return False

    if way==2 or way=='f' or way=='file':
        try:
            os.remove(name)
            bool_print('Removed '+name+' on '+work_path+'.',bool_)
            return True
        except FileNotFoundError:
            bool_print('Not found '+name+' on '+work_path+'.',bool_)
            return False

def recursive_remove(name,bool_=True,work_path=os.getcwd(),way=0):
    if way==0:
        way=exist.exist(work_path)

    import os

    bool_print('>>'+work_path,bool_)
    try:
        os.chdir(work_path)
    except FileNotFoundError:
        bool_print('Not found '+work_path+'.')
        return
    if way==1 or way=='p' or way=='path':
        while True:
            _work_path=os.getcwd()
            bool_print('>'+_work_path,bool_)
            bool_print('Removing '+name+' on '+_work_path+'~',bool_)
            r=remove(name,bool_,_work_path,way)
            if r:
                break
            elif not r:
                os.chdir('..')
                if os.getcwd()==_work_path:
                    bool_print('Not found '+name+' on all path.',bool_)
                    break
            else:
                return TypeError

    if way==2 or way=='f' or way=='file':
        while True:
            _work_path=os.getcwd()
            bool_print('>'+_work_path)
            bool_print('Removing '+name+' on '+_work_path+'~')
            r=remove(name,bool_,_work_path,way)
            if r:
                break
            elif not r:
                os.chdir('..')
                if os.getcwd()==_work_path:
                    bool_print('Not found '+name+' on all path.')
                    break
            else:
                return TypeError
