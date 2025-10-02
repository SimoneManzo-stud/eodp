
# MAIN FUNCTION TO CALL THE ISM MODULE

from ism.src.ism import ism

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'C:\\Users\\Simone\\OneDrive\\Documenti\\Desktop\\EODP\\eodp\\auxiliary'
indir = r"C:\\Users\\Simone\\OneDrive\\Documenti\\Desktop\\Earth Observation\\EODP-TS-ISM\\input\\gradient_alt100_act150" # small scene
outdir = r"C:\\Users\\Simone\\OneDrive\\Documenti\\Desktop\\myoutput_src_EODP"

# Initialise the ISM
myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
