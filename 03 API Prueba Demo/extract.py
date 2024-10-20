import requests
import psycopg2

# Configuraciones de la API
API_URL = "http://34.239.4.107:8000/records?count=100"  # Reemplaza <tu_ip_publica> con la IP pública de tu API

# Configuraciones de la base de datos PostgreSQL
DB_HOST = "database-cloud.cenfi8vp6ne5.us-east-1.rds.amazonaws.com"
DB_NAME = "recorridos"
DB_USER = "postgres"
DB_PASSWORD = "djsn2024"
DB_PORT = "5432"

# Función para llamar a la API y obtener los datos
def get_records_from_api(count):
    response = requests.post(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener datos de la API: {response.status_code}")
        return None

# Función para guardar los registros en PostgreSQL
def save_to_postgres(records):
    try:
        # Conectar a la base de datos PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        cur = conn.cursor()

        # Crear la tabla si no existe
        cur.execute("""
        CREATE TABLE IF NOT EXISTS taxi_records (
            VendorID INT,
            tpep_pickup_datetime TIMESTAMP,
            tpep_dropoff_datetime TIMESTAMP,
            passenger_count INT,
            trip_distance FLOAT,
            RatecodeID INT,
            store_and_fwd_flag VARCHAR(10),
            PULocationID INT,
            DOLocationID INT,
            payment_type INT,
            fare_amount FLOAT,
            extra FLOAT,
            mta_tax FLOAT,
            tip_amount FLOAT,
            tolls_amount FLOAT,
            improvement_surcharge FLOAT,
            total_amount FLOAT,
            congestion_surcharge FLOAT,
            airport_fee FLOAT
        );
        """)
        conn.commit()

        # Insertar los registros en la tabla
        insert_query = """
        INSERT INTO taxi_records (
            VendorID, tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance,
            RatecodeID, store_and_fwd_flag, PULocationID, DOLocationID, payment_type, fare_amount,
            extra, mta_tax, tip_amount, tolls_amount, improvement_surcharge, total_amount,
            congestion_surcharge, airport_fee
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Insertar cada registro
        for record in records:
            cur.execute(insert_query, (
                record["VendorID"], record["tpep_pickup_datetime"], record["tpep_dropoff_datetime"],
                record["passenger_count"], record["trip_distance"], record["RatecodeID"], record["store_and_fwd_flag"],
                record["PULocationID"], record["DOLocationID"], record["payment_type"], record["fare_amount"],
                record["extra"], record["mta_tax"], record["tip_amount"], record["tolls_amount"],
                record["improvement_surcharge"], record["total_amount"], record["congestion_surcharge"],
                record["airport_fee"]
            ))
        conn.commit()

        # Cerrar la conexión
        cur.close()
        conn.close()

        print(f"{len(records)} registros insertados correctamente en PostgreSQL.")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error al conectar o insertar en PostgreSQL: {error}")

# Ejecutar la solicitud y guardado
if __name__ == "__main__":
    records = get_records_from_api(100)
    if records:
        save_to_postgres(records)