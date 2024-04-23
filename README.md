# Snakemake workflow: EMU-smk

This is the Huginn version of the EMU snakemake workflow. Basically, it's just two files, a minimal snakemake file that refers to the one in [Github](https://github.com/AU-ENVS-Bioinformatics/emu-smk/) and a configuration file already "configured" to huginn. Please, refer to the public repo for more information. 

## Usage

1. Preparate the metadata sheet. 
2. Run the pipeline
3. Download the RDS file with a phyloseq object ready to analyze.  

```bash
conda activate snakemake
snakemake --use-conda -n --conda-prefix /software/emu-snakemake
snakemake --use-conda -c50 --conda-prefix /software/emu-snakemake
```

If you want to keep intermediate output (such as unclassified sequences in a separate fasta or the alignments) use instead:

```bash
conda activate snakemake
snakemake --use-conda -n --conda-prefix /software/emu-snakemake --notemp
snakemake --use-conda -c50 --conda-prefix /software/emu-snakemake --notemp
```