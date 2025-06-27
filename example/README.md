
# **cluster_parser.py**

## Data as input
> **Reminder:** Check the [`data`](data) folder for example input files. (a folder with a file per cluster that contains a multiFasta)

```
>seq1 Fake protein 1
AKDQCLERDNVETDAKDCNRQTFVINHHYHEMRILCMCRWAWFQHWHFIWEQEHNVRMCS
RGWSMDEFIQEQLQCMKGLPSWRAKGERCHQMMGWTAFKKLWYDDHTLNWGDFISKIGQN
RHTIRY
>seq2 Fake protein 2
LHCLAWSAKIHMDIMFNCVMFHLWLLFNCGYEHQLTLSQPAKGDLQMHMTLIELKQQIWQ
AVFFLSHEGCKPCWYQQETFNPTHSHFMIYNMSMECHLNCYFQERPKLKYSRMRGEHSSR
CDGRPRWDAMMLWGPNHQAPHKEICEPPVGKALALSCFYMLNFWISWCYCFYESYGNAWE
TQPDRFYPTSLPQGVEIRGSGLNMHAHMQDHMEYGNEKGNGVHCNHCVKNRESKMPPHDW
THIDICDDGLVLCKSWQGVQKLCFQLFWPIQMTNQKHAPHPDHAKVRLGYSRCKLPNTVF
LVVGAPVKKPHPLIGRWTAMDGTVCS
>seq3 Fake protein 3
CRDLCPNYVGHLKIETDQVTCVMETNFSRAAIWVSMLRWLCQIFYVCPMFREQYQCLTPL
RMHQWKCITSCYEN
```

## How to use with the following example

```python
python main/ck_parser.py -i ".\example\data" -o ".\example\output\stats_clusters.csv" -k "10"
```

## Result

The file `stats_clusters.csv` will be created in the folder `.\example\output\`.  
You can open it with a spreadsheet program or import it into Python with pandas:

```python
import pandas as pd

df = pd.read_csv(r'.\example\output\stats_clusters.csv')
print(df.head())
```

```csv
| ClusterNumber   | n  | mean    | std     | min | max | %_keyword=10 |
|-----------------|----|---------|---------|-----|-----|--------------|
| fake_1.fasta    | 71 | 224.338 | 97.603  | 46  | 399 | 1.408        |
| fake_10.fasta   | 29 | 233.517 | 99.436  | 48  | 393 | 3.448        |
| fake_2.fasta    | 29 | 243.966 | 96.618  | 45  | 391 | 3.448        |
| fake_3.fasta    | 95 | 218.242 | 102.195 | 45  | 395 | 1.053        |
| fake_4.fasta    | 45 | 225.356 | 92.271  | 70  | 397 | 2.222        |
| fake_5.fasta    | 5  | 169.8   | 94.701  | 81  | 300 | 0.0          |
| fake_6.fasta    | 3  | 266.667 | 178.147 | 61  | 373 | 0.0          |
| fake_7.fasta    | 76 | 248.289 | 99.986  | 48  | 398 | 1.316        |
| fake_8.fasta    | 37 | 209.622 | 109.548 | 60  | 391 | 2.703        |
| fake_9.fasta    | 96 | 219.208 | 100.4   | 48  | 399 | 1.042        |
```


# **score_aln.py**

## Data as input
> **Reminder:** Check the [`data2`](data2) folder for example input files. (a folder with the alignment files)

```
>CK_Pro_MIT9313_02404|CK_00042790
LSLNTQKSRVDVLSATSVAGLASAAVIVVSA
>CK_Pro_MIT9303_16681|CK_00042790
LSLNTQKLRADVPSATSVAGLASGAVIVVSA
```

## How to use with the following example

```python
python score_aln.py -i ".\example\data2"  -b ".\example\blosum\BLOSUM62.txt" -o ".\example\output" -s 10
```

## Result

```csv
| Cluster                  | score | n | Long | score/(L*n)         |
|--------------------------|-------|---|------|---------------------|
| CK_00043857_cluster.aln  | 137   | 2 | 29   | 2.3620689655172415  |
| CK_00044462_cluster.aln  | 149   | 2 | 30   | 2.4833333333333334  |
| CK_00045049_cluster.aln  | 123   | 2 | 30   | 2.05                |
| CK_00046779_cluster.aln  | 139   | 2 | 31   | 2.2419354838709675  |
| CK_00046969_cluster.aln  | 144   | 2 | 30   | 2.4                 |
| CK_00035421_cluster.aln  | 153   | 2 | 32   | 2.390625            |
| CK_00038482_cluster.aln  | 137   | 2 | 31   | 2.2096774193548385  |
| CK_00042790_cluster.aln  | 114   | 2 | 31   | 1.8387096774193548  |
| CK_00045640_cluster.aln  | 158   | 2 | 32   | 2.46875             |
| CK_00045858_cluster.aln  | 138   | 2 | 31   | 2.225806451612903   |
```


# Supplementary 
# Supplementary
You can find two other scripts; one is generate_set_fasta.py, which can easily be found on the web to generate a folder with several files that contain random fake fasta sequences.
You can find two other scripts: one is `generate_set_fasta.py`, which can easily be found on the web to generate a folder with several files that contain random fake fasta sequences.
The other one is `SubdivideFolder.py`. You can use this simply with a clone of the repo, and import the function `subdivide_folder_by_size`.folder and the number totale of subdivision that you want to do This function takes as parameters the original folder that you want to split into many smaller ones, the `output_dir` where to locate the new folders, and the total number of subdivisions that you want to do.
