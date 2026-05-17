import random

class GuardianSwarm:
    """
    Simulates thousands of micro-defense AIs. We'll abstract this into 5 distinct agent models.
    They must argue and reach consensus. If consensus breaks, the transaction is killed.
    """
    
    def evaluate(self, transaction: dict, dna_result: dict) -> dict:
        agents = ["FraudAgent", "GeoAgent", "TimingAgent", "PatternAgent", "QuantumCryptoAgent"]
        
        votes = []
        logs = []
        
        for agent in agents:
            # Agents vote based on different criteria
            vote_safe = True
            if agent == "TimingAgent" and dna_result.get("entropy_score", 1.0) < 0.5:
                vote_safe = False
                logs.append(f"{agent} voted REJECT: Unnatural timing entropy.")
            elif agent == "PatternAgent" and float(transaction.get("amount", 0)) > 40000 and random.random() < 0.3:
                vote_safe = False
                logs.append(f"{agent} voted REJECT: Velocity spike anomaly detected.")
            elif agent == "GeoAgent" and transaction.get("origin", "").startswith("UNKNOWN"):
                vote_safe = False
                logs.append(f"{agent} voted REJECT: Ghost routing origin.")
                
            votes.append(vote_safe)
        
        # 4 out of 5 agents must agree it's safe
        safe_count = sum(votes)
        consensus_reached = safe_count >= 4
        
        return {
            "consensus": consensus_reached,
            "votes_safe": safe_count,
            "total_agents": len(agents),
            "logs": logs
        }
