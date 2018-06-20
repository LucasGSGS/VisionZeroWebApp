import datetime

name="Manhattan whole day"
print(name)

def timewindower(dt):
    if (dt.isoweekday()>5):
    	return False #immediate return false if weekend
    return True
