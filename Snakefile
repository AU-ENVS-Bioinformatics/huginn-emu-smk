from snakemake.utils import min_version
import re
from pathlib import Path

min_version("6.0")


configfile: "config.yaml"


module emu:
    snakefile:
        github(
            "AU-ENVS-Bioinformatics/emu-smk",
            path="workflow/Snakefile",
            # TODO: add tag version
            branch="main",
        )
    config:
        config


use rule * from emu


