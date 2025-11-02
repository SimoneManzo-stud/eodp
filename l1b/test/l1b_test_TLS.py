import numpy as np
import matplotlib.pyplot as plt
from common.io.writeToa import readToa

indir_ref = r"C:\Users\Simone\OneDrive\Documenti\Desktop\myoutputs\myoutput_L1B_1610"
indir_out = r"C:\Users\Simone\OneDrive\Documenti\Desktop\myoutputs\myoutput_ism_1610"
bands = ["VNIR-0", "VNIR-1", "VNIR-2", "VNIR-3"]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for i, band in enumerate(bands):
    file_ref = f"{indir_ref}\\l1b_toa_{band}.nc"
    file_out = f"{indir_out}\\ism_toa_isrf_{band}.nc"

    toa_ref = readToa(indir_ref, file_ref)
    toa_out = readToa(indir_out, file_out)

    row_idx = toa_ref.shape[0] // 2
    row_ref = toa_ref[row_idx, :]
    row_out = toa_out[row_idx, :]
    x = np.arange(toa_ref.shape[1])

    ax = axes[i]
    ax.plot(x, row_ref, label="L1B_TOA")
    ax.plot(x, row_out, "--", label="ISM_TOA_ISRF")
    ax.set_title(band)
    ax.set_xlabel("Column index")
    ax.set_ylabel("TOA Value")
    ax.grid(True)
    ax.legend()

plt.suptitle("Comparison of Central Row for L1B_TOA vs ISM_TOA_ISRF", fontsize=14)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

