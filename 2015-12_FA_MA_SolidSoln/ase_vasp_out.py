import ase.io.vasp
import ase.io.xyz

cell = ase.io.xyz.read_xyz("2x2x2_MA_FA_checkerboard_sorted.xyz")
ase.io.vasp.write_vasp("2x2x2_MA_FA_checkerboard_sorted.ASE.vasp",cell, label='2x2x2_MA_FA_checkerboard_sorted.ASE.vasp',direct=True,sort=True,vasp5=True)

