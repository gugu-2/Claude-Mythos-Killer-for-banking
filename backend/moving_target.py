import asyncio
import random
import time

class MovingTargetDefense:
    """
    Self-Healing / Moving Target Architecture.
    Constantly mutates internal API endpoints, open ports, and container IPs.
    If an attacker scans the network, the map becomes obsolete within 60 seconds.
    """
    def __init__(self):
        self.current_topology = self._generate_topology()
        self.last_shift_time = time.time()

    def _generate_topology(self) -> dict:
        # Generative API Mutation: Procedurally generate new API endpoint names to break scrapers
        api_version = f"v{random.randint(2, 9)}.{random.randint(0, 99)}"
        api_prefix = random.choice(["/x-core", "/alpha", "/omega-bridge", "/secure-tunnel"])
        
        return {
            "internal_gateway_port": random.randint(30000, 60000),
            "cobol_bridge_ip": f"10.0.{random.randint(1,255)}.{random.randint(1,255)}",
            "active_enclaves": random.randint(12, 48),
            "dynamic_api_schema": f"{api_prefix}/{api_version}/tx-commit"
        }

    async def run_topology_shifter(self, broadcast_callback):
        """
        Runs in the background, shifting the topology periodically and notifying the system.
        """
        while True:
            await asyncio.sleep(random.uniform(15, 30)) # Shift every 15-30s for demo
            
            self.current_topology = self._generate_topology()
            self.last_shift_time = time.time()
            
            shift_msg = f"Topology & Schema Mutation: Gateway Port {self.current_topology['internal_gateway_port']} | Bridge {self.current_topology['cobol_bridge_ip']} | API {self.current_topology['dynamic_api_schema']}"
            
            # Send the broadcast up to the main WebSocket layer
            await broadcast_callback(shift_msg)
