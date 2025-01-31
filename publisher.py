import pika

# Configurar credenciais
credentials = pika.PlainCredentials('admin', 'admin')

# Conectar ao RabbitMQ com credenciais
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', credentials=credentials)
)
channel = connection.channel()

# Criar a fila
channel.queue_declare(queue='test_queue')

# Enviar mensagem
message = "Olá, teste!"
channel.basic_publish(exchange='', routing_key='test_queue', body=message)

print(f" [x] Mensagem enviada: {message}")

# Fechar conexão
connection.close()
