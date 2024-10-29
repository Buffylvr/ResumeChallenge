# Eventually a thing that talks to S3

import boto3


s3 = boto3.client('s3')

def create_bucket(bucket_name, region):
    response =s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )
    print(response)


#testing1fortestingsake1 # don't use _ in the bucket name

def delete_bucket(bucket_name, bucket_owner):
	#bucket_owner is expected per https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_bucket.html
	#bucket_owner is the account ID
    response = s3.delete_bucket(
	    Bucket=bucket_name,
	    ExpectedBucketOwner=bucket_owner
    )
    print(response)


#this function only gives you the first name of the first item back
def list_bucket_contents(bucket_name):
    response = s3.list_objects(
        Bucket=bucket_name
    )
    #print(response)
    item_name = response['Contents'][0]['Key']
    print(item_name)


def list_all_bucket_contents(bucket_name):
    response = s3.list_objects(
        Bucket=bucket_name
    )
#    print("printing everything")
#    print(response)
#    print("printing one thing")
 #   item_name = response['Contents'][0]
    for i in response['Contents']:
        for k, v in i.items():
            if k == 'Key':
                print(v)


