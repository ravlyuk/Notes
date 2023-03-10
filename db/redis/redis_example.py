import redis

with redis.Redis(host="localhost", port=6379, db=0) as client:
    client.flushall()

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

    # get all keys generator
    print("all keys:", client.scan_iter("*", count=100))

    # add to list
    client.lpush("lst", 1)
    client.lpush("lst", 2)
    client.lpush("lst", 3)
    print("list:", client.lrange("lst", 0, 10_000))

    # len list
    print("len lst: ", client.llen("lst"))

    # get by infex
    print("lindex:", client.lindex("lst", 0))

    # insert into list
    client.linsert("lst", "before", "2", "2.5")
    print("list after insert:", client.lrange("lst", 0, 10_000))
