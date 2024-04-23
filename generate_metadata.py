import pandas as pd
import sys
import os
import re

# 
print("This script will prompt you and help you create a metadata table to run the pipeline")
print("If it doesn't work, just create the metadata table yourself")
srcdir = input("Directory with the original fastq files: ")
if not os.path.exists(srcdir):
    print(f"Directory {srcdir} does not exist", file=sys.stderr)
    sys.exit(1)
# Find all fastq files
files = [os.path.join(srcdir, f) for f in os.listdir(srcdir) if f.endswith('.fastq')]
print(f"Found {len(files)} fastq files in {srcdir}")

basenames = [os.path.basename(f) for f in files]
new_basenames = basenames

def regex_helper_fn(regex, x):
    all_groups =  re.search(regex, x).groups()
    # Add extension to the last group
    # Concatenate all groups
    return ''.join(all_groups) + os.path.splitext(x)[1]

while True:
    rename = input("Do you want to rename the files? (Y/n): ")
    if rename.lower() != 'n':
        print("Please, provide a regex that captures the new name")
        print("For example, if the file is 'AAA_sample1_BBB.fastq' , you can use the regex 'AAA_(.*)_BBB.+' to capture 'sample1'")
        regex = input("Regex: ")
        new_basenames = [regex_helper_fn(regex, f) for f in basenames]
        print("Old names:", basenames)
        print("New names:", new_basenames)
        print("Do the new names look good?")
        confirm = input("Confirm (Y/n): ")
        if confirm.lower() != 'n':
            break

print("Now we are going to symlink the files to a new directory?")
dstdir = input("Directory to symlink the files: ")
if not os.path.exists(dstdir):
    os.makedirs(dstdir)
for src, dst in zip(files, new_basenames):
    src = os.path.abspath(src)
    dst = os.path.abspath(os.path.join(dstdir, dst))
    os.symlink(src, dst)

print("Creating metadata table")
samples = [os.path.splitext(f)[0] for f in new_basenames]
data = {'sample_id': samples, 'foo': 'bar'}
df = pd.DataFrame(data)
print("Where should the metadata table be saved?")
metadata_file = input("Metadata file (leave empty to print to stdout): ")
if metadata_file:
    df.to_csv(metadata_file, index=False)
else:
    df.to_csv(sys.stdout, index=False)
