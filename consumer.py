import pika

credentials = pika.PlainCredentials('admin', 'admin')

# Conectar ao RabbitMQ com credenciais
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', credentials=credentials)
)
channel = connection.channel()

# Garantir que a fila existe
channel.queue_declare(queue='test_queue')

# Callback para processar mensagens recebidas
def callback(ch, method, properties, body):
    print(f" [x] Mensagem recebida: {body.decode()}")

# Consumir mensagens da fila
channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Aguardando mensagens. Pressione CTRL+C para sair.')
channel.start_consuming()
