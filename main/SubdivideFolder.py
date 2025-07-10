import os
import shutil
from collections import defaultdict
from tqdm import tqdm
from optparse import OptionParser
import pandas as pd


def print_infos(output):
    '''affiche le nombre de sous-dossiers créée et leur taille'''
    folder_stats = []
    for folder_name in os.listdir(output):
        folder_path = os.path.join(output, folder_name)
        if os.path.isdir(folder_path):
            total_size = 0
            file_count = 0
            for dirpath, dirnames, filenames in os.walk(folder_path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
                    file_count += 1
            folder_stats.append((folder_name, total_size, file_count))

    for name, size, count in folder_stats:
        print(f"{name}: {size} octets, {count} fichiers")


def subdivide_folder_by_size(input_dir, output_dir, n_subdivided):
    """
    Subdivide a folder into n_subdivided subfolders with balanced total file size.
    """
    files = [(f, os.path.getsize(os.path.join(input_dir, f))) for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
    files_sorted = sorted(files, key=lambda x: x[1], reverse=True) # on classe les fichiers par taille décroissante

    subfolders = []
    subfolder_sizes = []

    # Crée les sous-dossiers de sortie et initialise leur taille totale à 0
    for i in range(n_subdivided):
        subfolder_name = f"subfolder_{i+1}"
        subfolder_path = os.path.join(output_dir, subfolder_name)
        os.makedirs(subfolder_path, exist_ok=True)
        subfolders.append(subfolder_path)
        subfolder_sizes.append(0)

    # Pour chaque fichier (du plus gros au plus petit), l'affecte au sous-dossier le moins rempli
    for fname, fsize in tqdm(files_sorted):
        idx = subfolder_sizes.index(min(subfolder_sizes))  # Cherche le sous-dossier avec la plus petite taille totale 
        dst_folder = subfolders[idx]
        src_path = os.path.join(input_dir, fname)
        dst_path = os.path.join(dst_folder, fname)
        shutil.copy2(src_path, dst_path)  # Copie le fichier dans le sous-dossier choisi
        subfolder_sizes[idx] += fsize    # Met à jour la taille totale du sous-dossier

    print_infos(output_dir)

#==================================================================================================================
#                                               MAIN
#==================================================================================================================

def main():
     usage = "python subdivide_folder.py -i <input_dir> -o <output_dir> -n <n_subdivided> \n" 
     parser = OptionParser(usage)
     parser.add_option("-i", "--input_dir", dest="input_dir", help="a big folder that you want to subdivide")
     parser.add_option("-o", "--output_dir", dest="output_dir", help="output direction to save subdivided folders")
     parser.add_option("-n", "--n_subdivided", dest="n_subdivided", help="number of subdivisions")

      
     (options, args) = parser.parse_args()
     input_dir = options.input_dir
     output_dir = options.output_dir
     n_sub = int(options.n_subdivided)


     subdivide_folder_by_size(input_dir, output_dir, n_sub)



#==================================================================================================================
if __name__ == "__main__":
	main()





