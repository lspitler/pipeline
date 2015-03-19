import os

__version__ = '0.7.0'

# If you set the environment variable 'PYWIFES_DIR' then it will be found
mdir = os.getenv('PYWIFES_DIR')

# Otherwise, just look where we are right now, and go from there
if mdir == None:
    #metadata_dir = '/Users/fvogt/Tools/Python/pywifes/pywifes_v0.5.6/reference_data/'
    # Where are we located ?
    src_dir = os.path.dirname(__file__)
    # Where are the reference data ?
    pywifes_dir = os.path.join(src_dir, '..')
    metadata_dir = os.path.join(pywifes_dir, 'reference_data')
else:
    metadata_dir = mdir


