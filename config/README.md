First, prepare a metadata csv file. You can use this as an [example](../.tests/metadata.csv). It can have any arbitrary column, but it needs to have two columns: sample_id,sample_name for identifying the filename and the sample name. Again, see the [tests directory](../.tests) for an example. 

Then, edit the [configuration file](config/config.yaml) so it fits your case:

- reads_dir is the relative path to wherever your fastq files. 
- metadata_tbl is the relative or absolute path to wherever your metadata csv file. 
- emu_database is the absolute path to wherever the database you want to use. Please, [read here to know how to create that database](https://gitlab.com/treangenlab/emu#1-download-database).  