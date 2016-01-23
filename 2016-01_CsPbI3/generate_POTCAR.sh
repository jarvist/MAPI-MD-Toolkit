#  Cs   I  Pb
#   216 648 216

rm POTCAR
cat  ~/Potpaw_PBE.52/Cs_sv/POTCAR >> POTCAR

cat  ~/Potpaw_PBE.52/I/POTCAR >> POTCAR

cat  ~/Potpaw_PBE.52/Pb_d/POTCAR >> POTCAR

grep TITEL POTCAR # check by relisting atoms to STDOUT
head POSCAR
