# evolution-simulation-pipeline_Ne_and_generations
This is the evolution simulator to calculate all possible ranges of Ne, generations and mutations

This pipeline is the part of bioengineering and bioinformatics faculty coursework, it creates the range of sequences with different evolution parameters

## Before you start

The pipeline is availble only for <i>Linux</i> users </br>
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
```bash run_script.sh``` and wait for the program to complete.
It has to create ``./Files`` directory and archive it in to ``archive.tar``
You are expected to receive such demo results in ./Files:

```
out_log_file_1.txt
out_log_file_2.txt
simulation_heteroplasmy|cycles_2|species_2|mutations_1_0.25
simulation_heteroplasmy|cycles_2|species_2|mutations_2_0.25
simulation_heteroplasmy|cycles_2|species_4|mutations_1_0.25
simulation_heteroplasmy|cycles_2|species_4|mutations_2_0.25
simulation_heteroplasmy|cycles_2|species_8|mutations_1_0.25
simulation_heteroplasmy|cycles_2|species_8|mutations_2_0.25
simulation_heteroplasmy|cycles_4|species_2|mutations_1_0.25
simulation_heteroplasmy|cycles_4|species_2|mutations_2_0.25
simulation_heteroplasmy|cycles_4|species_4|mutations_1_0.25
simulation_heteroplasmy|cycles_4|species_4|mutations_2_0.25
simulation_heteroplasmy|cycles_4|species_8|mutations_1_0.25
simulation_heteroplasmy|cycles_4|species_8|mutations_2_0.25
simulation_heteroplasmy|cycles_8|species_2|mutations_1_0.25
simulation_heteroplasmy|cycles_8|species_2|mutations_2_0.25
simulation_heteroplasmy|cycles_8|species_4|mutations_1_0.25
simulation_heteroplasmy|cycles_8|species_4|mutations_2_0.25
simulation_heteroplasmy|cycles_8|species_8|mutations_1_0.25
simulation_heteroplasmy|cycles_8|species_8|mutations_2_0.25
```
For create your populations and analyze them change necessary parameters in run_script.sh and heatmap_df_maker.py


## Contact me

Feel free to contact me for any suggestions or critique.

Email: pavel-kravchenk0@yandex.ru 

Site: http://kodomo.fbb.msu.ru/~pavel-kravchenko/index.html 

