
# MAIN FUNCTION TO CALL THE L1B MODULE

from l1b.src.l1b import l1b

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'C:\\Users\\Simone\\OneDrive\\Documenti\\Desktop\\EODP\\eodp\\auxiliary'
indir = r'C:\\Users\\Simone\\OneDrive\\Documenti\Desktop\\Earth Observation\\my_output_ism1610'
outdir = r"C:\\Users\\Simone\\OneDrive\\Documenti\\Desktop\\myoutput_L1B_1610"

# Initialise the ISM
myL1b = l1b(auxdir, indir, outdir)
myL1b.processModule()
