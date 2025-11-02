
# MAIN FUNCTION TO CALL THE ISM MODULE

from ism.src.ism import ism

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'C:\\Users\\Simone\\OneDrive\\Documenti\\Desktop\\EODP\\eodp\\auxiliary'
indir = r"C:\\Users\\Simone\\OneDrive\\Documenti\\Desktop\\Earth Observation\\EODP-TS-E2E-20251002T100205Z-1-001\\EODP-TS-E2E\\sgm_out"# small scene
outdir = r'C:\\Users\\Simone\\OneDrive\\Documenti\\Desktop\\myoutputs\\myoutput_ism_1610'

# Initialise the ISM
myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
