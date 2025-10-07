Specific genomes used

Arabidopsis - Araport11,

Rice - Oryza sativa v7.0,

Maize - Zea mays RefGen_V4,

Sorghum - Sorghum bicolor v5.1,

Setaria - Setaria italica v2.2,

Tomato - Solanum lycopersicum ITAG5.0


Got protein data from https://phytozome-next.jgi.doe.gov/  ({plant}.protein_primaryTranscriptOnly.fa.gz).
Unzip files using gzip, then place them in a directory together (orthofinder_input), orthofinder_inputZipped has the zipped versions of these files.

Run orthofinder on the directory using python {path to orthofinder}/orthofinder/{version}/orthofinder.py -f {path to orthofinder_input}
Or, use a script similar (orthofinder.slurm) to mine if using SLURM.
Orthogroups.csv shows the output of orthofinder on these 6 proteomes (originally a tsv).

script.py finds orthologs, co-orthologs, and paralogs using an input (input.csv for example), with a gene, source species, and target species/species of interest.
The script outputs a table (output.csv for example) of gene of interest, the homolog found, and the relationship (ortholog, co-ortholog, paralog).

TO EXECUTE FROM COMMAND LINE

example - python script.py Orthogroups.tsv Input.csv 1

ARGUMENTS
Orthogroups.tsv - known orthogroups (from orthofinder output)
Input.csv - table with with genes, source species, and target species/species of interest
include paralogs (1 for true, 0 for false)

