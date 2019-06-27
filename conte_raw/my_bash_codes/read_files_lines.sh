for f in *; 
do 
    [ -d ./"$f" ] && find ./"$f" -maxdepth 1 -exec echo \; | wc -l && echo $f; 
    #echo $f 
done  >> file_report_sub.txt
