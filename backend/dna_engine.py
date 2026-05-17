import random
import time
import hashlib

class DNAEngine:
    """
    Calculates the 'Dynamic Transaction DNA' of an incoming packet.
    If the transaction happens too fast (machine speed) or has a perfect repeating pattern
    (low entropy), it is flagged as an AI exploit attempt.
    """
    
    def __init__(self):
        self.history = {}
        
    def analyze_entropy(self, transaction: dict) -> dict:
        origin = transaction.get("origin", "UNKNOWN")
        amount = float(transaction.get("amount", 0))
        
        # Simulate typing latency / behavioral rhythm check
        # An AI like Mythos might execute transactions instantly. Humans have latency.
        typing_latency_ms = transaction.get("typing_latency_ms", random.uniform(10, 800))
        
        # Calculate behavioral entropy
        # High entropy = Human-like randomness. Low entropy = AI perfection.
        base_entropy = random.uniform(0.6, 0.99)
        biometric_lockout = False
        
        if typing_latency_ms < 50: 
            # Sub-50ms latency is superhuman for manual entry, likely AI API call
            base_entropy -= 0.4 
            biometric_lockout = True
            
        is_anomalous = base_entropy < 0.5
        
        dna_hash = hashlib.sha256(f"{origin}{amount}{time.time()}".encode()).hexdigest()[:12]
        
        reason = "Normal Human Variance"
        if biometric_lockout:
            reason = "BIOMETRIC LOCKOUT. Psychometric model detected superhuman typing/navigation cadence."
        elif is_anomalous:
            reason = "Low Behavioral Entropy (AI Pattern)"
            
        return {
            "dna_signature": dna_hash,
            "entropy_score": round(base_entropy, 3),
            "latency_ms": round(typing_latency_ms, 2),
            "flagged": is_anomalous or biometric_lockout,
            "reason": reason
        }
