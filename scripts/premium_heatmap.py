import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load the CSV file
file_path = os.path.join('reports', 'risk_based_premium.csv')
if not os.path.exists(file_path):
    print(f"Error: File not found at {file_path}. Please check the path or generate the CSV first.")
    exit()

df = pd.read_csv(file_path)

print("Available columns:", df.columns.tolist())
correlation_matrix = df[['Claim_Probability', 'Predicted_Severity', 'Risk_Based_Premium']].corr()

# Create the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='YlOrRd', fmt='.2f', cbar_kws={'label': 'Correlation Coefficient'}, square=True)

# Customize the plot
plt.title('Correlation Heatmap of Risk-Based Premium Data', pad=20)
plt.xlabel('Variables')
plt.ylabel('Variables')

# Save the heatmap to a file
plt.savefig('reports/risk_based_premium_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

