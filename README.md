# evolution-simulation-pipeline_Ne_and_generations
This is the evolution simulator to compute populations with all possible ranges of Ne, generations and mutations. It creates sets of sequences with different evolution parameters

This pipeline is the part of bioengineering and bioinformatics faculty coursework

## Before you start

The pipeline is available only for <i>Linux</i> users </br>
Make sure that you have installed all components:
<ul>
<li>Python 3.6 or upper https://www.python.org/
<li>Biopython 1.70 or upper http://biopython.org/
<li>R and R-Studio with basic packages https://www.rstudio.com/
</ul>


## Getting started

### Installation

First of all you have to ```clone``` this directory</br></br>
```git clone https://github.com/Pavel-Kravchenko/evolution-simulation-pipeline_Ne_and_generations/```</br></br>
Then ```cd``` in evolution-simulation-pipeline_Ne_and_generations</br></br>
```cd evolution-simulation-pipeline_Ne_and_generations```</br></br>
And ```tar``` Species_files.tar.gz</br></br>
```tar -xvf evolution-simulation-pipeline_Ne_and_generations.tar.gz```</br></br>
Command ```ls -1``` and make sure that you have all files in your directory
```
alignment_reader_script.py
evolution-simulation-pipeline_Ne_and_generations.tar.gz
heatmap_df_maker.py
README.md
R_plot.R
run_script.sh
simulation_script.py
```
Now you are ready to start.
To check, command 
```bash run_script.sh``` and wait until the program is completed.
</br></br>
!!!You may have to wait a couple of hours!!!</br></br>

It has to create ``./Files`` directory and archive it to ``archive.tar``
You are expected to receive such demo results in ./Files:

```
out_log_file_1.txt
out_log_file_2.txt
out_log_file_4.txt
simulation_heteroplasmy|cycles_128|species_128|mutations_1_0.25
simulation_heteroplasmy|cycles_128|species_128|mutations_2_0.25
simulation_heteroplasmy|cycles_128|species_128|mutations_4_0.25
simulation_heteroplasmy|cycles_128|species_16|mutations_1_0.25
simulation_heteroplasmy|cycles_128|species_16|mutations_2_0.25
simulation_heteroplasmy|cycles_128|species_16|mutations_4_0.25
simulation_heteroplasmy|cycles_128|species_2|mutations_1_0.25
simulation_heteroplasmy|cycles_128|species_2|mutations_2_0.25
simulation_heteroplasmy|cycles_128|species_2|mutations_4_0.25
simulation_heteroplasmy|cycles_128|species_32|mutations_1_0.25
simulation_heteroplasmy|cycles_128|species_32|mutations_2_0.25
simulation_heteroplasmy|cycles_128|species_32|mutations_4_0.25
simulation_heteroplasmy|cycles_128|species_4|mutations_1_0.25
simulation_heteroplasmy|cycles_128|species_4|mutations_2_0.25
simulation_heteroplasmy|cycles_128|species_4|mutations_4_0.25
simulation_heteroplasmy|cycles_128|species_64|mutations_1_0.25
simulation_heteroplasmy|cycles_128|species_64|mutations_2_0.25
simulation_heteroplasmy|cycles_128|species_64|mutations_4_0.25
simulation_heteroplasmy|cycles_128|species_8|mutations_1_0.25
simulation_heteroplasmy|cycles_128|species_8|mutations_2_0.25
simulation_heteroplasmy|cycles_128|species_8|mutations_4_0.25
simulation_heteroplasmy|cycles_16|species_128|mutations_1_0.25
simulation_heteroplasmy|cycles_16|species_128|mutations_2_0.25
simulation_heteroplasmy|cycles_16|species_128|mutations_4_0.25
simulation_heteroplasmy|cycles_16|species_16|mutations_1_0.25
simulation_heteroplasmy|cycles_16|species_16|mutations_2_0.25
simulation_heteroplasmy|cycles_16|species_16|mutations_4_0.25
simulation_heteroplasmy|cycles_16|species_2|mutations_1_0.25
simulation_heteroplasmy|cycles_16|species_2|mutations_2_0.25
simulation_heteroplasmy|cycles_16|species_2|mutations_4_0.25
simulation_heteroplasmy|cycles_16|species_32|mutations_1_0.25
simulation_heteroplasmy|cycles_16|species_32|mutations_2_0.25
simulation_heteroplasmy|cycles_16|species_32|mutations_4_0.25
simulation_heteroplasmy|cycles_16|species_4|mutations_1_0.25
simulation_heteroplasmy|cycles_16|species_4|mutations_2_0.25
...
```

``out_log_file_1.txt`` contains the Kendall's rank correlation tau table

```
Spe\Gen	2	4	8	16	32	64	128	
2	NA	NA	NA	NA	NA	NA	NA	
4	NA	NA	NA	NA	NA	NA	NA	
8	NA	NA	NA	NA	NA	NA	NA	
16	NA	NA	NA	NA	-0.269	NA	-0.38	
32	NA	NA	NA	-0.336	-0.444	-0.152	-0.223	
64	NA	NA	NA	NA	-0.285	-0.149	-0.367	
128	NA	NA	NA	NA	-0.328	-0.324	-0.213		
```
To create your populations and analyze them, change necessary parameters in run_script.sh and heatmap_df_maker.py
You may variate following parameters:</br></br>
In run_script.sh
<ul>
<li>mask=0.25
</ul>
In heatmap_df_maker.py
<ul>
<li>round_ = 3
<li>pvalue_stop = 0.05
</ul>
In alignment_reader_script.py
<ul>
<li>round_ = 4
</ul>
In simulation_script.py
<ul>
<li>length_of_sequence = 1000
<li>round_ = 4
</ul>

When you change generation, species or mutation parameters in run_script.sh, do not forget to change the same parameters (iter_ = mutation, species = species, generation = generation) in heatmap_df_maker.py.

## Contact me

Feel free to contact me for any suggestions or critique.

Email: pavel-kravchenk0[@]yandex[dot]ru

Site: http://kodomo.fbb.msu.ru/~pavel-kravchenko/index.html 

