# JMF 2015-02-22
# Quick ASE script to generate large supercells for MAPI and FAPI

import ase.io.vasp

cell = ase.io.vasp.read_vasp("CsPbI3_brokensymm_cubic.POSCAR.vasp")

ase.io.vasp.write_vasp("POSCAR_2x2x2_CsPbI3",cell*(2,2,2), label='POSCAR_2x2x2_CsPbI3',direct=True,sort=True,vasp5=True)
ase.io.vasp.write_vasp("POSCAR_4x4x4_CsPbI3",cell*(4,4,4), label='POSCAR_4x4x4_CsPbI3',direct=True,sort=True,vasp5=True)
ase.io.vasp.write_vasp("POSCAR_6x6x6_CsPbI3",cell*(6,6,6), label='POSCAR_6x6x6_CsPbI3',direct=True,sort=True,vasp5=True)
ase.io.vasp.write_vasp("POSCAR_8x8x8_CsPbI3",cell*(8,8,8), label='POSCAR_8x8x8_CsPbI3',direct=True,sort=True,vasp5=True)

