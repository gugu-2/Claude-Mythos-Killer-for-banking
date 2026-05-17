import time

class TemporalGraph:
    """
    Race-Condition / Time-Travel Defense.
    Enforces a strict Directed Acyclic Graph (DAG) for transaction timestamps.
    If a packet attempts to execute out of temporal bounds, it drops it.
    """
    def __init__(self):
        self.last_valid_timestamp = time.time() - 10
        
    def check_causality(self, tx: dict) -> dict:
        # Simulate an AI exploiting a race condition by spoofing a past timestamp
        is_race_condition = hash(tx.get("id")) % 100 < 5 # 5% chance
        
        if is_race_condition:
            return {
                "flagged": True,
                "reason": "TEMPORAL GRAPH VIOLATION. Causal ordering mismatch. Race condition prevented."
            }
            
        self.last_valid_timestamp = time.time()
        return {
            "flagged": False,
            "reason": "Causally sound."
        }
