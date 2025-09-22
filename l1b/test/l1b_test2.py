import numpy as np
import matplotlib.pyplot as plt
from common.io.writeToa import readToa

# input and output directory
indir_ref = r"C:\Users\Simone\OneDrive\Documenti\Desktop\myoutput_EODP"
indir_out = r"C:\Users\Simone\OneDrive\Documenti\Desktop\Earth Observation\isrf_output"

# Bands list
bands = ["VNIR-0", "VNIR-1", "VNIR-2", "VNIR-3"]

plt.figure(figsize=(12, 8))

for band in bands:
    # file path building
    file_ref = f"{indir_ref}\\l1b_toa_{band}.nc"
    file_out = f"{indir_out}\\ism_toa_isrf_{band}.nc"

    # matrix reading
    toa_ref = readToa(indir_ref, file_ref)
    toa_out = readToa(indir_out, file_out)

    # central row index
    row_idx = toa_ref.shape[0] // 2

    # central row
    row_ref = toa_ref[row_idx, :]
    row_out = toa_out[row_idx, :]

    # X axis = column index
    x = np.arange(toa_ref.shape[1])

    # Overlapped plot for each band
    plt.plot(x, row_ref, label=f"{band} - Reference")
    plt.plot(x, row_out, "--", label=f"{band} - Output")

plt.xlabel("Column index")
plt.ylabel("TOA Value")
plt.title("Comparison of Central Row for TOA Matrices (VNIR bands)")
plt.legend()
plt.grid(True)
plt.show()

