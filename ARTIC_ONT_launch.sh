
path_barcoding="/srv/nfs/ngs-stockage/NGS_Virologie/CGINEVRA/Artic_Minion/2020-07-03_Run_5_ARTIC/2020-07-03_Run_5_ARTIC/barcoding"
output_dir="/srv/nfs/ngs-stockage/NGS_Virologie/CGINEVRA/Artic_Minion/2020-07-03_Run_5_ARTIC/2020-07-03_Run_5_ARTIC/ARTIC_RESULTS"
SEQSUMfilepath="/srv/nfs/ngs-stockage/NGS_Virologie/CGINEVRA/Artic_Minion/2020-07-03_Run_5_ARTIC/2020-07-03_Run_5_ARTIC/20200703_1336_MN31515_FAO01103_e6ec20f7/sequencing_summary_FAO01103_986b0304.txt"
FAST5path="/srv/nfs/ngs-stockage/NGS_Virologie/CGINEVRA/Artic_Minion/2020-07-03_Run_5_ARTIC/2020-07-03_Run_5_ARTIC/20200703_1336_MN31515_FAO01103_e6ec20f7/fast5_pass/"
ARTICrep="/data/HadrienR/artic-ncov2019/"

snakemake -s ARTIC_ONT.py \
    --core 8 \
    --config \
        BARCODEpath=$path_barcoding \
        RESULTpath=$output_dir \
        SEQSUMpath=$SEQSUMfilepath \
        FAST5path=$FAST5path \
        ARTICrep=$ARTICrep