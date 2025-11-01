import os
import numpy as np
from common.io.writeToa import readToa

def check_toa_all(ref_dir, out_dir, prefix="ism_toa_ds_", threshold=1e-4):


    # Consider only .nc files
    ref_files = sorted([
        f for f in os.listdir(ref_dir)
        if f.startswith(prefix) and f.lower().endswith(".nc")
    ])
    out_files = sorted([
        f for f in os.listdir(out_dir)
        if f.startswith(prefix) and f.lower().endswith(".nc")
    ])

    print(f"Found {len(ref_files)} reference files and {len(out_files)} output files.\n")

    # Iterate over matched pairs
    for ref_file, out_file in zip(ref_files, out_files):
        print(f"--- Checking: {ref_file} ---")

        try:
            # Read data
            toa_ref = readToa(ref_dir, os.path.join(ref_dir, ref_file))
            toa_out = readToa(out_dir, os.path.join(out_dir, out_file))
        except Exception as e:
            print(f"⚠️ Skipping {ref_file} due to read error: {e}\n")
            continue

        # Compute relative difference (avoid division by zero)
        diff_rel = np.abs((toa_out - toa_ref) / np.maximum(np.abs(toa_ref), 1e-12))

        # Statistics
        mean_diff = np.mean(diff_rel)
        std_diff = np.std(diff_rel)
        cutoff = mean_diff + 3 * std_diff

        # Ratio of valid points
        valid_points = np.sum(diff_rel < threshold)
        total_points = diff_rel.size
        ratio_valid = valid_points / total_points

        # Print results
        print(f"Mean relative difference: {mean_diff:.2e}")
        print(f"Standard deviation: {std_diff:.2e}")
        print(f"3-sigma cutoff: {cutoff:.2e}")
        print(f"Valid points (< {threshold:.1e}): {ratio_valid * 100:.3f}%")

        if ratio_valid >= 0.997:  # ~3σ rule
            print("✅ Test passed: at least 99.7% of points are within 0.01% difference.\n")
        else:
            print("❌ Test failed: more than 0.3% of points exceed the 0.01% tolerance.\n")



check_toa_all(
    ref_dir=r"C:\Users\Simone\OneDrive\Documenti\Desktop\myoutputs\myoutput_ism_0910",
    out_dir=r"C:\Users\Simone\OneDrive\Documenti\Desktop\Earth Observation\EODP-TS-ISM\output"
)
