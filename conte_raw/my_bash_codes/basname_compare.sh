!#/bin/bash

t_file1=$1
t_file2=$2

out_file=$3


echo "Comparing following two files">>$out_file
echo " ">>$out_file
echo $t_file1>>$out_file
echo " " >>$out_file
echo $t_file2>>$out_file
echo " ">>$out_file

#declare -a b_name1
#declare -a b_name2

idx=0
while read -r line
do
   #echo $line
   y=$( basename "$line" )
   #echo $y 
   b_name1+=$y
done < "$t_file1"

idx=0
while read -r line
do
    #echo $line
    l=${line// /_}
    #echo $l
    y1=$( basename "$l" )
    #echo $y1
    b_name2+=$y1
done < "$t_file2"

for i in "{$b_name1[@]}"
do
    echo $i
    echo $'\n'
     
    if echo $b_name2 | grep -w $i > /dev/null; then
    	echo "$i" #>>$out_file
    else
        echo $i "not there"
    fi
done

