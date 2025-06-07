from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Inicializa o banco de dados
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS hotels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        location TEXT NOT NULL,
        price REAL NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        guest_name TEXT NOT NULL,
        hotel_id INTEGER NOT NULL,
        check_in TEXT NOT NULL,
        check_out TEXT NOT NULL,
        FOREIGN KEY (hotel_id) REFERENCES hotels(id)
    )''')
    # Insere dados de exemplo
    c.execute("INSERT OR IGNORE INTO hotels (id, name, location, price) VALUES (1, 'Hotel Praia', 'Natal, RN', 200.00)")
    c.execute("INSERT OR IGNORE INTO hotels (id, name, location, price) VALUES (2, 'Hotel Sol', 'Pipa, RN', 150.00)")
    conn.commit()
    conn.close()

# Rota para listar hotéis
@app.route('/api/hotels', methods=['GET'])
def get_hotels():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM hotels')
    hotels = [{'id': row[0], 'name': row[1], 'location': row[2], 'price': row[3]} for row in c.fetchall()]
    conn.close()
    return jsonify(hotels)

# Rota para criar reserva
@app.route('/api/reservations', methods=['POST'])
def create_reservation():
    data = request.get_json()
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO reservations (guest_name, hotel_id, check_in, check_out) VALUES (?, ?, ?, ?)',
              (data['guestName'], data['hotelId'], data['checkIn'], data['checkOut']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Reserva criada com sucesso!'}), 201

if __name__ == '__main__':
    init_db()
    app.run(debug=True)