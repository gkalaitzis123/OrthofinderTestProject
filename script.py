import pandas as pd
import numpy as np
import argparse

#Takes a pandas dataframe of orthogroups, gene name, source species name, target species name, and whether or not you want paralogs,
#Outputs a df with input gene, target species genes, and type of relationship in rows
def homologSearch(orthoGroups, gene, s1, s2, includeParalogs):
    data = orthoGroups.to_numpy()

    #find orthogroup of interest in orthogroups data
    sourceStr, targetStr = "", ""
    for row in data:
        for s in row[1:]:
            if type(s) == str and s2 in s:
                targetStr = s
            if type(s) == str and gene in s and s1 in s:
                sourceStr = s
        if len(sourceStr) > 0:
            break

    #constructing output, gene name is always before first '|'
    output = []
    if includeParalogs:
        for s in sourceStr.split(", "):
            if gene in s:
                continue
            output.append([gene, s.split("|")[0], 'paralog'])
    if len(targetStr.split(", ")) == 1 and len(sourceStr) > 0:
        output.append([gene, targetStr.split("|")[0], 'ortholog'])
    elif len(sourceStr) > 0:
        for s in targetStr.split(", "):
            output.append([gene, s.split("|")[0], 'co-ortholog'])

    df = pd.DataFrame(output,columns=["sourceGene","targetGene","Relationship"])

    return df

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("orthogroups", help="csv with rows of orthogroups, each column represents a species, each cell contains all paralogs (directly from orthofinder output)",type=str)
  parser.add_argument("inputFile", help="csv with rows of queries consisting of gene name, source species, and target species (manually constructed)", type=str)
  parser.add_argument("includeParalogs", help="0 for false, 1 for true",type=int)
  args = parser.parse_args()
  
  data = pd.read_csv(args.orthogroups, sep='\t')
  input = pd.read_csv(args.inputFile).to_numpy()
  includeParalogs = args.includeParalogs
  
  df = pd.DataFrame()
  for row in input:
      gene, s1, s2 = row[0],row[1],row[2]
      df = pd.concat([df, homologSearch(data, gene, s1, s2, includeParalogs)], axis=0)
  df.to_csv('output.csv', index=False)

if __name__ == "__main__":
  main()
