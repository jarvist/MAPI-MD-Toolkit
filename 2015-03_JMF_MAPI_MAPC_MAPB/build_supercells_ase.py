# JMF 2015-02-22
# Quick ASE script to generate large supercells for MAPI and FAPI

import ase.io.vasp

cell = ase.io.vasp.read_vasp("pseudocubic_CH3NH3PbI3.POSCAR.vasp")
ase.io.vasp.write_vasp("POSCAR_2x2x2_MAPI",cell*(2,2,2), label='POSCAR_4x4x4_MAPI',direct=True,sort=True,vasp5=True)

cell = ase.io.vasp.read_vasp("pseudocubic_CH3NH3PbCl3.POSCAR.vasp")
ase.io.vasp.write_vasp("POSCAR_2x2x2_MAPCl",cell*(2,2,2), label='POSCAR_2x2x2_MAPCl',direct=True,sort=True,vasp5=True)

cell = ase.io.vasp.read_vasp("pseudocubic_CH3NH3PbBr3.POSCAR.vasp")
ase.io.vasp.write_vasp("POSCAR_2x2x2_MAPBr",cell*(2,2,2), label='POSCAR_2x2x2_MAPBr',direct=True,sort=True,vasp5=True)

# Files from github;
# https://github.com/WMD-Bath/Hybrid-perovskites/
# pseudocubic_CH3NH3PbBr3.POSCAR.vasp
# pseudocubic_CH3NH3PbCl3.POSCAR.vasp
# pseudocubic_CH3NH3PbI3.POSCAR.vasp


