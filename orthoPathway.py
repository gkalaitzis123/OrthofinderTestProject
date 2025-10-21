import pandas as pd
import numpy as np
import argparse

#Given orthofinder output orthogroups, source gene, annotation of gene, and source species name,
#Returns a row corresponding to all orthologs and paralogs of a gene at a step in a metabolic pathway
def orthoGroupSearch(orthoGroups, gene, annotation, sourceSpecies):
    #designed to be resistant to case
    col = ""
    for header in orthoGroups.columns:
        if sourceSpecies.lower() == header.lower():
            col = str(header)
            break
    if len(col) == 0:
        raise ValueError("Source species not found in orthogroups dataframe columns")
    
    #searches for row with gene of interest
    column = orthoGroups[col].to_numpy()
    index = -1
    for i in range(len(column)):
        if type(column[i]) == str and gene.lower() in column[i].lower():
            index = i
            break

    #constructing output
    output = pd.DataFrame(index=[0])
    output['sourceGene'] = gene
    if index == -1:
        for s in orthoGroups.columns[1:]:
            output.loc[0, s] = np.nan
        output.loc[0, 'inferred annotation'] = annotation
        return output

    for s in orthoGroups.iloc[index,1:].index:
        output[s] = orthoGroups.iloc[index,1:][s]
    output['inferred annotation'] = annotation
    return output

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("orthogroups", help="tsv with rows of orthogroups, each column represents a species, each cell contains all paralogs (directly from orthofinder output)",type=str)
  parser.add_argument("inputFile", help="csv with rows of queries consisting of gene alias, gene name, and annotation (manually constructed)", type=str)
  parser.add_argument("species", help="species name as it is spelled in orthofinder result column headers (e.g, athaliana), not case sensitive",type=str)
  args = parser.parse_args()
  
  data = pd.read_csv(args.orthogroups, sep='\t')
  inputFile = pd.read_csv(args.inputFile)
  sourceSpecies = args.species
  
  df = pd.DataFrame()
  for row in inputFile.to_numpy():
      gene, annotation = row[1],row[2]
      df = pd.concat([df, orthoGroupSearch(data, gene, annotation, sourceSpecies)], axis=0)
  df.to_csv('orthoPathwayResults.csv', index=False)

if __name__ == "__main__":
  main()