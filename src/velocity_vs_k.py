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
P_values=[1.0,5.0,10.0]
E_min = 1e-4
E_max = 50
N_E = 20000

E = np.linspace(E_min, E_max, N_E)

# --------------------------------
# Helper: find energy bands(Already Done)
# --------------------------------


# --------------------------------
# Reconstruct E(k) for lowest band
# --------------------------------
if __name__ == "__main__":
    

    for P in P_values:
            
        fE = kp_rhs(E, a, P)
        bands = find_energy_bands(E, fE)

        E1_start, E1_end = bands[0]
        mask = (E >= E1_start) & (E <= E1_end)

        E_band = E[mask]
        f_band = np.clip(fE[mask], -1, 1)

        k = np.arccos(f_band) / a

        # Sort by k
        idx = np.argsort(k)
        k = k[idx]
        E_band = E_band[idx]

        # --------------------------------
        # Compute velocity
        # --------------------------------
        v_k = np.gradient(E_band, k)

        # --------------------------------
        # Plot velocity vs k
        # --------------------------------
        plt.figure(figsize=(6, 4))
        plt.plot(k, v_k, label="v(k)")
        plt.plot(-k, -v_k, linestyle="--", alpha=0.6, label="v(-k)")

        plt.axhline(0, color="k", linewidth=0.8)

        plt.xlabel("Wave vector k")
        plt.ylabel("Group velocity v(k)")
        plt.title(f"Velocity vs k (P = {P})")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        plt.savefig(f"figures/velocity_vs_k_P{P}.png", dpi=300)
        plt.show()
        plt.close()
