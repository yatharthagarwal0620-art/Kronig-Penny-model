import numpy as np
import matplotlib.pyplot as plt
import os

from kp_basics import kp_rhs
from fE_vs_E__band_structure import find_energy_bands

os.makedirs("figures", exist_ok=True)

# --------------------------------
# Parameters
# --------------------------------
a = 1.0
E_min = 1e-4
E_max = 50
N_E = 15000

E = np.linspace(E_min, E_max, N_E)

P_values = np.linspace(0.5, 10, 15)
effective_masses = []

# --------------------------------
# Helper: find bands(already done in fE_vs_E__band_structure)
# --------------------------------


# --------------------------------
# Compute effective mass
# --------------------------------
for P in P_values:
    fE = kp_rhs(E, a, P)
    bands = find_energy_bands(E, fE)

    # Lowest band
    E1_start, E1_end = bands[0]
    mask = (E >= E1_start) & (E <= E1_end)

    E_band = E[mask]
    f_band = np.clip(fE[mask], -1, 1)

    k = np.arccos(f_band) / a

    # Sort by k (important)
    idx = np.argsort(k)
    k = k[idx]
    E_band = E_band[idx]

    # Take small-k region
    k_small = k[k < 0.3]
    E_small = E_band[:len(k_small)]

    # Quadratic fit: E = E0 + A k^2
    coeffs = np.polyfit(k_small**2, E_small, 1)
    A = coeffs[0]

    m_star = 1 / (2 * A)
    effective_masses.append(m_star)

# --------------------------------
# Plot
# --------------------------------
if __name__ == "__main__":
   

    plt.figure(figsize=(6, 4))
    plt.plot(P_values, effective_masses, 'o-', linewidth=2)

    plt.xlabel("Barrier strength P")
    plt.ylabel("Effective mass $m^*$")
    plt.title("Effective Mass vs Barrier Strength")
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("figures/effective_mass_vs_P.png", dpi=300)
    plt.show()
