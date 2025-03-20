# LogiWave
Simulate spatial-temporal event propagation in logistics networks. Delivery status waves ripple through hubs over time — powered by a custom ChronoMap data structure.

📦 Logistics EventWave Simulator
Simulate delivery chain events as they ripple through logistics hubs over time and geography. Each event represents a package update, and waves simulate status propagation (e.g., arrival notifications, transfer alerts) to nearby hubs.

🚀 Features
Custom ChronoMap data structure to manage time-ordered and spatially-indexed events.
Propagation of delivery events through logistics hubs in a wave-like pattern.
Efficient querying by time window and location bounds.
Auto-cleanup of expired events to maintain real-time simulation.
🗺️ Use Case
Simulates package or shipment updates across a network of delivery hubs. For instance:

A shipment arrives at Hub A → nearby Hubs B, C, D get notified after 1 hour → notifications propagate onward.

📂 Project Structure
bash
Copy
Edit
logistics_eventwave_simulator/
│
├── eventwave.py          # Main simulation code
├── README.md             # Project documentation (this file)
🧱 Core Components
1. EventNode
Represents a delivery event.

python
Copy
Edit
EventNode:
  - id: unique identifier
  - timestamp: time of event
  - location: (x, y) coordinates of hub
  - data: payload (e.g., package status)
2. ChronoMap
Custom structure for efficient management:

MinHeap → Orders events by time.
Spatial Index (Grid-based) → Quick spatial access.
HashMap → O(1) event lookup.
3. EventWave Propagation
Algorithm to simulate delivery event ripple effect over time:

At each tick, propagate events to neighbor hubs.
Delay propagation to mimic real-world processing or transfer time.
🖥️ Usage Example
bash
Copy
Edit
# Run the simulation
python eventwave.py
Sample Output:

vbnet
Copy
Edit
Time 0:
Event at Hub (0, 0): Shipment Arrived

Time 1:
Event at Hub (1, 0): Propagation from 1st event
Event at Hub (-1, 0): Propagation from 1st event
...
🔧 Customize Simulation
You can modify:

max_time: How many time ticks to simulate.
wave_delay: Time delay between propagation steps.
radius: How far the event reaches (e.g., distance to neighbor hubs).
initial_events: Inject multiple starting points.
📈 Potential Extensions
Visualize hubs and event waves with matplotlib or Plotly.
Add event decay after N waves.
Integrate with real logistics data for replay analysis.
📜 License
MIT License — free to use and modify.

🤝 Contribute
Got ideas to enhance event propagation or optimize spatial indexing (e.g., QuadTree)? PRs welcome!
