from blogengine import pageLocation
from example import main
import pickle, os

def createPage(info):


    path = os.path.join(pageLocation, info['pageName'])



    written = {}
    checkPath = os.path.abspath(path)
    if ".." in path:
        return 'Not Allowed'
    #path = list(pageInfo.keys())[0] + '.txt'
    with open(path, 'wb') as f:
        pickle.dump(info, f)
    return 'success'

def deletePage(name):
    path = os.path.join(pageLocation, name)
    try:
        os.remove(path)
        return 'success'
    except:
        return 'failed'

def getPage(name):
    path = os.path.join(pageLocation, name)
    try:
        with open(path, 'rb') as f:
            out = pickle.load(f)
            return out
    except:
        return {'content': ''}

def getMeta(name):
    path = os.path.join(pageLocation, name)

    with open(path, 'rb') as f:
        out = pickle.load(f)['meta']



        return out