from __future__ import print_function
import boto3

def auth_handler(event, context):
    token = event['authorizationToken']

    if token == 'allow':
        return generatePolicy('user', 'Allow', event['methodArn'])
    elif token == 'deny':
        return generatePolicy('user', 'Deny', event['methodArn'])
    elif token == 'unauthorized':
        return "Unauthorized"
    else:
        return "error"

def generatePolicy(principalId, effect, resource):
    authResponse = {}
    authResponse['principalId'] = principalId
    if effect and resource:
        policyDocument = {}
        policyDocument['Version'] = '2012-10-17'
        policyDocument['Statement'] = []
        
        statementOne = {}
        statementOne['Action'] = 'execute-api:Invoke'
        statementOne['Effect'] = effect
        statementOne['Resource'] = resource
        policyDocument['Statement'].append(statementOne)
        
        authResponse['policyDocument'] = policyDocument
    return authResponse
