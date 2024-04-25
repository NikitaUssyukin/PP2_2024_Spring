import psycopg2
from config import load_config


def insert_vendor(vendor_name):
    """ Insert a new vendor into the vendors table """

    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""
    
    sql_alt = f"""INSERT INTO vendors(vendor_name)
                  VALUES('{vendor_name}') RETURNING vendor_id;"""
    
    vendor_id = None
    config = load_config()

    # print(sql % vendor_name) # INSERT INTO vendors(vendor_name)
    #                             # VALUES(3M Co.) RETURNING vendor_id;

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (vendor_name,))
                # or
                # cur.execute(sql_alt)

                # get the generated id back                
                rows = cur.fetchone()
                if rows:
                    vendor_id = rows[0]
                print(vendor_id, vendor_name)

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return vendor_id
    
def insert_many_vendors(vendor_list):
    """ Insert multiple vendors into the vendors table  """

    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    config = load_config()
    rows = []

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.executemany(sql, vendor_list)

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return rows

if __name__ == '__main__':
    insert_vendor("3M Co.")

    insert_many_vendors([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])