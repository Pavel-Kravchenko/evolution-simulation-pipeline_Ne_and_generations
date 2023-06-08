
# coding: utf-8

# In[ ]:

import sys
from sys import argv
import os

home_directory = os.getcwd()

round_ = 3
pvalue_stop = 0.05
list_dir = os.listdir(path=home_directory)
#print(list_dir)

for iter_ in [1, 2, 4, 8, 16, 32, 64]:
    d = {}
    for directory in list_dir:
        if os.path.exists(directory):
            if os.path.isdir(directory):
                list_name = directory.split("|")
                if len(list_name) >= 4:
                    generation = int(list_name[1][7:])
                    species = int(list_name[2][8:])
                    mutations = int(list_name[3][10:].split("_")[0])
                    id_dir = (species, generation, mutations)
                    #print(id_dir)
                    #print(generation)
                    #print(species)
                    #print(mutations)
                os.chdir(directory)
                try:
                    with open("Kendall_test.txt", 'r') as f:
                        file_K = [x.strip() for x in f.readlines() if len(x.strip()) != 0]
                        #print(file_K)
                        info_Kendall = (file_K[2], file_K[6])
                        #print(info_Kendall)
                        d[id_dir] = info_Kendall
                except IOError as e:
                    #print("File Kendall_test.txt does not exists!")
                    pass
                os.chdir(home_directory)
    #print(d)
    #print(d.keys())
    l_out = []
    collector = []
    for species in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
        for generation in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
            for mutation in [iter_]:
                key = (species, generation, mutation)
                #print(key)
                if key in d.keys():
                    try:
                        kendall = float(d[key][1])
                        #print(kendall)
                        #print(d[key][0])
                        pvalue = d[key][0].split("p-value")[1][2:].strip()
                        #print(pvalue)
                        if float(pvalue) < pvalue_stop:
                            print("OK")
                            kendall = round(kendall, round_)
                            collector.append(str(kendall))
                            print(kendall)
                        if float(pvalue) >= 0.05: 
                            collector.append("NA") 
                    except ValueError as v:
                         collector.append("NA")
                if key not in d.keys():
                    collector.append("NA")
        #print(l_out)
        l_out.append(collector)   
        collector = []
    #print(l_out)
    l_out.insert(0, ["2", "4", "8", "16", "32", "64", "128", "256", "512", "1024"])
    #print(l_out)

    calc = 1
    with open("out_log_file_" + str(iter_) + ".txt", "w") as out_log_file:
        for i in l_out:
            if calc == 1:
                out_log_file.write("Spe\Gen" + "\t")
            if calc != 1:
                out_log_file.write(str(calc) + "\t")
            for j in i:
                out_log_file.write(j + "\t")
            out_log_file.write("\n")
            calc = calc * 2
            #print(calc)
    out_log_file.close()
    print("")



