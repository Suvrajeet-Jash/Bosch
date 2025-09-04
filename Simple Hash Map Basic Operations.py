class SimpleHashMap:
    def __init__(self, size=10):
        self.size = size
        self.map = [[] for _ in range(size)]
    
    def _hash(self, key):
        # Simple hash function: sum of char codes modulo size
        return sum(ord(c) for c in str(key)) % self.size
    
    def put(self, key, value):
        index = self._hash(key)
        bucket = self.map[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    
    def get(self, key):
        index = self._hash(key)
        bucket = self.map[index]
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def remove(self, key):
        index = self._hash(key)
        bucket = self.map[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False


if __name__ == "__main__":
    hashmap = SimpleHashMap()
    
    while True:
        command = input("Enter command (put/get/remove/exit): ").strip().lower()
        if command == "put":
            key = input("Key: ")
            value = input("Value: ")
            hashmap.put(key, value)
            print(f"Inserted ({key}: {value})")
        elif command == "get":
            key = input("Key: ")
            value = hashmap.get(key)
            if value is not None:
                print(f"Value: {value}")
            else:
                print("Key not found.")
        elif command == "remove":
            key = input("Key: ")
            if hashmap.remove(key):
                print("Key removed.")
            else:
                print("Key not found.")
        elif command == "exit":
            break
        else:
            print("Invalid command. Use put/get/remove/exit.")
