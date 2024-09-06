import redis
r = redis.Redis("localhost")
print(r.ping())

r.set("test", "test")
print(r.get("test"))
