


path_barcoding="/srv/nfs/ngs-stockage/NGS_Virologie/CGINEVRA/Artic_Minion/2020-07-03_Run_5_ARTIC/2020-07-03_Run_5_ARTIC/barcoding"
output_dir="/srv/nfs/ngs-stockage/NGS_Virologie/CGINEVRA/Artic_Minion/2020-07-03_Run_5_ARTIC/2020-07-03_Run_5_ARTIC/ARTIC_RESULTS"

snakemake -s ARTIC_ONT.py \
    --core 1 \
    --config \
        BARCODEpath=$path_barcoding \
        RESULTpath=$output_dir
