import numpy as np
import matplotlib.pyplot as plt
import os

from kp_basics import kp_rhs
from fE_vs_E__band_structure import find_energy_bands
# --------------------------------
# Create figures folder
# --------------------------------
os.makedirs("figures", exist_ok=True)

# --------------------------------
# Parameters
# --------------------------------
a = 1.0
E_min = 1e-4
E_max = 100
N_E = 20000

E = np.linspace(E_min, E_max, N_E)

# --------------------------------
# Helper function: find energy bands (Already declared in fE_vs_E__band_structure )
# --------------------------------

# --------------------------------
# Band gap vs P
# --------------------------------
P_values = np.linspace(0.5, 10, 20)
band_gaps = []

for P in P_values:
    fE = kp_rhs(E, a, P)
    bands = find_energy_bands(E, fE)

    if len(bands) >= 2:
        E1_start, E1_end = bands[0]
        E2_start, E2_end = bands[1]
        band_gaps.append(E2_start - E1_end)
    else:
        band_gaps.append(0.0)

# --------------------------------
# Plot
# --------------------------------
if __name__ == "__main__":


    plt.figure(figsize=(6, 4))
    plt.plot(P_values, band_gaps, 'o-', linewidth=2)

    plt.xlabel("Barrier strength P")
    plt.ylabel("Band gap ΔE")
    plt.title("Band Gap vs Barrier Strength (Kronig–Penney Model)")
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("figures/bandgap_vs_P.png", dpi=300)
    plt.show()


