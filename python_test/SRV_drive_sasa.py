import numpy as np

class radius_Volume_Error_Calc:
    C_1 = 0.28209479
    C_2 = 0.09403160


    def core_radius(self, sasa = [1,2,3]):
        radius = self.C_1 * (np.power(sasa,0.5))
        #radius = pow(sasa,0.5)
        return radius


    def core_radius_error(self, sasa, sasa_error):
  #      a = sasa - sasa_error
        radius_error = self.C_1 * np.subtract( np.power(sasa,0.5) , np.power(np.subtract(sasa, sasa_error),0.5)) 
        return radius_error


    def core_volume(self, sasa):
        volume = self.C_2 * ( np.power(sasa,1.5) )
        return volume


    def core_volume_error(self, sasa, sasa_error):
        volume_error = self.C_2 * np.subtract( np.power(np.add(sasa_error,sasa),1.5) , np.power(sasa,1.5) )
        return volume_error

class make_List():

    def __init__(self,table):
        self.table = table

    def extend_column(self, column_number):
        column = [float(lines[column_number]) for i,lines in enumerate(self.table)]
        return column



if __name__ == "__main__":

    rv=radius_Volume_Error_Calc()
    
    itemList = []
    for line in open('sasa_probe_1nm_PEG10.dat', 'r'):
     itemList.append(line[:-1].split('\t'))
    print (itemList)
    
    ec=make_List(itemList)
    N = ec.extend_column(0)
    s=ec.extend_column(1)
    ds = ec.extend_column(2)

    r=rv.core_radius(s)
    dr=rv.core_radius_error(s,ds)
    v=rv.core_volume(s)
    dv=rv.core_volume_error(s,ds)
    [print(N[i],r[i],dr[i],v[i],dv[i],s[i],ds[i]) for i in range(len(ds))]
    p=np.c_[N,r,dr,v,dv,s,ds]
   #print(p)
    np.savetxt('SRV_sasa_probe_1nm_PEG10.dat',p, fmt='%.7s', delimiter='\t', comments='#')
