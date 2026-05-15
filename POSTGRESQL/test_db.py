import psycopg2

try:
    # Στοιχεία σύνδεσης - ΑΝΤΙΚΑΤΑΣΤΗΣΕ ΤΑ ΜΕ ΤΑ ΔΙΚΑ ΣΟΥ
    connection = psycopg2.connect(
        user="postgres",
        password="kgkdts7819", # Βάλε εδώ τον κωδικό της PostgreSQL
        host="127.0.0.1",
        port="5433",
        database="Diplwmatikh" # Το όνομα που έδωσες στο pgAdmin
    )

    cursor = connection.cursor()
    
    # Εκτέλεση ενός απλού query για να δούμε αν "μιλάει" η βάση
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("--- Σύνδεση Επιτυχής! ---")
    print("Είσαι συνδεδεμένος στην έκδοση:", record)

    # Έλεγχος αν υπάρχουν οι πίνακες που έφτιαξες
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = cursor.fetchall()
    print("Πίνακες που βρέθηκαν στη βάση σου:", tables)

except Exception as error:
    print("Σφάλμα κατά τη σύνδεση:", error)

finally:
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("--- Η σύνδεση έκλεισε με ασφάλεια. ---")