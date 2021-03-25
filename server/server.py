import http.server
import socketserver

# Обробка запитів клієнта до сервера
handler = http.server.SimpleHTTPRequestHandler

# Сервер буде запущений  на порту 1234
with socketserver.TCPServer(("", 1234), handler) as httpd:

    # Сервер буди виконуватись постійно
    httpd.serve_forever()