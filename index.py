import tornado.ioloop
import tornado.web
import tornado.websocket

# Список подключенных клиентов
clients = []

class ChatHandler(tornado.websocket.WebSocketHandler):
    # Вызывается при подключении клиента
    def open(self):
        clients.append(self)

    # Вызывается при получении сообщения от клиента
    def on_message(self, message):
        # Отправляем сообщение всем клиентам
        for client in clients:
            client.write_message(message)

    # Вызывается при закрытии соединения клиента
    def on_close(self):
        clients.remove(self)

class MainHandler(tornado.web.RequestHandler):
    # Отображаем страницу чата
    def get(self):
        self.render("chat.html")

app = tornado.web.Application([
    (r"/", MainHandler),
    (r"/chat", ChatHandler),
    ])

if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
