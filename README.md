# HTTP2RevShell

**HTTP2RevShell** is a remote shell tool based on HTTP to control a victim through a Flask server and a TCP socket connection. This application allows you to send commands to the victim's machine and receive responses through a web interface.

## Features

- Connect to the victim via a socket on the specified port.
- Real-time communication through commands sent to the victim and displayed in the browser.
- Simple web interface to send commands and view responses.
- RESTful API to interact with the victim through HTTP requests.

## Requirements

- Python 3.x
- Flask
- Flask-CORS

You can install the necessary dependencies using `pip`:

```bash
pip install flask flask-cors
```

## Configuration

You can configure the victim connection ports and the Flask API with the following parameters:

- `--host`: Server IP address (default `0.0.0.0`).
- `--port`: Port for the victim's data connection (default `4444`).
- `--flask_host`: Host for the Flask API (default `0.0.0.0`).
- `--flask_port`: Port for the Flask API (default `8080`).
- `--timeout`: Timeout for a client response (default `1 second`).

## Execution

To run the application, use the following command:

```bash
python app.py --host <IP> --port <PORT> --flask_host <FLASK_HOST> --flask_port <FLASK_PORT> --timeout <TIMEOUT>
```

- `<IP>`: Server IP address.
- `<PORT>`: Port where the server will listen to the victim.
- `<FLASK_HOST>`: Host where the Flask API will be available.
- `<FLASK_PORT>`: Port where the Flask API will be available.
- `<TIMEOUT>`: Timeout for a client response.

## Demo

<p align="left"><img width=100% alt="Usage demonstration" src="https://github.com/vpanal/http2revshell/blob/main/assets/demo.gif"></p>

## Web Interface

Access the web interface by visiting `http://<FLASK_HOST>:<FLASK_PORT>/`. From there you can send commands to the victim and view the responses in real-time.

## API

### `POST /api/v1/victim/command`

Send a command to the victim. The request body should be a JSON with the command:

```json
{
  "command": "command_to_send"
}
```

### `GET /api/v1/victim/status`

Get the status of the connection with the victim (connected or not).

## License

This project is under the MIT License. See the LICENSE file for more details.
