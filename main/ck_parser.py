from optparse import OptionParser
from tqdm import tqdm
import pandas as pd
import os

#==================================================================================================================

def writer_tab(df, output : str ):
	"""
	writes the panda table as a csv in the output file

	args:
	"df" : the panda table that you need to write
	"output" : path for the outuput 
	"""

	df.to_csv(os.path.abspath(output),index=False)	
      
#==================================================================================================================

def read_multi_fasta_info(path, keyword = 'hypothetical'):
    """
    return the number of seq of the file with the mean of the sequences sizes
    path : folder direction of the fasta sequences for each CK
    keyword : a str to compute the percentage of sequence contains the keyword in the cluster
    - - -
    next upgrade
    # add a format = 60 ?
    """
    with open(path) as f:

        seq = []
        seq_len = 0
        p = 0

        for line in f:
            line = line.strip()
            
            if line.startswith('>'):
                text = str(line)
                product = text.split('!')[-1]   

                if keyword in product:
                    p += 1       

                if seq_len > 0:
                    seq.append(seq_len)
                seq_len = 0
            else:
                seq_len += len(line)
                
        if seq_len > 0:
            seq.append(seq_len)

        return len(seq), sum(seq)/len(seq), seq, p/len(seq)
      
#==================================================================================================================
#                                               MAIN
#==================================================================================================================

def main():
     usage = "python ck_parser.py -i <input_file> -o <output_dir> -k <keyword> \n" 
     parser = OptionParser(usage)
     parser.add_option("-i", "--input_file", dest="input_file", help="a csv that you want to parsed")
     parser.add_option("-o", "--output_dir", dest="output_dir", help="the path of the data will be saved")
     parser.add_option("-k", "--keyword", dest="keyword", default="hypothetical", help="keyword to compute the percentage of sequences containing it (default: 'hypothetical')")
          
     (options, args) = parser.parse_args()
     folder_fasta = options.input_file
     output_dir = options.output_dir
     keyword = options.keyword

     list_f = [f for f in os.listdir(os.path.abspath(folder_fasta)) if os.path.isfile(os.path.join(folder_fasta, f))]

     with open(os.path.abspath(output_dir),'w', encoding='utf-8') as f:

          f.write(f"ClusterNumber,n,mean,std,min,max, %_keyword={keyword}\n")

          for elm in tqdm(list_f):
               n, m, l, p = read_multi_fasta_info(os.path.join(folder_fasta, elm), keyword)

               ck = str(elm)#[:-14]

               if len(l) > 1:
                    variance = sum((x - m) ** 2 for x in l) / (len(l) - 1)
                    std_dev = variance ** 0.5
               else:
                    std_dev = 0.0

               row = f"{ck},{n},{round(m,3)}, {round(std_dev, 3)}, {min(l)},{max(l)}, {round(p*100,3)},\n"
               f.write(row)

     print(f"File is saved to {os.path.abspath(output_dir)}")


#==================================================================================================================
if __name__ == "__main__":
	main()
