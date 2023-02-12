import os


def fopen(fpath, mode):# define the path
    try:
        file = open(fpath, mode)
    except:
        file = 0
        path, fname = os.path.split(fpath)  # it looks for the last slash and split the path
        if not os.path.exists(path):
            os.makedirs(path)
    return file

# check if the folder with the file already exists if not it creates it
if __name__ == '__main__':
    fpath ="./data/bookDB/booklist.txt"
    try:
        file = open(fpath, 'r')
    except:
        file = 0
        path, fname = os.path.split(fpath)  # it looks for the last slash and split the path
        if not os.path.exists(path):
            os.makedirs(path)

    print(path, fname)