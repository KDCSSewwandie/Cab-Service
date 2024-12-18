import vehiclemanager
import ui

ovm=vehiclemanager.Vehiclemanager()

def Add(user):
    return ovm.Add(user[0],user[1],user[2],user[3],user[4])

def Assign(user):
    return ovm.assign(user[0],user[1],user[2],user[3],user[4])

def Remove(id):
    return ovm.remove(id)

def Release(id):
    return ovm.release(id)
def Available():
    return ovm.Available()