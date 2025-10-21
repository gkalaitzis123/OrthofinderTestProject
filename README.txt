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

ORTHOSEARCH.PY

orthoSearch.py finds orthologs, co-orthologs, and paralogs using an input (orthoSearchInput.csv for example), with a gene, source species, and target species/species of interest.
The script outputs a table (orthoSearchOutput.csv for example) of gene of interest, the homolog found, and the relationship (ortholog, co-ortholog, paralog).

TO EXECUTE FROM COMMAND LINE

example - python orthoSearch.py Orthogroups.tsv orthoSearchInput.csv 1

ARGUMENTS
Orthogroups.tsv - known orthogroups (from orthofinder output)
orthoSearchInput.csv- table with with genes, source species, and target species/species of interest
include paralogs (1 for true, 0 for false)

ORTHOPATHWAY.PY

orthoPathway.py finds the orthogroup of a gene corresponding to a step in a metabolic pathway using a table (orthoPathwayInput.csv for example), with genes and their annotations.
The script outputs a table (orthoPathwayOutput.csv for example) of gene of interest, the homolog found, and the relationship (ortholog, co-ortholog, paralog).

TO EXECUTE FROM COMMAND LINE

example - python orthoPathway.py Orthogroups.tsv orthoPathwayInput.csv Athaliana

ARGUMENTS
Orthogroups.tsv - known orthogroups (from orthofinder output)
orthoPathwayInput.csv - table with with genes and their annotations (assumes shared name is second column, annotation is third column)
Athaliana - source species name as written in orthoFinder output (not case sensitive)




