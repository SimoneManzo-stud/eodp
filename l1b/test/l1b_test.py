import matplotlib.pyplot as plt
import numpy as np
from common.io.writeToa import readToa

#TEST FOR VNIR-O
toa0= readToa(r"C:\Users\Simone\OneDrive\Documenti\Desktop\myoutput_EODP", r"C:\Users\Simone\OneDrive\Documenti\Desktop\myoutput_EODP\l1b_toa_VNIR-0.nc")
toa_out0= readToa(r'C:\Users\Simone\OneDrive\Documenti\Desktop\EODP-TS-L1B\output"', r"C:\Users\Simone\OneDrive\Documenti\Desktop\EODP-TS-L1B\output\l1b_toa_VNIR-0.nc")

# Compute relative difference, avoid division by zero using a small epsilon (1e-12)
diff_rel = np.abs((toa_out0 - toa0) / np.maximum(np.abs(toa0), 1e-12))

# Compute statistics on the relative differences
mean_diff = np.mean(diff_rel)
std_diff = np.std(diff_rel)
cutoff = mean_diff + 3 * std_diff   # 3-sigma threshold

# Define tolerance threshold: 0.01% = 1e-4 in relative terms
threshold = 1e-4

# Count valid points below the threshold
valid_points = np.sum(diff_rel < threshold)
total_points = diff_rel.size
ratio_valid = valid_points / total_points

# Print results
print(f"Mean relative difference: {mean_diff:.2e}")
print(f"Standard deviation: {std_diff:.2e}")
print(f"3-sigma cutoff: {cutoff:.2e}")
print(f"Percentage of valid points (< {threshold:.1e}): {ratio_valid*100:.3f}%")

# Check if at least 99.7% of points (≈3-sigma rule) are within the threshold
if ratio_valid >= 0.997:
    print("✅ Test passed: at least 99.7% of points are within 0.01% difference.")
else:
    print("❌ Test failed: more than 0.3% of points exceed the 0.01% tolerance.")

#TEST FOR VNIR-1
toa1= readToa(r"C:\Users\Simone\OneDrive\Documenti\Desktop\myoutput_EODP", r"C:\Users\Simone\OneDrive\Documenti\Desktop\myoutput_EODP\l1b_toa_VNIR-1.nc")
toa_out1= readToa(r'C:\Users\Simone\OneDrive\Documenti\Desktop\EODP-TS-L1B\output"', r"C:\Users\Simone\OneDrive\Documenti\Desktop\EODP-TS-L1B\output\l1b_toa_VNIR-1.nc")

# Compute relative difference, avoid division by zero using a small epsilon (1e-12)
diff_rel = np.abs((toa_out1 - toa1) / np.maximum(np.abs(toa1), 1e-12))

# Compute statistics on the relative differences
mean_diff = np.mean(diff_rel)
std_diff = np.std(diff_rel)
cutoff = mean_diff + 3 * std_diff   # 3-sigma threshold

# Define tolerance threshold: 0.01% = 1e-4 in relative terms
threshold = 1e-4

# Count valid points below the threshold
valid_points = np.sum(diff_rel < threshold)
total_points = diff_rel.size
ratio_valid = valid_points / total_points

# Print results
print(f"Mean relative difference: {mean_diff:.2e}")
print(f"Standard deviation: {std_diff:.2e}")
print(f"3-sigma cutoff: {cutoff:.2e}")
print(f"Percentage of valid points (< {threshold:.1e}): {ratio_valid*100:.3f}%")

# Check if at least 99.7% of points (≈3-sigma rule) are within the threshold
if ratio_valid >= 0.997:
    print("✅ Test passed: at least 99.7% of points are within 0.01% difference.")
else:
    print("❌ Test failed: more than 0.3% of points exceed the 0.01% tolerance.")

#TEST FOR VNIR-2
toa2= readToa(r"C:\Users\Simone\OneDrive\Documenti\Desktop\myoutput_EODP", r"C:\Users\Simone\OneDrive\Documenti\Desktop\myoutput_EODP\l1b_toa_VNIR-2.nc")
toa_out2= readToa(r'C:\Users\Simone\OneDrive\Documenti\Desktop\EODP-TS-L1B\output"', r"C:\Users\Simone\OneDrive\Documenti\Desktop\EODP-TS-L1B\output\l1b_toa_VNIR-2.nc")

# Compute relative difference, avoid division by zero using a small epsilon (1e-12)
diff_rel = np.abs((toa_out2 - toa2) / np.maximum(np.abs(toa2), 1e-12))

# Compute statistics on the relative differences
mean_diff = np.mean(diff_rel)
std_diff = np.std(diff_rel)
cutoff = mean_diff + 3 * std_diff   # 3-sigma threshold

# Define tolerance threshold: 0.01% = 1e-4 in relative terms
threshold = 1e-4

# Count valid points below the threshold
valid_points = np.sum(diff_rel < threshold)
total_points = diff_rel.size
ratio_valid = valid_points / total_points

# Print results
print(f"Mean relative difference: {mean_diff:.2e}")
print(f"Standard deviation: {std_diff:.2e}")
print(f"3-sigma cutoff: {cutoff:.2e}")
print(f"Percentage of valid points (< {threshold:.1e}): {ratio_valid*100:.3f}%")

# Check if at least 99.7% of points (≈3-sigma rule) are within the threshold
if ratio_valid >= 0.997:
    print("✅ Test passed: at least 99.7% of points are within 0.01% difference.")
else:
    print("❌ Test failed: more than 0.3% of points exceed the 0.01% tolerance.")





