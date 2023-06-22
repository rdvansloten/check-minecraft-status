from flask import Flask, render_template
import socket

# Start app
app = Flask(__name__)

@app.route("/")
def index():
  def check_server_status(ip, port):
    try:
      socket.create_connection((ip, port), timeout=5)
      return f'Server {ip}:{port} is up'
    except socket.error:
      return f'Server {ip}:{port} is down'

  server_ip = 'minecraft.woomies.ink'
  server_port = 31565
  status = check_server_status(server_ip, server_port)
  return status