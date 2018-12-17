###################################################################
#       Developed by Sameera K. Abeykoon
#
#       This will backup data from /mnt/jxvs01/incoming folders 
#       to external hard drive
#
####################################################################


# Change into incoming directory
cd /mnt/jxvs01/incoming

# rTMS data
echo "Copying Smoking_Cessation_Abi_Dargham data"
echo "=========================================="
rsync -rtvu /mnt/SCAN_center/Smoking_Cessation_Abi_Dargham/ Smoking_Cessation_Abi_Dargham/
chmod -R 750 Smoking_Cessation_Abi_Dargham
chgrp -R rtms Smoking_Cessation_Abi_Dargham

# tnfcs data
echo "Copying JVS_K01_VanSnellenberg data"
echo "=========================================="
rsync -rtvu /mnt/SCAN_center/JVS_K01_VanSnellenberg/ JVS_K01_VanSnellenberg/
chmod -R 750 JVS_K01_VanSnellenberg
chgrp -R tnfcs JVS_K01_VanSnellenberg

# rdoc data
echo "Copying RDoC A and B  data"
echo "=========================================="
rsync -rtvu /mnt/SCAN_center/RdOC_A_Abi_Dargham/ RDoc_A_Abi_Dargham/
rsync -rtvu /mnt/SCAN_center/RdOC_B_Abi_Dargham/ RDoc_B_Abi_Dargham/
chmod -R 750 RDoc_A_Abi_Dargham
chmod -R 750 RDoc_B_Abi_Dargham
chgrp -R rdoc RDoc_A_Abi_Dargham
chgrp -R rdoc RDoc_B_Abi_Dargham

# Jodi's data
echo "Copying Spectroscopy_Weinstein data"
echo "=========================================="
rsync -rtvu /mnt/SCAN_center/Spectroscopy_Weinstein/ Spectroscopy_Weinstein/
chmod -R 750 Spectroscopy_Weinstein
chgrp -R k23 Spectroscopy_Weinstein
