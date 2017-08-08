#!/bin/bash

i="9999"

while [ $i -lt 99999 ]
do
i=$[$i+1]
echo $i >> dic.txt
done
