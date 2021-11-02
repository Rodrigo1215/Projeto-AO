import json
import boto3
from boto3.dynamodb.conditions import Key


# Conexão com o Banco de Dados DynamoDB
dynamodb = boto3.resource('dynamodb')

# Conexão com a Tabela de Mensagens
tabela = dynamodb.Table('MensagensDavi')


def lambda_handler(event, context):
    response = tabela.query(
        KeyConditionExpression = Key('origem').eq(event['from'])
    )

    for x in response['Items']:
        if x['destino'] == event['to']:
            return x

    return None
