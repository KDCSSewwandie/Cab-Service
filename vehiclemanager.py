import vehicle
class Vehiclemanager:
    Queue=[]
    id=1

    def Add(self, type,max_passenger, Ac, size, max_load):
        self.Queue.append(vehicle.Vehicle(self.id, type, max_passenger, Ac, size, max_load, True))
        self.id+=1
        print("vehicle added")
        return 1

    def remove(self, id):
        for v in self.Queue:
            if id == v.get_id():
                self.Queue.remove(v)
                print("Vehicle removed")
                return 1
        print("Vehicle not found")
        return 0

    def assign(self, type, max_passenger, Ac, size, max_load):
        for v in self.Queue:
            if type == v.get_type() and max_passenger ==v.get_max_passenger() and Ac ==v.get_Ac() and max_load == v.get_max_load() and size == v.get_size()  and True==v.get_Available():
                v.set_Available()
                print("Assign job successful.Vehicle id is", v.get_id())
                return 1
        print("Vehicle not found for your requirement")
        return 0

    def release(self,id):
        for v in self.Queue:
            if id== v.get_id():
                if v.get_Available()== False:
                    self.Queue.append(vehicle.Vehicle(v.get_id(), v.get_type(), v.get_max_passenger(), v.get_Ac(), v.get_size(), v.get_max_load(), True))
                    self.Queue.remove(v)
                    print("Vehicle released")
                    return 1
                else:
                    print("Vehicle is not in the job")
                    return 0
        print("Vehicle id not found")
        return 0

    def Available(self):
        list=[]
        print("ID \t TYPE  MAX_PASSENGER \t AC \t SIZE \t MAX_LOAD")
        for v in self.Queue:
            if v.get_Available() == True:
                print(v.get_id(),"\t", v.get_type(),"\t\t", v.get_max_passenger(),"\t\t\t", v.get_Ac()," \t", v.get_size(),"\t\t", v.get_max_load())
                list.append([v.get_id(), v.get_type(), v.get_max_passenger(), v.get_Ac(), v.get_size(), v.get_max_load()])
        print("\t\t**************END**************\n")
        return list
