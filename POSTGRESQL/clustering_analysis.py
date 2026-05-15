import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Σύνδεση με τη βάση δεδομένων
# Αντικατάστησε με τα δικά σου στοιχεία (user, password, host, port, db_name)
engine = create_engine('postgresql://postgres:kgkdts7819@localhost:5433/Diplwmatikh')

# 2. Φόρτωση των δεδομένων από τον πίνακα player_stats
query = "SELECT user_id, net_profit, avg_clv FROM player_stats"
df = pd.read_sql(query, engine)


# 3. Προετοιμασία δεδομένων για τον K-means
# Επιλέγουμε τις δύο στήλες (διαστάσεις) που θα αναλύσουμε
features = ['net_profit', 'avg_clv']
x = df[features]

# Scaling: Μετατρέπουμε τα δεδομένα ώστε να έχουν μέση τιμή 0 και τυπική απόκλιση 1
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# 4. Εφαρμογή του K-means
# Ζητάμε από τον αλγόριθμο να φτιάξει 2 clusters
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(x_scaled)

# 5. Οπτικοποίηση (Visualization)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='avg_clv', y='net_profit', hue='cluster', palette='viridis', s=100)

plt.title('Player Segmentation: Sharps vs Casuals')
plt.xlabel('Average CLV (Closing Line Value)')
plt.ylabel('Total Net Profit (€)')
plt.axhline(0, color='red', linestyle='--', linewidth=1) # Γραμμή για το break-even
plt.axvline(0, color='red', linestyle='--', linewidth=1) # Γραμμή για το μηδενικό CLV
plt.grid(True, alpha=0.3)
plt.legend(title='Cluster')
plt.show()

print("Η ανάλυση ολοκληρώθηκε! Το γράφημα εμφανίζεται στην οθόνη σου.")