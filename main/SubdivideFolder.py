import os
import shutil
from collections import defaultdict
from tqdm import tqdm

def print_infos(output):
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
    files_sorted = sorted(files, key=lambda x: x[1], reverse=True)

    subfolders = []
    subfolder_sizes = []

    for i in range(n_subdivided):
        subfolder_name = f"subfolder_{i+1}"
        subfolder_path = os.path.join(output_dir, subfolder_name)
        os.makedirs(subfolder_path, exist_ok=True)
        subfolders.append(subfolder_path)
        subfolder_sizes.append(0)

    for fname, fsize in tqdm(files_sorted):
        idx = subfolder_sizes.index(min(subfolder_sizes))
        dst_folder = subfolders[idx]
        src_path = os.path.join(input_dir, fname)
        dst_path = os.path.join(dst_folder, fname)
        shutil.copy2(src_path, dst_path)
        subfolder_sizes[idx] += fsize


