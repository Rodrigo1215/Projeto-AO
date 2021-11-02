import json
from datetime import datetime
import boto3


# Os dois comandos abaixo estao fora do handler para melhor performance
# Conexão com o Banco de Dados DynamoDB
dynamodb = boto3.resource('dynamodb')

# Conexão com a Tabela de Mensagens
# Deve haver uma tabela com o nome abaixo:
tableMensagens = dynamodb.Table('MensagensDavi')


def lambda_handler(event, context):
    # Data e hora para registrar na mensagem
    data_hora = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    # Dados da mensagem vindos via HTTP POST
    # As chaves de event[] devem bater com os ids do formulário
    remetente = str(event['from'])
    destinatario = str(event['to'])
    mensagem = str(event['msg'])

    # O try/catch é para erro no acesso ao DynamoDB
    try:
        # Uma role deve ser configurada para a esta função,
        # permitindo PutItem para DynamoDB
        tableMensagens.put_item(
            Item={
                'remetente': remetente,
                'data_hora': data_hora,
                'destinatario': destinatario,
                'mensagem': mensagem
            }
        )

        return{
            # Sucesso
            'statusCode': 200,
            'body': json.dumps('Mensagem de '
                               + remetente
                               + ' para '
                               + destinatario
                               + ' inserida no Banco de Dados')
        }

    except:
        # Erro: print() coloca mensagem de erro no log da função lambda
        print('Erro: lambda function terminada sem sucesso')
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar processar mensagem')
        }
