import os
import numpy as np
from common.io.writeToa import readToa


def check_toa_all(ref_dir, out_dir, prefix="ism_toa_isrf_", threshold=1e-4):
    """
    Automatically check TOA reference vs output for all available bands.

    Parameters
    ----------
    ref_dir : str
        Directory containing reference TOA files.
    out_dir : str
        Directory containing output TOA files.
    prefix : str
        Common prefix of TOA files (default: "l1b_toa_").
    threshold : float
        Relative tolerance (default: 1e-4 = 0.01%).
    """

    # Get sorted lists of reference and output files
    ref_files = sorted([f for f in os.listdir(ref_dir) if f.startswith(prefix)])
    out_files = sorted([f for f in os.listdir(out_dir) if f.startswith(prefix)])

    print(f"Found {len(ref_files)} reference files and {len(out_files)} output files.\n")

    # Iterate over matched pairs
    for ref_file, out_file in zip(ref_files, out_files):
        print(f"--- Checking: {ref_file} ---")

        # Read data
        toa_ref = readToa(ref_dir, os.path.join(ref_dir, ref_file))
        toa_out = readToa(out_dir, os.path.join(out_dir, out_file))

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
    ref_dir=r'C:\Users\Simone\OneDrive\Documenti\Desktop\my_output_ism0910',
    out_dir=r"C:\Users\Simone\OneDrive\Documenti\Desktop\Earth Observation\EODP-TS-ISM\output"
)




