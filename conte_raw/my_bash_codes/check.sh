!#/bin/bash

t_file1=$1
t_file2=$2

out_file=$3

out_file2=$4

echo "Comparing following two files">>$out_file
echo " ">>$out_file
echo $t_file1>>$out_file
echo " " >>$out_file
echo $t_file2>>$out_file
echo " ">>$out_file

echo "Comparing following two files">>$out_file2
echo " ">>$out_file2
echo $t_file1>>$out_file2
echo " " >>$out_file2
echo $t_file2>>$out_file2
echo " ">>$out_file2

#readarray arr1<$t_file1
#readarray arr2<$t_file2

no_lines_f1=$(wc -l $t_file1)
no_lines_f2=$(wc -l $t_file2)

no_col=2

#for i in {0..no_lines_f1}; do
#    eval "declare -a matrix1$i=( $(for j in {0..no_col}; do echo 0; done) )"
#done

#for i in {0..no_lines_f1}; do
#    eval "declare -a matrix2$i=( $(for j in {0..no_col}; do echo 0; done) )"
#done

declare -a mat1_v
declare -a mat1_p
declare -a mat2_v
declare -a mat2_p

idx=0
while read -r line
do
    mat1_v[idx]="$( cut -d ' ' -f 1  <<< "$line" )";
    mat1_p[idx]="$( cut -d ' ' -f 2- <<< "$line" )";
    let idx++;
done < "$t_file1"

idx=0
while read -r line
do
    mat2_v[idx]="$( cut -d ' ' -f 1  <<< "$line" )";
    mat2_p[idx]="$( cut -d ' ' -f 2- <<< "$line" )";
    let idx++;
done < "$t_file2"

#echo "${mat1_v[@]}"
#echo ""
#echo "${mat1_p[@]}"

declare -a base1
declare -a base2

idx=0
for i in "${mat1_p[@]}"
do 
   base1[idx]=$(basename "$i");
   let idx++;
done

idx=0
for i in "${mat2_p[@]}"
do
   base2[idx]=$(basename "$i");
   #case "${base2[idx]}" in "${base1[@]}";
   #if "${base1[@]} | grep "${base2[idx]}" 
   #then
   #	echo "found"
   #fi
   let idx++;
done

# echo "${base1[@]}"
# echo ""

# echo "${#base1[@]}"
# echo ""

echo "Following files are different">>$out_file;
echo " "

echo fol1, path1, fol2, path2

for ((i=1;i<="${#base1[@]}";i++));
do  
    #echo $i
    #echo ${base1[$i]}
    for ((j=1;j<="${#base2[@]}";j++));
    do
    	#echo ${base2[$j]}
    	if [ "${base1[$i]}" = "${base2[$j]}" ];
        then
           #echo "${mat1_p[$i]}"
           #echo "${mat2_p[$j]}"
           if [[ "${mat1_v[$i]}" != "${mat2_v[$j]}" ]];
           then
           	# echo "Following files are different">>$out_file;
                echo "$t_file1","${mat1_p[$i]}","$t_file2","${mat2_p[$j]}">>$out_file;
           	#echo "${mat1_p[$i]} in $t_file1 folder">>$out_file;
           	#echo "${mat2_p[$j]} in $t_file2 folder">>$out_file;
		#echo "  ">>$out_file;
           fi
        fi
    done
done

echo "Following files have same md5sum values">>$out_file2
echo " " >>$out_file2

echo "Finsihed processing first part"

for ((i=1;i<="${#mat1_v[@]}";i++));
do
    for ((j=1;j<="${#mat2_v[@]}";j++));
    do
        if [ "${mat1_v[$i]}" = "${mat2_v[$j]}" ];
        then
            if [[ "${base1[$i]}" != "${base2[$j]}" ]];
            then
            	# echo "Following files have same md5sum values">>$out_file2;
            	echo "$t_file1","${mat1_p[$i]}","$t_file2","${mat2_p[$j]}">>$out_file2;
            	#echo "${mat2_p[$j]} in $t_file2 folder">>$out_file2;
            	#echo "  ">>$out_file2;
            fi
        fi
    done
done

