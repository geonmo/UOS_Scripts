#!/bin/bash
while [ 1 -le 2 ] 
do
multicrab -status
multicrab -get
multicrab -status
multicrab -resubmit bad
sleep 1800
done
