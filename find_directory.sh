#!/bin/bash
echo "Enter the filename"
read filename
a=`ls -l $filename | cut -c 1`
echo $a
if [ $a == "t" ]
then 
	echo "Directory"
else
	echo "Not a directory"
fi
