
############################################################################################
# Objective:
#   Perform non-parametric hypothesis testing between abundance values in different groups

# Author: Vitalii Stebliankion (vsteb002@fiu.edu)
#   Bioinformatics Research Group (BioRG)
############################################################################################


from scipy.stats import mannwhitneyu
import pandas as pd
import PyPluMA

def test_sp(all_species, df1, df2):
    significant_species=[]
    for species in all_species:
        try:
            stat, p = mannwhitneyu(list(df1[species]), list(df2[species]))
        except ValueError:
            continue # when all numbers are identical
        if p<0.05:
            #print(species, p)
            significant_species.append(species.replace(' ','.').replace('(','X.').replace(')','.').replace('-', '.'))
    return significant_species

class MannWhitneyPlugin:
    def input(self, inputfile):
       paramfile = open(inputfile, 'r')
       self.params=dict()
       for line in paramfile:
           contents = line.strip().split('\t')
           self.params[contents[0]] = contents[1]

    def run(self):
       #df = pd.read_csv('out_abundance/abundance_group.csv')
       df = pd.read_csv(PyPluMA.prefix()+"/"+self.params['abundance'])
       group1 = self.params['group1']
       group2 = self.params['group2']
       self.all_species = list(df.columns)
       self.all_species.pop(0)
       self.all_species.pop(0)

       self.df1 = df[df['Group']==group1]
       self.df2 = df[df['Group']==group2]
       #df_control = df[df['Group']=='Control']
       #df_gwi = df[df['Group']=='GWI']
       #df_wd_control = df[df['Group']=='WD_Control']
       #df_wd_gwi = df[df['Group']=='WD_GWI']

    def output(self, outputfile):
       significant_species = test_sp(self.all_species, self.df1, self.df2)
       outfile = open(outputfile, 'w')
       outfile.write("Number of significant species: {}".format(len(significant_species)))
       for species in significant_species:
           outfile.write(species+"\n")
       #print()
       #significant_species_wd = test_sp(all_species, df_wd_control, df_wd_gwi)
       #print("Number of significant WD species: {}".format(len(significant_species_wd)))
       #print(significant_species_wd)
       #print()
       #print("All Species:")
       #print(set(significant_species+significant_species_wd))
