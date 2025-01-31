# RabbitMQ Test Project

Este projeto tem como objetivo testar a comunicação entre produtores e consumidores utilizando RabbitMQ com Docker e Python.

## 📌 Requisitos

- **Docker** e **Docker Compose** instalados
- **Python 3.x** instalado
- Biblioteca **pika** instalada (`pip install pika`)

---

## 🚀 Configuração

### 1️⃣ **Subir o RabbitMQ com Docker**

Crie um arquivo `docker-compose.yml` com o seguinte conteúdo:

```yaml
version: '3.8'
services:
  rabbitmq:
    image: rabbitmq:3-management
    container_name: rabbitmq
    restart: always
    ports:
      - "5672:5672"   # Porta para conexões do RabbitMQ
      - "15672:15672" # Painel de administração
    environment:
      RABBITMQ_DEFAULT_USER: admin
      RABBITMQ_DEFAULT_PASS: admin
    volumes:
      - rabbitmq_data:/var/lib/rabbitmq

volumes:
  rabbitmq_data:
    driver: local
```

Agora, execute o comando para iniciar o RabbitMQ:

```bash
docker-compose up -d
```

Acesse o painel de gerenciamento em [http://localhost:15672](http://localhost:15672)

- **Usuário:** `admin`
- **Senha:** `admin`

---

### 2️⃣ **Criar o Produtor (Publisher)**

Crie um arquivo `publisher.py` com o seguinte código:

```python
import pika

# Configurar credenciais
credentials = pika.PlainCredentials('admin', 'admin')

# Conectar ao RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', credentials=credentials)
)
channel = connection.channel()

# Criar a fila
channel.queue_declare(queue='test_queue')

# Enviar mensagem
message = "Olá, RabbitMQ!"
channel.basic_publish(exchange='', routing_key='test_queue', body=message)

print(f" [x] Mensagem enviada: {message}")

# Fechar conexão
connection.close()
```

Execute o publisher:

```bash
python3 publisher.py
```

---

### 3️⃣ **Criar o Consumidor (Consumer)**

Crie um arquivo `consumer.py`:

```python
import pika

# Configurar credenciais
credentials = pika.PlainCredentials('admin', 'admin')

# Conectar ao RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', credentials=credentials)
)
channel = connection.channel()

# Criar fila
channel.queue_declare(queue='test_queue')

def callback(ch, method, properties, body):
    print(f" [x] Mensagem recebida: {body.decode()}")

# Consumir mensagens
channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Aguardando mensagens. Pressione CTRL+C para sair.')
channel.start_consuming()
```

Execute o consumidor:

```bash
python3 consumer.py
```

Agora, o consumidor ficará esperando mensagens. Quando o `publisher.py` for executado, ele enviará mensagens para o RabbitMQ e o `consumer.py` as receberá.

---

## 🛠 Solução de Problemas

1. **Erro de autenticação (ACCESS\_REFUSED)**

   ```
   pika.exceptions.ProbableAuthenticationError: ConnectionClosedByBroker: (403) 'ACCESS_REFUSED'
   ```

   ✅ Certifique-se de que está usando as credenciais corretas no `publisher.py` e `consumer.py`.

2. **Conexão recusada**

   ```
   pika.exceptions.AMQPConnectionError: [Errno 111] Connection refused
   ```

   ✅ Verifique se o RabbitMQ está rodando:

   ```bash
   docker ps
   ```

3. **Painel do RabbitMQ não abre** ✅ Acesse: [http://localhost:15672](http://localhost:15672) ✅ Caso não funcione, reinicie o container:

   ```bash
   docker-compose down && docker-compose up -d
   ```

---

## 🎯 Conclusão

Este projeto demonstra um fluxo simples de mensageria utilizando RabbitMQ. Para casos mais avançados, você pode explorar **trocas (exchanges)**, **filas duráveis** e **múltiplos consumidores**.

Caso precise de mais funcionalidades, me avise! 🚀

# RabbitMQ Test Project

Este projeto tem como objetivo testar a comunicação entre produtores e consumidores utilizando RabbitMQ com Docker e Python.

## 📌 Requisitos

- **Docker** e **Docker Compose** instalados
- **Python 3.x** instalado
- Biblioteca **pika** instalada (`pip install pika`)

---

## 🚀 Configuração

### 1️⃣ **Subir o RabbitMQ com Docker**

Crie um arquivo `docker-compose.yml` com o seguinte conteúdo:

```yaml
version: '3.8'
services:
  rabbitmq:
    image: rabbitmq:3-management
    container_name: rabbitmq
    restart: always
    ports:
      - "5672:5672"   # Porta para conexões do RabbitMQ
      - "15672:15672" # Painel de administração
    environment:
      RABBITMQ_DEFAULT_USER: admin
      RABBITMQ_DEFAULT_PASS: admin
    volumes:
      - rabbitmq_data:/var/lib/rabbitmq

volumes:
  rabbitmq_data:
    driver: local
```

Agora, execute o comando para iniciar o RabbitMQ:

```bash
docker-compose up -d
```

Acesse o painel de gerenciamento em [http://localhost:15672](http://localhost:15672)

- **Usuário:** `admin`
- **Senha:** `admin`

---

### 2️⃣ **Criar o Produtor (Publisher)**

Crie um arquivo `publisher.py` com o seguinte código:

```python
import pika

# Configurar credenciais
credentials = pika.PlainCredentials('admin', 'admin')

# Conectar ao RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', credentials=credentials)
)
channel = connection.channel()

# Criar a fila
channel.queue_declare(queue='test_queue')

# Enviar mensagem
message = "Olá, RabbitMQ!"
channel.basic_publish(exchange='', routing_key='test_queue', body=message)

print(f" [x] Mensagem enviada: {message}")

# Fechar conexão
connection.close()
```

Execute o publisher:

```bash
python3 publisher.py
```

---

### 3️⃣ **Criar o Consumidor (Consumer)**

Crie um arquivo `consumer.py`:

```python
import pika

# Configurar credenciais
credentials = pika.PlainCredentials('admin', 'admin')

# Conectar ao RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', credentials=credentials)
)
channel = connection.channel()

# Criar fila
channel.queue_declare(queue='test_queue')

def callback(ch, method, properties, body):
    print(f" [x] Mensagem recebida: {body.decode()}")

# Consumir mensagens
channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Aguardando mensagens. Pressione CTRL+C para sair.')
channel.start_consuming()
```

Execute o consumidor:

```bash
python3 consumer.py
```

Agora, o consumidor ficará esperando mensagens. Quando o `publisher.py` for executado, ele enviará mensagens para o RabbitMQ e o `consumer.py` as receberá.

---

## 🛠 Solução de Problemas

1. **Erro de autenticação (ACCESS\_REFUSED)**

   ```
   pika.exceptions.ProbableAuthenticationError: ConnectionClosedByBroker: (403) 'ACCESS_REFUSED'
   ```

   ✅ Certifique-se de que está usando as credenciais corretas no `publisher.py` e `consumer.py`.

2. **Conexão recusada**

   ```
   pika.exceptions.AMQPConnectionError: [Errno 111] Connection refused
   ```

   ✅ Verifique se o RabbitMQ está rodando:

   ```bash
   docker ps
   ```

3. **Painel do RabbitMQ não abre** ✅ Acesse: [http://localhost:15672](http://localhost:15672) ✅ Caso não funcione, reinicie o container:

   ```bash
   docker-compose down && docker-compose up -d
   ```

---

## 🎯 Conclusão

Este projeto demonstra um fluxo simples de mensageria utilizando RabbitMQ. Para casos mais avançados, você pode explorar **trocas (exchanges)**, **filas duráveis** e **múltiplos consumidores**.

Caso precise de mais funcionalidades, me avise! 🚀

