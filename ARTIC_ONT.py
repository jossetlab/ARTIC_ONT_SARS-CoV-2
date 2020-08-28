import os
import glob

configfile : "config/config.yaml"

BC_path=config['BARCODEpath']
if (BC_path[-1] != "/"):
	BC_path=BC_path+"/"

results_path=config['RESULTpath']
if (results_path[-1] != "/"):
	results_path=results_path+"/"

#get all barcodes in a list after demultiplexing
barcode_list = glob.glob(BC_path+"barcode*")
BARCODE=[]
for BC in barcode_list:
	barcode=str(os.path.basename(BC))
	BARCODE.append(barcode)

rule pipeline_output:
    input:
        filter_fastq = expand(results_path+"FILTER/{barcode}/merged.fastq"  ,barcode=BARCODE),

rule filter:
    message:
        "filter fastq."
    input:
        #lambda wildcards: expand(BC_path+"{barcode}", barcode=BARCODE) {params.path}
        BC_path+"{barcode}"
    output:
        filter_fastq = results_path+"FILTER/{barcode}/merged.fastq" 
    params:
        path = BC_path+"{barcode}"     
    shell:
        """
            artic guppyplex --skip-quality-check --min-length 400 --max-length 700 \
                --directory {input} --prefix run_name --output {output}
        """