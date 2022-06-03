import redis

client = redis.Redis(host='localhost', port=6379, db=0)

client.set('name', 'Yevhenii')
print(client.get('name'))
client.delete('name')

client.close()
