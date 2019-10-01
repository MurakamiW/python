import numpy as np

class radius_Volume_Error_Calc:
    C_1 = 0.28209479
    C_2 = 0.09403160


    def core_radius(self, sasa = [1,2,3]):
        radius = self.C_1 * (np.power(sasa,0.5))
        return radius


    def core_radius_error(self, sasa, sasa_error):
        radius_error = self.C_1 * np.subtract( np.power(sasa,0.5) , np.power(np.subtract(sasa, sasa_error),0.5)) 
        return radius_error


    def core_volume(self, sasa):
        volume = self.C_2 * ( np.power(sasa,1.5) )
        return volume


    def core_volume_error(self, sasa, sasa_error):
        volume_error = self.C_2 * np.subtract( np.power(np.add(sasa_error,sasa),1.5) , np.power(sasa,1.5) )
        return volume_error




if __name__ == "__main__":

    rv=radius_Volume_Error_Calc()


    itemList1 = []
    for line in open('Data1.txt', 'r'):
     itemList1.append(line[:-1].split('\t'))
    print (itemList1)

    itemList2 = []
    for line in open('Data2.txt', 'r'):
     itemList2.append(line[:-1].split('\t'))
    print (itemList2)
    
    N = [float(lists[3]) for i,lists in enumerate(itemList2)]
    ds = [float(lists[2]) for i,lists in enumerate(itemList2)]
    s=[float(lists[1]) for i,lists in enumerate(itemList2)]
    r=rv.core_radius(s)
    dr=rv.core_radius_error(s,ds)
    v=rv.core_volume(s)
    dv=rv.core_volume_error(s,ds)
    [print(N[i],r[i],dr[i],v[i],dv[i],s[i],ds[i]) for i in range(len(ds))]
    

    np.savetxt('sample1.txt', itemList1, fmt='%.18s', delimiter='\t', comments='#')
    np.savetxt('sample2.txt', itemList2, fmt='%.18s', delimiter='\t', comments='#')    
