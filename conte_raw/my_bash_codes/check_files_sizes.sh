#!/bin/bash
dir1=$1
dir2=$2
textfile=$3

echo $dir1>>$textfile
echo "">>$textfile
echo $dir2>>$textfile
echo "">>$textfile

list1=$(ls -R $dir1)
list2=$(ls -R $dir2)

i=1
for f in list1; do
     if find list2 -name f; then
        #if [cksum f != cksum file2]; then
	      echo "size $f is different, cksum f, cksum file2"
              #>>$textfile(i);
              let i=i+1
        #fi
     fi
done

