import numpy as np

class radius_Surface_Error_Calc:
    C_3 = 0.6203
    C_4 = 4.8360


    def core_radius(self, v):
        radius = self.C_3 * (np.power(v,0.3333))
        return radius

    def core_radius_error(self, v, v_error):
        radius_error = self.C_3 * np.subtract( np.power(v,0.3333) , np.power(np.subtract(v, v_error),0.3333)) 
        return radius_error


    def core_surface(self, v):
        surface = self.C_4 * ( np.power(v,0.6667) )
        return surface


    def core_surface_error(self, v, v_error):
        surface_error = self.C_4 * np.subtract(np.power(v,0.6667),np.power(np.subtract(v,v_error),0.6667) )
        return surface_error


class make_List():

    def __init__(self,table):
        self.table = table

    def extend_column(self, column_number):
        column = [float(lines[column_number]) for i,lines in enumerate(self.table)]
        return column



if __name__ == "__main__":

    rs=radius_Surface_Error_Calc()
    
    itemList = []
    for line in open('Geometrically.dat', 'r'):
     itemList.append(line[:-1].split('\t'))
    print (itemList)
    
    ec=make_List(itemList)
    N = ec.extend_column(0)
    v=ec.extend_column(1)
    dv = ec.extend_column(2)

    r=rs.core_radius(v)
    dr=rs.core_radius_error(v,dv)
    s=rs.core_surface(v)
    ds=rs.core_surface_error(v,dv)
    [print(N[i],r[i],dr[i],v[i],dv[i],s[i],ds[i]) for i in range(len(ds))]
    p=np.c_[N,r,dr,v,dv,s,ds]
   #print(p)
    np.savetxt('SRV_Geometrically.dat',p, fmt='%.7s', delimiter='\t', comments='#')
