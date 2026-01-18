import boto3


def main():
    # metadata
    # pk: USER#1, sk: METADATA, name: "John Doe", email: "<Email>", picture: "<Picture URL>", phone: "<Phone Number>", createdAt: "<Timestamp>"
    # pk: GROUP#1, sk: METADATA, name: "Group 1", description: "This is group 1", picture: "<Picture URL>", createdAt: "<Timestamp>"
    # pk: GROUP#1, sk: MEMBER#USER#1, joinedAt: "<Timestamp>"
    # pk: GROUP#1, sk: MEMBER#USER#2#DATE#<Timestamp>, name: "Item 1", description: "This is item 1", cost: 100, who_added: "user#1", for_whom: "{user#2}", createdAt: "<Timestamp>"
    dynamodb = boto3.client('dynamodb')
    dynamodb.put_item(
        TableName='fairbuddy_test',
        Item={
            'pk': {'S': 'item#2'},
            'sk': {'N': '10'},
        }
    )

if __name__ == "__main__":
    main()
