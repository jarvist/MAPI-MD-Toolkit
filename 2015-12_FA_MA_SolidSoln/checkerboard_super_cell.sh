# I'm so so sorry for this terrible hack. ~Jarv 2015-12-18

L=6.4

for X in 0 1 
do
 for Y in 0 1 
 do
  for Z in 0 1 
  do

      cat PbI3.xyz | awk '{print $1, $2+'$X'*'$L', $3+'$Y'*'$L', $4+'$Z'*'$L'}'
      
      if (( ($X+$Y+$Z)%2 )) 
      then 
      #    echo "$X $Y $Z MA"
          CATION="MA.xyz"
      else
      #    echo "$X $Y $Z FA"
          CATION="FA.xyz"
      fi
      cat "${CATION}" | awk '{print $1, $2+'$X'.5*'$L', $3+'$Y'.5*'$L', $4+'$Z'.5*'$L'}' 
      # Magic number of 0.5 is to scale cation to middle of the cell 
 
  done
 done
done
