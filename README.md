# vasppy - a python package for manipulating VASP files

Modules:
- poscar
- super

The following modules can be run as command line applications:

## poscar_to_xtl.py

    usage: poscar_to_xtl.py [-h] poscar
    
    Converts a VASP POSCAR file to the .xtl file format
    
    positional arguments:
      poscar      filename of the VASP POSCAR to be processed
    
    optional arguments:
      -h, --help  show this help message and exit

## super.py

    usage: super.py [-h] [-l {1,4}] [-c] [-t {c,cartesian,d,direct}] [-g] [-s h k l]
                 poscar
    
    Manipulates VASP POSCAR files
    
    positional arguments:
      poscar                filename of the VASP POSCAR to be processed
    
    optional arguments:
      -h, --help            show this help message and exit
      -l {1,4}, --label {1,4}
                            label coordinates with atom name at position {1,4}
      -c, --coordinates-only
                            only output coordinates
      -t {c,cartesian,d,direct}, --coordinate-type {c,cartesian,d,direct}
                            specify coordinate type for output
                            {(c)artesian|(d)irect} [default = (d)irect]
      -g, --group           group atoms within supercell
      -s h k l, --s

