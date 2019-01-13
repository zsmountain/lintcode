'''
Implement a load balancer for web servers. It provide the following functionality:

Add a new server to the cluster => add(server_id).
Remove a bad server from the cluster => remove(server_id).
Pick a server in the cluster randomly with equal probability => pick().
Have you met this question in a real interview?  
Example
At beginning, the cluster is empty => {}.

add(1)
add(2)
add(3)
pick()
>> 1         // the return value is random, it can be either 1, 2, or 3.
pick()
>> 2
pick()
>> 1
pick()
>> 3
remove(1)
pick()
>> 2
pick()
>> 3
pick()
>> 3
'''

import random

class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.servers = []
        self.servers_map = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        if server_id in self.servers_map:
            return
        size = len(self.servers_map)
        if len(self.servers) == size:
            self.servers.append(server_id)
        else:
            self.servers[size] = server_id
            
        self.servers_map[server_id] = size

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        if server_id not in self.servers:
            return
        pos = self.servers_map[server_id]
        size = len(self.servers_map)
        self.servers_map[self.servers[size - 1]] = pos
        self.servers[pos], self.servers[size - 1] = self.servers[size - 1], self.servers[pos]
        del self.servers_map[server_id]
        
    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        size = len(self.servers_map)
        return self.servers[random.randint(0, size - 1)]

s = LoadBalancer()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(6)
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
s.remove(1)
s.remove(6)
print(s.pick())
print(s.pick())
print(s.pick())
s.add(11)
s.add(22)
s.add(33)
s.add(44)
s.add(55)
s.add(66)
s.remove(11)
s.remove(22)
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
