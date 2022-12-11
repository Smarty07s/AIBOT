def createf(filename , data):
    with open(filename,'w'):
        f = open(filename,'w')
        f.write(data)
        f.close()