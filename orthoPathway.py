import pandas as pd
import numpy as np
import argparse

#Given orthofinder output orthogroups, inputFile with genes and annotations, and source species name,
#Returns a df corresponding to all orthologs and paralogs of a gene at every step in the input metabolic pathway
def orthoGroupSearch(orthoGroups, inputFile, sourceSpecies):
    output = pd.DataFrame(index=range(len(inputFile)),columns=['sourceGene'] + list(orthoGroups.columns[1:]) + ['inferred annotation'])
    geneList = inputFile.iloc[:,1].to_list()
    annotationList = inputFile.iloc[:,2].to_list()

    #designed to be resistant to case
    col = ""
    for header in orthoGroups.columns:
        if sourceSpecies.lower() == header.lower():
            col = str(header)
            break
    if len(col) == 0:
        raise ValueError("Source species not found in orthogroups dataframe columns")
    
    #searches for any orthogroup with a gene of interest, inserts it in its index in the pathway
    column = orthoGroups[col]
    for i in range(len(column)):
        for gene in geneList:
            if type(column[i]) == str and gene.lower() in column[i].lower():
                step = geneList.index(gene)
                output.loc[step, 'sourceGene'] = gene
                for s in orthoGroups.iloc[i,1:].index:
                    output.loc[step, s] = orthoGroups.iloc[i][s]
                output.loc[step, 'inferred annotation'] = annotationList[step]
    return output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("orthogroups", help="tsv with rows of orthogroups, each column represents a species, each cell contains all paralogs (directly from orthofinder output)",type=str)
    parser.add_argument("inputFile", help="csv with rows of queries consisting of gene alias, gene name, and annotation (manually constructed)", type=str)
    parser.add_argument("species", help="species name as it is spelled in orthofinder result column headers (e.g, athaliana), not case sensitive",type=str)
    args = parser.parse_args()
  
    orthoGroups = pd.read_csv(args.orthogroups, sep='\t')
    inputFile = pd.read_csv(args.inputFile)
    sourceSpecies = args.species

    orthoGroupSearch(orthoGroups, inputFile, sourceSpecies).to_csv('orthoPathwayResults.csv', index=False)

if __name__ == "__main__":
  main()

