class DeceptionNetwork:
    """
    AI-Generated Deception Networks.
    Deploys dynamic "Fake APIs" (Honeypots). If an attacker probes these endpoints,
    their origin IP is permanently shadow-banned across the entire banking cluster.
    """
    def __init__(self):
        self.shadow_ban_list = set()
        # Simulated fake endpoints that shouldn't receive legitimate traffic
        self.honeypot_endpoints = ["/api/v1/legacy_admin", "/api/v1/debug/db", "/api/v1/swift_gateway_override"]

    def check_and_trap(self, tx: dict) -> dict:
        origin = tx.get("origin", "UNKNOWN")
        
        # If origin is already banned, drop instantly
        if origin in self.shadow_ban_list:
            return {
                "trapped": True,
                "reason": f"Origin {origin} is globally shadow-banned."
            }

        # Simulate an AI attacker probing a honeypot endpoint
        # For simulation, we randomly assume 10% of anomalous transactions touch a honeypot
        probed_honeypot = False
        touched_endpoint = ""
        
        if origin.startswith("UNKNOWN_NODE") and (hash(tx.get("id")) % 10) > 7:
            probed_honeypot = True
            touched_endpoint = self.honeypot_endpoints[hash(tx.get("id")) % len(self.honeypot_endpoints)]

        if probed_honeypot:
            self.shadow_ban_list.add(origin)
            return {
                "trapped": True,
                "reason": f"Honeypot intrusion on {touched_endpoint}. Origin {origin} permanently shadow-banned."
            }

        return {
            "trapped": False,
            "reason": "Clear."
        }
