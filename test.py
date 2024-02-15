
import boto3

# Initialize the API Gateway client
apigateway = boto3.client('apigateway')

# Initialize a list to store all APIs
all_apis = []

# Paginate through the API results
paginator = apigateway.get_paginator('get_rest_apis')
for page in paginator.paginate():
    all_apis.extend(page['items'])

# Iterate through the list of all APIs and print their names and IDs
for api in all_apis:
    api_name = api['name']
    api_id = api['id']
    print(f"API Name: {api_name}, API ID: {api_id}")

print(len(all_apis))