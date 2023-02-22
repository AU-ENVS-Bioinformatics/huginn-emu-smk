import sys
from pathlib import Path
with open(snakemake.log[0], "w") as f:
    sys.stderr = sys.stdout = f
    for src, dest in zip(snakemake.input, snakemake.output):
        src, dest = Path(src).absolute(), Path(dest).absolute()
        dest.parent.mkdir(parents=True, exist_ok=True)
        print(src)
        print(dest)
        dest.symlink_to(src)