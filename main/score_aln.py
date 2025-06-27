from optparse import OptionParser
from tqdm import tqdm
import os
import pandas as pd

#==================================================================================================================

def readBlosum(nameFile):
	"""
	Input1 nameFile : blosum file name
	Output1 Blosum: a dictionary containing BLOSUM matrix, key is a pair of amino acids (alphabetic order) and value is the substitution value. 
	REMARK : You should eliminate the last four columns and last four rows of Blosum file
	"""
	Blosum = {}
	fi = open(nameFile,"r")
	ligne = fi.readline()

	while ligne[0] == "#":
		ligne = fi.readline()

	ligneAA = ligne.split()
	ligneAA = ligneAA[0:len(ligneAA)]
	ligne = fi.readline() 

	while len(ligne) > 0:
		ligne = ligne.split()

		for j in range(0,len(ligneAA)-1,1):
			Blosum[ligne[0]+ligneAA[j]]= ligne[j+1]
		ligne=fi.readline()
	fi.close()
	return Blosum


#==================================================================================================================

def calculeScore(AA,AA2,blosum):
	score=0
	try :
		score=blosum[AA+AA2]
	except : 
		score = blosum[AA2+AA]
	return int(score)
#==================================================================================================================

def extraireAllFastaMulti(fileName):  
	"""
	Read a FASTA file with several sequences
	input1 fileName: file name
	output1 IdSeq: list of sequences IDs
	output2 Seqs: sequences   
	"""
	f = open(fileName,'r')
	B=False
	Seqs=[]
	se=""
	IdSeq=[]
	CurrentLine  = f.readline()
	while CurrentLine != "":
		if CurrentLine[0] != ">"  :
			se=se+CurrentLine.rstrip("\n")
			B=True
		else:
			IdSeq.append(CurrentLine.rstrip("\n")[1:])
			if B:
				Seqs.append(se)
				se=""
		CurrentLine  = f.readline()
	Seqs.append(se)    
	f.close()
	return IdSeq, Seqs

#==================================================================================================================


def SP_score(SeqsM, blosum, gap=-5):
	"""
	Compute MSA score based on a substitution matrix and gap penality
	input1 SeqsM: list of aligned sequences
	input2 blosum: substitution matrix
	input3 gap: gap penality
	output1 score: MSA score
	"""
	Long = len(SeqsM[0])
	s = 0
	n = len(SeqsM)

	for p in range(Long):
		for seq1 in range(len(SeqsM)) :
			for seq2 in range(seq1+1,len(SeqsM)):
				seq1p = SeqsM[seq1]
				seq2p = SeqsM[seq2]
				if p < len(seq1p) and p < len(seq2p) and seq1p[p] != '-' and seq2p[p] != '-':
					s1 = seq1p[p]
					s2 = seq2p[p]
					s += calculeScore(s1, s2, blosum)
				else :
					s += gap
	return s, n, Long

#==================================================================================================================
#                                               MAIN
#==================================================================================================================

def main():
    usage = "python ck_parser.py -i <input_file> -b <blosum_file> -o <output_dir> \n" 
    parser = OptionParser(usage)
    parser.add_option("-i", "--input_file", dest="input_file", help="the folder with the alignement files")
    parser.add_option("-b", "--blosum_file", dest="blosum_file", help="the BLOSUM matrix file to use")
    parser.add_option("-o", "--output_file", dest="output_file", help="the output CSV file to write the scores")
    parser.add_option('-s', '--smallest', dest='smallest', type='int', default=1, help='Number of smallest files to process (by size). If 0, process all files.')
         
    (options, args) = parser.parse_args()
    folder_aln = options.input_file
    blosum = options.blosum_file
    output_file = options.output_file
    born_smallest = options.smallest

    blosum = readBlosum(blosum)
	
    if folder_aln:

  
        files_with_sizes = [(f, os.path.getsize(os.path.join(folder_aln, f))) for f in os.listdir(folder_aln) if os.path.isfile(os.path.join(folder_aln, f))]
        files_with_sizes_sorted = sorted(files_with_sizes, key=lambda x: x[1])
        set_50_1st = files_with_sizes_sorted[:born_smallest]

        interet = [f for f, s in set_50_1st]





        list_f = [f for f in os.listdir(folder_aln) if os.path.isfile(os.path.join(folder_aln, f))]
		
        len_file = len(list_f)
        dict_scores = {}
        i = 1

        for CK in list_f:
            print("Processing.", CK, "file ", i,"/",len_file )
            i += 1
            fileName = os.path.join(folder_aln, CK)

            IdSeq, Seqs = extraireAllFastaMulti(fileName)
            score = SP_score(Seqs, blosum, gap=-5)
			
            dict_scores[CK] = scorehro
    else:
        print("error with -i : please provide a folder with alignements")
	
    # Save dict_scores to CSV
    df = pd.DataFrame(list(dict_scores.items()), columns=['filename', 'score'])
    df.to_csv(output_file, index=False)
     
#==================================================================================================================
if __name__ == "__main__":
	main()