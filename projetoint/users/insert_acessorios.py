# insert_acessorios.py
import pymysql
import json

# AWS RDS MySQL Configuration
db_config = {
    'HOST': '3.131.37.27',
    'USER': 'app_user',
    'PASSWORD': 'Xv4P16u3!O@+Bz',
    "NAME": "RPGTormenta",
    "port": 3306,
    "ssl": {"ssl": {"rejectUnauthorized": False}} ,
    'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
      # For SSL
}



# Read JSON file
with open("acessorios.json", "r", encoding="utf-8") as file:
    acessorios = json.load(file)

# Connect and insert
try:
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    for item in acessorios:
        cursor.execute(
            "INSERT INTO acessorios (nome, tipo, preco, descricao) VALUES (%s, %s, %s, %s)",
            (item["nome"], item["tipo"], item["preco"], item["descricao"])
        )
        print(f"✅ Inserted: {item['nome']}")

    conn.commit()
    print("🎉 All items inserted successfully!")

except Exception as e:
    print(f"❌ Error: {e}")
finally:
    if conn:
        conn.close()