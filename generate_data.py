import pandas as pd
import numpy as np

# --- Configuration ---
NUM_CELLS = 1000  # Total cells to simulate
DONORS = ['Donor_A', 'Donor_B', 'Donor_C']
DOSAGES = [0, 10, 50, 100]  # ng/mL

# --- Helper Function to Simulate Biology ---
def generate_cell_data(n_cells):
    data = []
    
    for _ in range(n_cells):
        # 1. Randomly assign a Donor and a Dosage
        donor = np.random.choice(DONORS)
        dose = np.random.choice(DOSAGES)
        
        # 2. Define Donor Baseline (Genetics)
        # Donor B has naturally higher baseline inflammation than A or C
        if donor == 'Donor_A': baseline = 2.0
        elif donor == 'Donor_B': baseline = 4.5 
        else: baseline = 2.5
        
        # 3. Simulate Gene A (The "Responder" - e.g., IL-6)
        # Formula: Baseline + (Dose * Sensitivity) + Noise
        # This creates a linear response to the cytokine
        sensitivity = 0.15 # How strongly the gene reacts to the dose
        noise = np.random.normal(0, 1.5) # Biological noise
        gene_a_exp = baseline + (dose * sensitivity) + noise
        
        # 4. Simulate Gene B (The "Housekeeper" - e.g., GAPDH)
        # This gene should NOT change much with dose (Control)
        gene_b_exp = 10.0 + np.random.normal(0, 0.5)
        
        data.append({
            'Donor_ID': donor,
            'Cytokine_Dose': dose,
            'Marker_Gene_Response': max(0, gene_a_exp), # Expression can't be negative
            'Housekeeping_Gene': gene_b_exp
        })
        
    return pd.DataFrame(data)

# --- Generate and Save ---
df = generate_cell_data(NUM_CELLS)
df.to_csv('synthetic_cell_village_data.csv', index=False)

print("✅ Data generated! First 5 rows:")
print(df.head())