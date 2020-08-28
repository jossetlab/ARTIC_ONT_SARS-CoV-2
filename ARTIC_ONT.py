import os
import glob

configfile : "config/config.yaml"

datapath=config['PathToData']
BC_path=config['BARCODEpath']

#get all barcodes in a list after demultiplexing
barcode_list = glob.glob(datapath+"barcode*")
BARCODE=[]
for BC in barcode_list:
	barcode=str(os.path.basename(BC))
	BARCODE.append(barcode)

rule pipeline_output:
    input:
        filter_fastq = expand(resultpath+"FILTER/{barcode}/merged.fastq"  ,barcode=BARCODE),


rule filter:
    message:
        "filter fastq."
    input:
        lambda wildcards: expand(resultpath+"barcoding/"+"{barcode}", barcode=BARCODE)
    output:
        filter_fastq = resultpath+"FILTER/{barcode}/merged.fastq" 
    params:
        path = resultpath+"barcoding/"+"{barcode}"       
    shell:
        """
            artic guppyplex --skip-quality-check --min-length 400 --max-length 700 \
                --directory {params.path} --prefix run_name --output {output}
        """