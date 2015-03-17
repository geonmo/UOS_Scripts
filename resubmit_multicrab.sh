#!/bin/bash
while [ 1 -le 2 ] 
do
multicrab -status short,color
multicrab -get
multicrab -resubmit bad
sleep 1800
done
