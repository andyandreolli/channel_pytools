from channel import get_dim_dnsin
import numpy as np



def brutalbin_getgrid(nfo_file):
    with open(nfo_file) as f:
        
        lines = f.readlines()
        
        # get first line
        currline = lines[0].split()
        nxtot = currline[0]
        nztot = currline[1]
        dx = currline[2]
        dz = currline[3]

        # get second line
        currline = lines[1].split()
        ny = currline[0]
        nytot = currline[1]
        a = currline[2]
        ymin = currline[3]
        ymax = currline[4]

        # get shape for reading file
        shape = (nztot, nytot, nxtot, 3)

        # get mesh
        x = dx * np.arange(nxtot)
        z = dz * np.arange(nztot)
        y = ymin + 0.5*(ymax-ymin)*( np.tanh(a*(2*np.arange(nytot)/ny-1)) / np.tanh(a) + 0.5*(ymax-ymin) )

        return shape, x, y, z



def read_brutalbin(field, nfo_file):
    '''Reads the .bin file output by out_exporter/out2bin.f90. Requires file name and name of dns.in file.'''
    shape, x, y, z = brutalbin_getgrid(nfo_file)
    field = np.fromfile(field, dtype=np.double, count=-1, sep='')
    field = field.reshape(shape)

    return field, x, y, z



def memmap_brutalbin(field, nfo_file):
    '''Reads the .bin file output by out_exporter/out2bin.f90 as a memmap (see numpy). Requires file name and name of dns.in file.'''
    shape, x, y, z = brutalbin_getgrid(nfo_file)
    field = np.memmap(field, dtype=np.double, shape=shape)
    return field, x, y, z