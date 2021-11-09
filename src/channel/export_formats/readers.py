from channel import get_dim_dnsin
import numpy as np



def read_brutalbin(field, dnsin):
    '''Reads the .bin file output by out_exporter/out2bin.f90. Requires file name and name of dns.in file.'''
    nn = get_dim_dnsin(dnsin)
    nx=nn[0]; ny=nn[1]; nz=nn[2]
    field = np.fromfile(field, dtype=np.double, count=-1, sep='')
    field = field.reshape(((2*nz)+1, ny+1, (2*nx)+1, 3))

    return field