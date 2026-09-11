#!/bin/bash
read N
n=1
while [ $n -le N ]
do touch file<$n>.txt
	a=$(( $RANDOM ))
	b=$(( $RANDOM))
	c=$(( $a + $b))
	echo $a + $b = $c / | file<$n> 
n=$(($n+1))
done


