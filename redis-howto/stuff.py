import redis

r = redis.Reddis(host='172.28.128.3', port=6379, db=0)

r.set('foo', 1)

for i in range(2**16):
    r.incr('foo')

print(r.get('foo'))