import heapq
import uuid
import math
from collections import defaultdict

# EventNode represents a delivery event at a specific hub
class EventNode:
    def __init__(self, timestamp, location, data):
        self.id = str(uuid.uuid4())[:8]  # Shortened for readability
        self.timestamp = timestamp      # Event time
        self.location = location        # (x, y) coordinates
        self.data = data                # Payload: e.g., package status

    def __lt__(self, other):
        return self.timestamp < other.timestamp

# ChronoMap: Custom structure for spatial-temporal event management
class ChronoMap:
    def __init__(self):
        self.minHeap = []  # Heap of events ordered by timestamp
        self.spatialIndex = defaultdict(list)  # Grid-based spatial index
        self.idMap = {}  # Quick lookup by event ID

    def insert(self, event):
        heapq.heappush(self.minHeap, event)
        key = self._grid_key(event.location)
        self.spatialIndex[key].append(event)
        self.idMap[event.id] = event

    def get_events_in_area_and_time(self, x1, y1, x2, y2, t_start, t_end):
        events = []
        for x in range(math.floor(x1), math.ceil(x2) + 1):
            for y in range(math.floor(y1), math.ceil(y2) + 1):
                key = (x, y)
                for event in self.spatialIndex.get(key, []):
                    if t_start <= event.timestamp <= t_end:
                        events.append(event)
        return events

    def remove_expired(self, current_time):
        while self.minHeap and self.minHeap[0].timestamp < current_time:
            event = heapq.heappop(self.minHeap)
            key = self._grid_key(event.location)
            if event in self.spatialIndex[key]:
                self.spatialIndex[key].remove(event)
            self.idMap.pop(event.id, None)

    def _grid_key(self, location):
        return (math.floor(location[0]), math.floor(location[1]))

# EventWave Propagation Simulation
def simulate_delivery_wave(initial_events, max_time=5, wave_delay=1, radius=1):
    chrono_map = ChronoMap()
    for event in initial_events:
        chrono_map.insert(event)

    current_time = 0
    while current_time <= max_time:
        print(f"\n=== Time {current_time} ===")
        chrono_map.remove_expired(current_time)
        events_now = chrono_map.get_events_in_area_and_time(-100, -100, 100, 100, current_time, current_time)

        for event in events_now:
            print(f"[{event.timestamp}] Hub {event.location} | {event.data}")
            # Propagate to neighboring hubs (N, S, E, W)
            directions = [(0, radius), (0, -radius), (radius, 0), (-radius, 0)]
            for dx, dy in directions:
                new_location = (event.location[0] + dx, event.location[1] + dy)
                new_data = f"Propagated from {event.id}"
                new_event = EventNode(current_time + wave_delay, new_location, new_data)
                chrono_map.insert(new_event)
        current_time += 1

# Entry point: Start simulation with a single delivery event
if __name__ == "__main__":
    initial_event = EventNode(timestamp=0, location=(0, 0), data="Shipment Arrived at Hub (0,0)")
    simulate_delivery_wave([initial_event], max_time=6, wave_delay=1, radius=1)
