# Kronig–Penney Band Structure Simulation

This project implements a numerical simulation of the **1D Kronig–Penney model** to study how a periodic potential modifies free-electron motion and leads to band formation in crystalline solids.

---

## 🔬 Objectives

- Solve the Bloch dispersion relation numerically  
- Visualize electronic band structure  
- Study the effect of lattice potential strength  
- Compute transport quantities such as velocity and effective mass  

---


## 🧾 Theory

### Periodic Potential in Crystals

In a crystalline solid, atoms are arranged in a regular repeating lattice.  
Electrons moving inside the crystal therefore experience a **periodic potential**:

\[
V(x) = V(x + a)
\]

where **a** is the lattice constant (unit cell length).( In this project , a is set to 1.0)

This periodicity leads to the formation of **Bloch states**, which are wavefunctions of the form:

ψₖ(x) = uₖ(x) e^{ikx}


where uₖ(x) has the same periodicity as the lattice.

---

### The Kronig–Penney Model

The **Kronig–Penney model** is an idealized 1D model that represents the periodic lattice using a sequence of potential wells and barriers.  

It provides an analytically tractable way to understand how a periodic potential modifies free-electron motion and leads to **energy band formation**.

---

### Kronig–Penney Dispersion Relation

Solving the Schrödinger equation for the periodic potential and applying Bloch’s theorem yields the **Kronig–Penney equation**:

cos(k.a) = cos(α.a) + (P / α.a) sin(α.a)


where:

- k → crystal momentum  
- a → lattice constant  
- α → √(2mE) / ħ  
- P → dimensionless potential strength 

Allowed energy states occur when:

|cos(ka)| ≤ 1

Values outside this range correspond to **forbidden energies (band gaps)**.

---

### Physical Interpretation

The periodic potential causes **Bragg reflection** of electron waves at Brillouin zone boundaries, which leads to:

- Splitting of energy levels  
- Formation of allowed energy bands  
- Appearance of forbidden gaps  

Thus, the Kronig–Penney model provides a microscopic explanation of why solids exhibit **metallic, semiconducting, or insulating behavior** depending on band structure.

---


## ⚙️ Methods

We work in dimensionless units where  

- ℏ² / 2m = 1  

- a = 1.0 

To study the effect of periodic potential strength on the band structure,
the dimensionless potential parameter **P** is varied.

Simulations are performed for:

- P = 1.0, 5.0, 10.0



Energy is scanned numerically and allowed bands are identified using the Bloch condition:

|cos(k.a)| ≤ 1

From the reconstructed dispersion E(k), we compute:

- Group velocity v(k)
- Effective mass m*
- Band gap vs potential strength

---

## 📊 Results

The simulation demonstrates:

- Band formation due to periodic potential  
- Band gap opening at Brillouin zone boundaries  
- Deviation from free-electron dispersion  
- Reduction of velocity with increasing potential  
- Increase of effective mass due to localization  

These results illustrate the microscopic origin of electronic properties in solids.

---
## 🚀 How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yatharthagarwal0620-art/kronig-penney-model.git
cd kronig-penney-model
 ```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```
### 3️⃣ Run 
```bash
python src/fE_vs_E_band_structure.py
python src/bandgap.py
python src/effective_mass.py
python src/velocity_vs_k.py
python src/free_electron_comparison.py
```
---
## 🧠 Key Physical Insight

- Periodic potential → band formation → gap opening → reduced velocity → increased effective mass
- This simulation provides a computational demonstration of how lattice periodicity gives rise to electronic behavior in solids.
---

## 🔮 Possible Extensions

- Density of states calculation
- Tight-binding approximation comparison
- 2D lattice extension
- Fermi level and carrier statistics
---
## 👤 Author

Yatharth Agarwal
---
## ⭐ Support

If you found this project interesting or useful:

### ⭐ Star the repository
🍴 Fork it to explore further

---