# Import observations from Bufr 001/xx102 of NCEP's observations tanks


## Introduction
Sandbox for importing bufr observations from tank 001/xx102 of NCEP

## Installation

Clone the code
```
git clone https://github.com/flampouris/ImportBufr001102.git
```
Required python modules
```
matplotlib
cartopy
numpy as np
datetime
ncepbufr
```

To install the ncepbufr
```
git clone https://github.com/JCSDA/py-ncepbufr.git
pip install py-ncepbufr
```

## Use

Update the following two variables in importbufr.py
```
filename='../test/b001/xx102' #Complete path of the dataset location and filename
varname='SGWH' #Variable name to be imported; user can define more than one but they should belong to the same replication.
```

The imported data are in the dictionary "values". The keys of the dictionary are *longitude*, *latitude*, *date*, and the *mnemonics* at "varname".


### Lisence
Latest Version of GNU
Copyright (C) 2018 Flampouris 
Washington, DC, USA, Earth
