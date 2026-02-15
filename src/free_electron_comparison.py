import numpy as np
import matplotlib.pyplot as plt
import os

from kp_basics import kp_rhs
from fE_vs_E__band_structure import find_energy_bands


os.makedirs("figures", exist_ok=True)

# -------------------------------
# Parameters
# -------------------------------
a = 1.0
P_values = [1, 5, 10]
E_min = 1e-4
E_max = 50
N_E = 20000

E = np.linspace(E_min, E_max, N_E)

# -------------------------------
# Helper: find energy bands
# -------------------------------
if __name__ == "__main__":
    
    for P in P_values:
        # -------------------------------
        # Kronig–Penney lowest band
        # -------------------------------
        fE = kp_rhs(E, a, P)
        bands = find_energy_bands(E, fE)

        E1_start, E1_end = bands[0]
        mask = (E >= E1_start) & (E <= E1_end)

        E_band = E[mask]
        f_band = np.clip(fE[mask], -1, 1)
        k_kp = np.arccos(f_band) / a

        # Sort
        idx = np.argsort(k_kp)
        k_kp = k_kp[idx]
        E_band = E_band[idx]

        # -------------------------------
        # Free electron
        # -------------------------------
        k_free = np.linspace(0, np.pi/a, 400)
        E_free = k_free**2

        # -------------------------------
        # Plot
        # -------------------------------
        plt.figure(figsize=(6, 4))

        plt.plot(k_kp, E_band, label="Kronig–Penney", linewidth=2)
        plt.plot(k_free, E_free, "--", label="Free electron", linewidth=2)

        plt.axvline(np.pi/a, color="k", linestyle=":", alpha=0.6)
        plt.text(np.pi/a, 0, r"$\pi/a$", ha="right", va="bottom")

        plt.xlabel("Wave vector k")
        plt.ylabel("Energy E")
        plt.title(f"Energy Dispersion: KP vs Free Electron (P = {P})")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        plt.savefig(f"figures/Ek_comparison_P{P}.png", dpi=300)
        plt.show()

        # -------------------------------
        # Velocity
        # -------------------------------
        v_kp = np.gradient(E_band, k_kp)
        v_free = 2 * k_free

        plt.figure(figsize=(6, 4))

        plt.plot(k_kp, v_kp, label="Kronig–Penney", linewidth=2)
        plt.plot(k_free, v_free, "--", label="Free electron", linewidth=2)

        plt.axvline(np.pi/a, color="k", linestyle=":", alpha=0.6)

        plt.xlabel("Wave vector k")
        plt.ylabel("Velocity v(k)")
        plt.title(f"Velocity vs k: KP vs Free Electron (P = {P})")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        plt.savefig(f"figures/velocity_comparison_P{P}.png", dpi=300)
        plt.show()
        plt.close()
