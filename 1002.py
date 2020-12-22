from collections import defaultdict, deque
class Solution:
    """
    @param routes:  a list of bus routes
    @param S: start
    @param T: destination
    @return: the least number of buses we must take to reach destination
    """
    def numBusesToDestination(self, routes, S, T):
        # Write your code here
        stop_to_bus = defaultdict(set)
        
        for i in range(len(routes)):
            for stop in routes[i]:
                stop_to_bus[stop].add(i)
                
        visited_bus = set()
        visited_stop = set()
        queue = deque([])
        queue.append(S)
        visited_stop.add(S)
        
        count = 0 
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                stop = queue.popleft()
                if stop == T:
                    return count 
                    
                buses = stop_to_bus.get(stop)
                for bus in buses:
                    if bus in visited_bus:
                        continue 
                    
                    visited_bus.add(bus)
                    for next_stop in routes[bus]:
                        if next_stop not in visited_stop:
                            visited_stop.add(next_stop)
                            queue.append(next_stop)
                        
            count += 1 
            
        return -1
