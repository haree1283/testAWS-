# import boto3
# import boto3
#
# # Create an S3 client
# s3 = boto3.client('s3')
#
# # List S3 buckets
# response = s3.list_buckets()
# for bucket in response['Buckets']:
#     print(f'Bucket Name: {bucket["Name"]}')
#
# # Initialize AWS client for API Gateway
# client = boto3.client('apigateway')
#
# # Specify your API ID (replace with your actual API ID)
# api_id = 'YOUR_API_ID'
# Access_key_ID= "AKIA4F52A4XRZFMOAKUZ"
# Secret_access_key ="GNwOm3ub2RZtIamPox5FzxgqneF65rpJpkYUpW8m"
# # Create the "test" resource under the root "/"
# response = client.create_resource(
#     restApiId=api_id,
#     parentId='/',
#     pathPart='test'
# )
#
# # Get the resource ID for the "test" resource
# resource_id = response['id']
#
# # Deploy the API to make the changes effective
# client.create_deployment(
#     restApiId=api_id,
#     stageName='prod'  # Replace with your desired stage name
# )

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