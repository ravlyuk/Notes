import redis

with redis.Redis(host="localhost", port=6379, db=0) as client:
    # set, get, delete
    client.set("name", "Yevhenii")
    print(client.get("name"))
    client.delete("name")

    # increment
    client.set("num", 1)
    client.incr("num")
    print(client.get("num"))

    # increment by
    client.incrby("num", 3)
    print(client.get("num"))

    # show all keys
    print("all keys:", client.keys("*"))
