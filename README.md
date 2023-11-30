# Sistema de Rastreamento de Atividades com RabbitMQ

Este projeto é um exemplo de implementação de um sistema de rastreamento de atividades utilizando RabbitMQ para comunicação assíncrona entre diferentes partes de um aplicativo distribuído. Projetado para ajudar a consolidar o conhecimento do curso rabbitMQ do Full Cycle.

## Estrutura do Projeto

producer.py: Script que simula produtores de eventos.
consumer.py: Script que atua como consumidor, processando e registrando os eventos.

## Requisitos

- Python 3.x
- docker

## Configuração

## Configuração do Projeto e Execução com Ambiente Virtual (env)

Para executar a aplicação usando um ambiente virtual (env), siga estas etapas:

1. Clone este repositório em sua máquina local:

   ```
   git clone https://github.com/MarinaSpadetto/activity_tracking_rabbitmq
   ```

2. Crie um ambiente virtual usando venv ou virtualenv:

   ```
   python3 -m venv venv
   ```

3. Ative o ambiente virtual:

   No Windows:
    ```
    venv\Scripts\activate
    ```

   No macOS e Linux:
    ```
    source venv/bin/activate
    ```

4. Instale as dependências do projeto:

   ```
   pip install -r requirements.txt
   ```

5. Execute este comando para subir um container do rabbitMQ.
   ```
   docker-compose up -d
   ```

7. Abra uma aba no terminal e execute o produtor de evento para simular eventos:

   ```
   python producer.py
   ```

8. Abra outra aba no terminal e execute o consumidor para processar e registrar os eventos:

   ```
   python consumer.py
   ```


## Docs utilizados

- https://www.rabbitmq.com/tutorials/tutorial-one-python.html
- https://hub.docker.com/_/rabbitmq
- https://pika.readthedocs.io/en/stable/intro.html

---

*Desenvolvido por Marina Spadetto*
