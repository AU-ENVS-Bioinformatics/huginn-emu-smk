# Snakemake workflow: EMU-smk

[![Snakemake](https://img.shields.io/badge/snakemake-≥6.3.0-brightgreen.svg)](https://snakemake.github.io)
[![GitHub actions status](https://github.com/AU-ENVS-Bioinformatics/emu-smk/workflows/Tests/badge.svg?branch=main)](https://github.com/AU-ENVS-Bioinformatics/emu-smk/actions?query=branch%3Amain+workflow%3ATests)


A Snakemake workflow for running [EMU](https://gitlab.com/treangenlab/emu). 


## Usage

First, prepare a metadata csv file. You can use this as an [example](.tests/metadata.csv). It can have any arbitrary column, but it needs to have two columns: sample_id,sample_name for identifying the filename and the sample name. Again, see the [tests directory](.tests) for an example. 

Then, edit the [configuration file](config/config.yaml) so it fits your case. You can [read more here](config/README.md).

Finally,

```bash
snakemake --use-conda -n
snakemake --use-conda -c100
```

