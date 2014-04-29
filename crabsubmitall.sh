#!/bin/bash
for i in {1..10} ; do crab -c $1 -submit `expr \( $i - 1 \) \* 500 + 1`-`expr $i \* 500` ; done
