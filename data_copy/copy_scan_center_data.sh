###################################################################
#       Developed by Sameera K. Abeykoon
#
#       This will copy data from the /mnt/SCAN_center folder
#       to /mnt/jxvs01/incoming folders and change the permissions
#       of those folders
#       
#       This will copy data from /nfsshare/export/PETMR folder
#       to /mnt/jxvs01/incoming folders and change the permissions
#       of those folders
#
####################################################################


# Change into incoming directory
cd /mnt/jxvs01/incoming

# rTMS data
echo "Copying Smoking_Cessation_Abi_Dargham data"
echo "=========================================="
rsync -rtvu /mnt/Scan_center/Smoking_Cessation_Abi_Dargham/ Smoking_Cessation_Abi_Dargham/
chmod -R 750 Smoking_Cessation_Abi_Dargham
chgrp -R rtms Smoking_Cessation_Abi_Dargham

# tnfcs data
echo "Copying JVS_K01_VanSnellenberg data"
echo "=========================================="
rsync -rtvu /mnt/Scan_center/JVS_K01_VanSnellenberg/ JVS_K01_VanSnellenberg/
chmod -R 750 JVS_K01_VanSnellenberg
chgrp -R tnfcs JVS_K01_VanSnellenberg

# rdoc data
echo "Copying RDoC A, B, C, D and E  data"
echo "=========================================="
rsync -rtvu /mnt/Scan_center/RDoC_A_Abi_Dargham/ RDoc_A_Abi_Dargham/
rsync -rtvu /mnt/Scan_center/RDoC_B_Abi_Dargham/ RDoc_B_Abi_Dargham/
rsync -rtvu /mnt/Scan_center/RDoC_C_Abi_Dargham/ RDoC_C_Abi_Dargham/
rsync -rtvu /mnt/Scan_center/RDoC_D_Weinstein/ RDoC_D_Weinstein/
rsync -rtvu /mnt/Scan_center/RDoC_E_VanSnellenberg/ RDoC_E_VanSnellenberg/
chmod -R 750 RDoc_A_Abi_Dargham
chmod -R 750 RDoc_B_Abi_Dargham
chmod -R 750 RDoC_C_Abi_Dargham
chmod -R 750 RDoC_D_Weinstein
chmod -R 750 RDoC_E_VanSnellenberg
chgrp -R rdoc RDoc_A_Abi_Dargham
chgrp -R rdoc RDoc_B_Abi_Dargham
chgrp -R rdoc RDoC_C_Abi_Dargham
chgrp -R k23 RDoC_D_Weinstein
chgrp -R tnfcs RDoC_E_VanSnellenberg

# Jodi's data
echo "Copying Spectroscopy_Weinstein data"
echo "=========================================="
rsync -rtvu /mnt/Scan_center/Spectroscopy_Weinstein/ Spectroscopy_Weinstein/
chmod -R 750 Spectroscopy_Weinstein
chgrp -R k23 Spectroscopy_Weinstein

# Scott's data
echo "Copying INSIGHT_Moeller data"
echo "======================================"
rsync -rtvu  /mnt/Scan_center/INSIGHT_Moeller/ INSIGHT_Moeller/
chmod -R 750 INSIGHT_Moeller
chgrp -R insight INSIGHT_Moeller

############################################################

## Copying PETMR - VAT data

# Scott's VAT - PETMR data

echo "Copying Scott's VAT project data"
echo "==================================="
rsync -rtvu /nfsshare/export/PETMR/PIMOELLER* PETMR_VAT_Moeller/
chmod -R 750 PETMR_VAT_Moeller
chgrp -R vatsud PETMR_VAT_Moeller

# Jodi's VAT - PETMR data

echo "Copying Jodi's VAT project data"
echo "==================================="
rsync -rtvu /nfsshare/export/PETMR/PIWEINSTEIN* PETMR_VAT_Weinstein/
chmod -R 750 PETMR_VAT_Weinstein
chgrp -R vatscz PETMR_VAT_Weinstein

