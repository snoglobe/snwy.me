#!/bin/sh

for f in pages/*.ssg
do
    python3 gen.py $f
done
