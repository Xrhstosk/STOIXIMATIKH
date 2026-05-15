import psycopg2
import random
# Δεν χρειαζόμαστε την Faker εδώ, μόνο τη σύνδεση και το random

def generate_bets():
    try:
        connection = psycopg2.connect(
            user="postgres", password="kgkdts7819", host="127.0.0.1", port="5433", database="Diplwmatikh"
        )
        cursor = connection.cursor()

        # Παίρνουμε όλα τα IDs από τη βάση
        cursor.execute("SELECT user_id, user_type_label FROM users")
        users = cursor.fetchall()
        
        cursor.execute("SELECT match_id, closing_odds_1, result FROM matches")
        matches = cursor.fetchall()

        print("Ξεκινάει η παραγωγή στοιχημάτων...")

        for user_id, label in users:
            # Κάθε παίκτης κάνει από 10 έως 30 στοιχήματα
            num_bets = random.randint(10, 30)
            
            for _ in range(num_bets):
                
                match = random.choice(matches)
                m_id, c_odds, res = match
                c_odds = float(c_odds) # Μετατροπή σε float για να γίνονται οι πράξεις
                stake = random.choice([10, 20, 50, 100])

                
                
                if label == 'Sharp':
                    # Οι Sharps βρίσκουν "αξία": odds_placed μεγαλύτερο από closing
                    odds_placed = round(c_odds * random.uniform(1.05, 1.15), 2)
                    # Οι Sharps κερδίζουν πιο συχνά (π.χ. 60% επιτυχία αν είναι το σωστό αποτέλεσμα)
                    is_winner = random.random() < 0.60
                else:
                    # Οι Casuals παίζουν στην τύχη ή σε χειρότερες αποδόσεις
                    odds_placed = round(c_odds * random.uniform(0.90, 1.00), 2)
                    is_winner = random.random() < (1 / c_odds) # Πιθανότητα βάσει απόδοσης

                # Υπολογισμός Payout
                payout = (stake * odds_placed) if is_winner else 0
                
                cursor.execute("""
                    INSERT INTO bets (user_id, match_id, odds_placed, stake, payout)
                    VALUES (%s, %s, %s, %s, %s)
                """, (user_id, m_id, odds_placed, stake, payout))

        connection.commit()
        print("--- ΕΠΙΤΥΧΙΑ: Τα στοιχήματα δημιουργήθηκαν! ---")

    except Exception as error:
        print("Σφάλμα στα στοιχήματα:", error)
    finally:
        if 'connection' in locals() and connection:
            cursor.close()
            connection.close()

# Κάλεσε τη νέα συνάρτηση
generate_bets()