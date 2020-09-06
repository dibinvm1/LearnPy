import os 
import requests
import shutil


def download(url, dir, fname=None):
    ''' Download functiion takes 3 args
    url - url pointing to the file to download
    dir - direct which the file need to be saved to 
    fname - the name of the file that need to saved default is 
                filename in the url'''
    if fname=None:
        fname = os.path.basename(url)
    dl_path =os.path.join(dir,fname)
    with requests.get(url, stream=True) as r:
        with open(dl_path, 'wb') as img:
            shutil.copyfileobj(r.raw, img)
    return dl_path