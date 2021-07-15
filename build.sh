#!/bin/sh

for f in pages/*.sp
do
    python3 gen.py $f
done
