import boto3

dynamodb = boto3.resource('dynamodb',region_name = 'ap-southeast-1')
table = dynamodb.Table('dsm-osm-camara')
response = table.scan()
items = response['Items']
print(items[0])

print(items[0]["location"])