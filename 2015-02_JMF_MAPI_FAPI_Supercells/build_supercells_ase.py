# JMF 2015-02-22
# Quick ASE script to generate large supercells for MAPI and FAPI

import ase.io.vasp

cell = ase.io.vasp.read_vasp("pseudocubic_CH3NH3PbI3.POSCAR.vasp")

ase.io.vasp.write_vasp("POSCAR_2x2x2_MAPI",cell*(2,2,2), label='POSCAR_2x2x2_MAPI',direct=True,sort=True,vasp5=True)
ase.io.vasp.write_vasp("POSCAR_4x4x4_MAPI",cell*(4,4,4), label='POSCAR_4x4x4_MAPI',direct=True,sort=True,vasp5=True)
ase.io.vasp.write_vasp("POSCAR_6x6x6_MAPI",cell*(6,6,6), label='POSCAR_6x6x6_MAPI',direct=True,sort=True,vasp5=True)
ase.io.vasp.write_vasp("POSCAR_8x8x8_MAPI",cell*(8,8,8), label='POSCAR_8x8x8_MAPI',direct=True,sort=True,vasp5=True)
ase.io.vasp.write_vasp("POSCAR_10x10x10_MAPI",cell*(10,10,10), label='POSCAR_10x10x10_MAPI',direct=True,sort=True,vasp5=True)

cell = ase.io.vasp.read_vasp("pseudocubic_CH2NHCH2PbI3.POSCAR.vasp")

ase.io.vasp.write_vasp("POSCAR_2x2x2_FAPI",cell*(2,2,2), label='POSCAR_2x2x2_FAPI',direct=True,sort=True,vasp5=True)
ase.io.vasp.write_vasp("POSCAR_4x4x4_FAPI",cell*(4,4,4), label='POSCAR_4x4x4_FAPI',direct=True,sort=True,vasp5=True)
ase.io.vasp.write_vasp("POSCAR_6x6x6_FAPI",cell*(6,6,6), label='POSCAR_6x6x6_FAPI',direct=True,sort=True,vasp5=True)
ase.io.vasp.write_vasp("POSCAR_8x8x8_FAPI",cell*(8,8,8), label='POSCAR_8x8x8_FAPI',direct=True,sort=True,vasp5=True)
ase.io.vasp.write_vasp("POSCAR_10x10x10_FAPI",cell*(10,10,10), label='POSCAR_10x10x10_FAPI',direct=True,sort=True,vasp5=True)


# Files from github;
# https://github.com/WMD-Bath/Hybrid-perovskites/
# pseudocubic_CH2NHCH2PbI3.POSCAR.vasp  pseudocubic_CH3NH3PbI3.POSCAR.vasp
