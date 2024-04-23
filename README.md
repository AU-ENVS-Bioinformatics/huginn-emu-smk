# Snakemake workflow: EMU-smk

This is the Huginn version of the EMU snakemake workflow. Basically, it's just two files, a minimal snakemake file that refers to the one in [Github](https://github.com/AU-ENVS-Bioinformatics/emu-smk/) and a configuration file already "configured" to huginn. Please, refer to the public repo for more information. 

## Usage

1. Preparate the metadata sheet. 
2. Run the pipeline
3. Download the RDS file with a phyloseq object ready to analyze.  

```bash
snakemake --use-conda -n
snakemake --use-conda -c100
```

