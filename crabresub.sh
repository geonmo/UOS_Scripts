#!/bin/bash

for i in {1..48}
do
    for D in `find $1* -maxdepth 0`
    do
	if [ -d $D ]; then
	    echo loop $i, crab -submit 500 -c $D
	    crab -submit 500 -c $D
            echo loop $i, crab -status -c $D
            crab -status -c $D
	    echo loop $i, crab -get -c $D
	    crab -get -c $D
            echo loop $i, crab -resubmit bad -c $D
	    crab -resubmit bad -c $D
	    echo loop $i, crab -publish 500 -c $D
	    crab -publish 500 -c $D
	fi
    done
    echo loop $i, sleep $D
    sleep 30m
done
