import meshio
import pandas as pd

def read_statistics(fname):
    """ Read the statistics file output by CIG-ASPECT

    return a pandas table, where names are taken from the statistics file.
    """
    # Remove comments in the header:
    header = []
    header_read = True

    with open(fname) as f:
        while header_read :
            line = f.readline()
            if line[0] == '#':
                idx_start = line.find(":")
                header.append(line[idx_start+2:-1])
            else:
                header_read = False

    # Read the data here
    values = pd.read_csv(fname, skiprows=len(header), header=None, delim_whitespace=True, names=header)
    return values



def read_vtu_file (file_name):
    """
    This function takes an input .vtu file_name (either structured or
    unstructured mesh) and returns the point coordinates and values in that file.  
    
    Parameters
    ----------
    file_name : str
        The name of the vtu file
        
    Returns
    -------
    nodes  : A numpy array with columns corresponding to the 
             coordinates of the node points (x, y, z) in the input mesh.
    
    data_out : A dictionary containing key:values corresponding to the 
               available fields and their values in the input .vtu file.
    """
    
    mesh     = meshio.read(file_name)
    nodes    = mesh.points
    data_out = mesh.point_data
    
    return (nodes, data_out)
