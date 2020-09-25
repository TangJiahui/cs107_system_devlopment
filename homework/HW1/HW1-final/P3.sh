#!/bin/bash
grep -c [0-9] apollo13.txt > apollo_out.txt
grep --help | grep -- --count
ls -l | grep -c "\.py$"
find ! -perm -o+r,o+w -type f| wc -l
find -maxdepth 1 -type f,d ! -perm -o+r,o+w | wc -l
