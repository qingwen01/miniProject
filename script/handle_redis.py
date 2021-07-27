import redis

conn = redis.Redis(host='10.10.0.138',port=6379)
print(conn.get(13735887043))