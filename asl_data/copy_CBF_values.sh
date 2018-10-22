##################################################

# Developed by Sameera K. Abeykoon (August  2018)

##################################################

echo Enter the Subject number list eg:0194 2264 2280
read -a sub_list

#sub_list=(0194 2264 2450 2280 2812 2791 3012 2839)
echo ${sub_list[*]}

for Subjlist in "${sub_list[@]}"; do :;
    # cd /mnt/hcp01/scR21_asl/asl_results/${Subjlist}
    for i in {1..3}; do :;
    # change dir to Asl folder to get the CBF_values file
    cd /mnt/hcp01/scR21_asl/asl_results/${Subjlist}/day_$i/Asl
    cp CBF_values_${Subjlist}_day_$i.csv /mnt/hcp01/scR21_asl/asl_results/ASL_CBF_values
    done
done

