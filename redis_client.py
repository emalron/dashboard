import redis

r = redis.Redis(host='localhost', port=6379, db=0)

value = r.get('server_metrics')

print(value)