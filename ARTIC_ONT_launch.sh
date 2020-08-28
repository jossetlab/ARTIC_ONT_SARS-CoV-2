


path_barcoding="/srv/nfs/ngs-stockage/NGS_Virologie/CGINEVRA/Artic_Minion/2020-07-03_Run_5_ARTIC/2020-07-03_Run_5_ARTIC/barcoding"


snakemake -s ARTIC_ONT.py \
    --core 10 \
    --config \
        BARCODEpath=$path_barcoding
