import psycopg2
import sys

QUERY="""
SELECT 
      pg_database.datname, pg_database_size(pg_database.datname), 
      pg_size_pretty(pg_database_size(pg_database.datname))
      FROM pg_database ORDER BY pg_database_size DESC;
"""

def main():
    try:
        connection = psycopg2.connect(user = "postgres",
                                    password = "1234",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "postgres")
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL: ", error)
        return(1)

    cursor = connection.cursor()
    
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print(f"You are connected to  {record[0]}")

    cursor.execute(QUERY)
    records = cursor.fetchall() 
    print(records)

    for row in records:
       print(f"DB {row[0]} has {row[2]}")

    import csv 
    with open("sizes.csv", "w") as f:
        cw = csv.writer(f)
        cw.writerow(['DB', 'Size', 'Size KB'])
        for row in records:
            cw.writerow(row)

    #closing database connection.
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
    return(0)

if __name__ == "__main__":
    sys.exit(main())