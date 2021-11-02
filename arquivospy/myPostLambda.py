import json
import boto3
from datetime import datetime
from boto3.dynamodb.conditions import Key


# Conexão com o Banco de Dados DynamoDB
dynamodb = boto3.resource('dynamodb')

# Conexão com a Tabela de Mensagens
tabela = dynamodb.Table('MensagensDavi')


def lambda_handler(event, context):
    response = tabela.query(
        KeyConditionExpression=Key('origem').eq(event['from']))

    body=[
        {
            'data_hora': (datetime.now()).strftime("%Y-%m-%d %H:%M:%S"),
            'msg': event['msg']
        }
    ]

    for x in response['Items']:
        if x['destino'] == event['to']:
            body.append(x['bo'])
            break

    return tabela.put_item(
        Item = {
            'origem': event['from'],
            'destino': event['to'],
            'body': body
        }
    )
