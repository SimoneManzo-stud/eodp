
# MAIN FUNCTION TO CALL THE L1C MODULE

from l1c.src.l1c import l1c

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'C:\\Users\\Simone\\OneDrive\\Documenti\\Desktop\\EODP\\eodp\\auxiliary'
# GM dir + L1B dir
indir = r"C:\Users\Simone\OneDrive\Documenti\Desktop\Earth Observation\EODP-TS-L1C-20250911T170741Z-1-001\EODP-TS-L1C\input\gm_alt100_act_150",r"C:\Users\Simone\OneDrive\Documenti\Desktop\Earth Observation\EODP-TS-L1C-20250911T170741Z-1-001\EODP-TS-L1C\input\l1b_output"
outdir = r'C:\\Users\\Simone\\OneDrive\\Documenti\Desktop\\Earth Observation\\my_output_L1C'

# Initialise the ISM
myL1c = l1c(auxdir, indir, outdir)
myL1c.processModule()
