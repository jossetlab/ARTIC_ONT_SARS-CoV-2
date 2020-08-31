import os
import glob

configfile : "config/config.yaml"

BC_path=config['BARCODEpath']
if (BC_path[-1] != "/"):
	BC_path=BC_path+"/"

results_path=config['RESULTpath']
if (results_path[-1] != "/"):
	results_path=results_path+"/"

SEQSUM_file=config['SEQSUMpath']
FAST5path=config['FAST5path']
ARTICrep=config['ARTICrep']
if (ARTICrep[-1] != "/"):
	ARTICrep=ARTICrep+"/"

#get all barcodes in a list after demultiplexing
barcode_list = glob.glob(BC_path+"barcode*")
BARCODE=[]
for BC in barcode_list:
	barcode=str(os.path.basename(BC))
	BARCODE.append(barcode)

rule pipeline_output:
    input:
        #filter_fastq = expand(results_path+"FILTER/{barcode}/merged.fastq"  ,barcode=BARCODE),
        #results = expand(results_path+"RESULTS/{barcode}/{barcode}.consensus.fasta",barcode=BARCODE),
        sumSEQ = results_path+"RESULTS/articONT_allseq.fasta",
        #covResults= expand(results_path+"COVERAGE/{barcode}.cov",barcode=BARCODE),
        summcov = results_path+"COVERAGE/COV_summary.cov"



rule filter:
    message:
        "filter fastq."
    input:
        BC_path+"{barcode}"
    output:
        filter_fastq = results_path+"FILTER/{barcode}/merged.fastq"  
    shell:
        """
            artic guppyplex --skip-quality-check --min-length 400 --max-length 700 \
                --directory {input} --prefix run_name --output {output}
        """

rule articONT:
    input:
        filter_fastq = rules.filter.output.filter_fastq
    output:
        results = results_path+"RESULTS/{barcode}/{barcode}.consensus.fasta",
        #bam = results_path+"RESULTS/{barcode}/{barcode}.primertrimmed.rg.sorted.bam"
    threads: 8
    shell:
        """
        mkdir -p {results_path}RESULTS/{wildcards.barcode}/
        artic minion --normalise 200 --threads {threads} --scheme-directory ~/artic-ncov2019/primer_schemes \
            --read-file {input.filter_fastq} \
            --fast5-directory {FAST5path} \
            --sequencing-summary {SEQSUM_file} \
            nCoV-2019/V3 {results_path}RESULTS/{wildcards.barcode}/{wildcards.barcode}
        """

rule computeCOV:
    input:
        results = rules.articONT.output.results,
        bam = results_path+"RESULTS/{barcode}/{barcode}.primertrimmed.rg.sorted.bam"
    output:
        covResults= temp(results_path+"COVERAGE/{barcode}.cov")
    shell:
        "bedtools genomecov -ibam {input.bam} -d -split | sed 's/$/\t{wildcards.barcode}\tONT/' > {output.covResults} "

rule concatCOV:
    input:
        all_covR = expand(rules.computeCOV.output.covResults,barcode=BARCODE)
    output:
        summcov = results_path+"COVERAGE/COV_summary.cov"
    shell:
        "cat {input.all_covR} > {output.summcov} "

rule concatCONS:
    input:
        cons_seq = expand(rules.articONT.output.results,barcode=BARCODE)
    output:
        sumSEQ = results_path+"RESULTS/articONT_allseq.fasta"
    shell:
        "cat {input} > {output} "