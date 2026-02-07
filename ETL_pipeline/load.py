import sqlite3

def load_to_db(df, db_path="etl.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql("orders", conn, if_exists="replace", index=False)
    conn.close()