# HTTP2RevShell

**HTTP2RevShell** es una herramienta de Shell remota basada en HTTP para controlar una víctima a través de un servidor Flask y una conexión de socket tcp. Esta aplicación permite enviar comandos a la máquina víctima y recibir respuestas a través de una interfaz web.

## Características

- Conexión a la víctima mediante un socket en el puerto especificado.
- Comunicación en tiempo real mediante comandos que se envían a la víctima y se muestran en el navegador.
- Interfaz web sencilla para enviar comandos y ver respuestas.
- API RESTful para interactuar con la víctima a través de solicitudes HTTP.

## Requisitos

- Python 3.x
- Flask
- Flask-CORS

Puedes instalar las dependencias necesarias utilizando `pip`:

```bash
pip install flask flask-cors
```

## Configuración

Puedes configurar los puertos de la conexión de la víctima y la API Flask con los siguientes parámetros:

- `--host`: Dirección IP del servidor (por defecto `0.0.0.0`).
- `--port`: Puerto para la conexión de datos de la víctima (por defecto `4444`).
- `--flask_host`: Host para la API Flask (por defecto `0.0.0.0`).
- `--flask_port`: Puerto para la API Flask (por defecto `8080`).

## Ejecución

Para ejecutar la aplicación, usa el siguiente comando:

```bash
python app.py --host <IP> --port <PORT> --flask_host <FLASK_HOST> --flask_port <FLASK_PORT>
```

- `<IP>`: Dirección IP del servidor.
- `<PORT>`: Puerto en el que el servidor escuchará a la víctima.
- `<FLASK_HOST>`: Host en el que la API Flask estará disponible.
- `<FLASK_PORT>`: Puerto en el que la API Flask estará disponible.

## Interfaz Web

Accede a la interfaz web visitando `http://<IP>:<FLASK_PORT>/`. Desde allí podrás enviar comandos a la víctima y ver las respuestas en tiempo real.

## API

### `POST /api/v1/victim/command`

Envía un comando a la víctima. El cuerpo de la solicitud debe ser un JSON con el comando:

```json
{
  "command": "comando_a_enviar"
}
```

### `GET /api/v1/victim/status`

Obtén el estado de la conexión con la víctima (conectado o no).

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.
