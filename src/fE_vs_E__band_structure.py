import numpy as np
import matplotlib.pyplot as plt
import os

from kp_basics import kp_rhs

os.makedirs("figures", exist_ok=True)

a = 1.0
E = np.linspace(1e-4, 100, 10000)

P_values = [1, 5, 10]

def find_energy_bands(E, fE):
    allowed = np.abs(fE) <= 1
    bands = []
    in_band = False

    for i in range(len(E)):
        if allowed[i] and not in_band:
            E_start = E[i]
            in_band = True
        elif not allowed[i] and in_band:
            E_end = E[i-1]
            bands.append((E_start, E_end))
            in_band = False

    if in_band:
        bands.append((E_start, E[-1]))

    return bands

def plot_fE_vs_E(P):
    fE = kp_rhs(E, a, P)

    plt.figure(figsize=(7, 5))
    plt.plot(E, fE)
    plt.axhline(1, color='k', linestyle='--')
    plt.axhline(-1, color='k', linestyle='--')

    plt.fill_between(E, -1, 1, where=np.abs(fE) <= 1,
                     alpha=0.3, label="Allowed bands")

    plt.xlabel("Energy E")
    plt.ylabel("f(E)")
    plt.title(f"f(E) vs E (P = {P})")
    plt.grid(True)

    plt.savefig(f"figures/fE_vs_E_P{P}.png", dpi=300)
    plt.show()
    plt.close()

def plot_band_structure(P):
    fE = kp_rhs(E, a, P)
    bands = find_energy_bands(E, fE)

    plt.figure(figsize=(7, 5))

    for (E1, E2) in bands:
        mask = (E >= E1) & (E <= E2)
        f_band = np.clip(fE[mask], -1, 1)
        k = np.arccos(f_band) / a

        plt.plot(k, E[mask], 'b')
        plt.plot(-k, E[mask], 'b')

    plt.xlabel("Wave vector k")
    plt.ylabel("Energy E")
    plt.title(f"Band Structure (P = {P})")
    plt.grid(True)

    plt.savefig(f"figures/bandstructure_P{P}.png", dpi=300)
    plt.show()
    plt.close()

# -----------------------------
# Run automation
# -----------------------------
if __name__ == "__main__":
        
    for P in P_values:
        plot_fE_vs_E(P)
        plot_band_structure(P)

    print("All plots generated successfully.")


