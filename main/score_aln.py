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
	Blosum={}

	fi=open(nameFile,"r")
	ligne=fi.readline()
	while ligne[0]=="#":
		ligne=fi.readline()
	ligneAA=ligne.split()
	ligneAA=ligneAA[0:len(ligneAA)] #-1] I commented that because some pair-wises were not in dict (show in next python cell)
	ligne=fi.readline()
	while len(ligne)>0:
		ligne=ligne.split()
		for j in range(0,len(ligneAA)-1,1):
			Blosum[ligne[0]+ligneAA[j]] = ligne[j+1]
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
	L = len(SeqsM[0]) # aligned sequence sizes (columns)
	n = len(SeqsM) # number of sequences in clusters (lines)
	s = 0 # initiate the score
	
	for col in tqdm(range(L)):
		for seq1 in range(n):
			for seq2 in range(seq1+1, n):
				seq1p = SeqsM[seq1]
				seq2p = SeqsM[seq2]

				if seq1p[col] != '-' and seq2p[col] != '-':
					s1 = seq1p[col]
					s2 = seq2p[col]
					s += calculeScore(s1, s2, blosum)
				else:
					s += gap
						
	return s/(L*n)


#==================================================================================================================
#                                               MAIN
#==================================================================================================================

def main():
    usage = "python ck_parser.py -i <input_file> -b <blosum_file> -o <output_dir> \n" 
    parser = OptionParser(usage)
    parser.add_option("-i", "--input_file", dest="input_file", help="the folder with the alignement files")
    parser.add_option("-b", "--blosum_file", dest="blosum_file", help="the BLOSUM matrix file to use")
    parser.add_option("-o", "--output_file", dest="output_file", help="the output CSV file to write the scores")
         
    (options, args) = parser.parse_args()
    folder_aln = options.input_file
    blosum = options.blosum_file
    output_file = options.output_file

    blosum = readBlosum(blosum)
	
    if folder_aln:
		
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
			
            dict_scores[CK] = score
    else:
        print("error with -i : please provide a folder with alignements")
	
    # Save dict_scores to CSV
    df = pd.DataFrame(list(dict_scores.items()), columns=['filename', 'score'])
    df.to_csv(output_file, index=False)
     
#==================================================================================================================
if __name__ == "__main__":
	main()