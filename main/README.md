# Data as input
> **Reminder:** Check the [`data`](./cluster_parser/example/data) folder for example input files.

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


# How to use with the following example

```python
python main/ck_parser.py -i ".\example\data" -o ".\example\output\data_saved.csv" -k "10"
```

## Result

The file `data_saved.csv` will be created in the folder `.\example\output\`.  
You can open it with a spreadsheet program or import it into Python with pandas:

```python
import pandas as pd

df = pd.read_csv(r'.\example\output\data_saved.csv')
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
