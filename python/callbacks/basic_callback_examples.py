#########################
# 1.- Simple callback
#########################

def callbackPrint(s):
    print('*** - Length of the text file is: ', s)
    
def findFileLength(path, callback):
    f = open(path, "r")
    length = len(f.read())
    f.close()
    callback(length)
    
if __name__ == '__main__':
    findFileLength("/Users/miguel.rooney/Jon.txt",callbackPrint)
