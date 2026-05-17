class FractionalMonitor:
    """
    Salami Slicing / Fractional Skimming Defense.
    Tracks aggregate fractional discrepancies (micro-cents) over time.
    If the discrepancy pool grows unexplainably, an AI might be skimming.
    """
    def __init__(self):
        self.aggregate_skim = 0.0
        
    def check_fractional_drift(self, tx: dict) -> dict:
        amount = tx.get("amount", 0.0)
        
        # Simulate fractional residue (e.g., rounding differences)
        # 1% chance a transaction has an unnatural micro-cent residue
        has_anomalous_residue = hash(tx.get("id")) % 100 < 1
        
        if has_anomalous_residue:
            # Add a fraction of a cent
            self.aggregate_skim += 0.001
            
        # Threshold: if aggregate skim reaches 0.005 quickly, flag it
        if self.aggregate_skim > 0.005:
            # Reset to prevent endless blocking for simulation
            self.aggregate_skim = 0.0
            return {
                "flagged": True,
                "reason": "FRACTIONAL SKIMMING DETECTED. Micro-cent discrepancy threshold exceeded."
            }
            
        return {
            "flagged": False,
            "reason": "Clean"
        }
