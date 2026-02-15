import numpy as np
import matplotlib.pyplot as plt

# -----------------------
# Physical parameters
# -----------------------
a = 1.0        # lattice constant = well width
P = 10.0       # delta barrier strength

# Energy range
E_min = 1e-4
E_max = 100
N_E = 20000

E = np.linspace(E_min, E_max, N_E)
alpha = np.sqrt(E)

# -----------------------
# Kronig-Penney RHS
# -----------------------
def kp_rhs(E, a, P):
    alpha = np.sqrt(E)
    return np.cos(alpha * a) + (P / (alpha * a)) * np.sin(alpha * a)

fE = kp_rhs(E, a, P)






# -----------------------
# Allowed bands condition
# -----------------------

#-----------------------
#Testing CODE:
#-----------------------
# allowed = np.abs(fE) <= 1


# plt.figure(figsize=(8, 5))
# plt.plot(E, fE, label=r'$f(E)$')
# plt.axhline(1, color='k', linestyle='--')
# plt.axhline(-1, color='k', linestyle='--')

# plt.fill_between(E, -1, 1, where=allowed, 
#                  color='skyblue', alpha=0.4, label='Allowed bands')

# plt.xlabel("Energy E")
# plt.ylabel(r"$\cos(ka)$")
# plt.title("Kronig–Penney Model (Delta Barrier)")
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.savefig(
#     f"figures/fE_vs_E_P{P}_a{a}.png",
#     dpi=300,
#     bbox_inches="tight"
# )


# plt.show()

# bands = []
# in_band = False

# for i in range(len(E)):
#     if allowed[i] and not in_band:
#         E_start = E[i]
#         in_band = True
#     elif not allowed[i] and in_band:
#         E_end = E[i-1]
#         bands.append((E_start, E_end))
#         in_band = False

# if in_band:
#     bands.append((E_start, E[-1]))

# print("Allowed energy bands:")
# for i, (E1, E2) in enumerate(bands):
#     print(f"Band {i+1}: {E1:.3f} – {E2:.3f}")


# plt.figure(figsize=(8, 5))

# for (E1, E2) in bands:
#     mask = (E >= E1) & (E <= E2)
#     E_band = E[mask]
#     f_band = fE[mask]

#     f_band = np.clip(f_band, -1.0, 1.0)

#     ka = np.arccos(f_band)
#     k = ka / a

#     plt.plot(k, E_band, color='blue')
#     plt.plot(-k, E_band, color='blue')  # negative k

# plt.xlabel("Wave vector k")
# plt.ylabel("Energy E")
# plt.title("Energy Band Structure (Kronig–Penney Model)")
# plt.grid(True)
# plt.tight_layout()
# plt.savefig(
#     f"figures/E_vs_K_{P}_a{a}.png",
#     dpi=300,
#     bbox_inches="tight"
# )

# plt.show()
