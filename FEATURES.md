# Aegis Sentinel: Feature Architecture

This document outlines the advanced, out-of-the-box defensive algorithms implemented in the Aegis Sentinel backend. These features are designed to solve critical business vulnerabilities and defend legacy infrastructure against AGI-level threats.

## 1. The Money Quarantine Layer
**The Concept**: In traditional banking, money transfers immediately. In this architecture, transactions are intentionally delayed.
**How it Works**: All inbound packets are immediately isolated in a holding cell. During this 1-3 second simulated window, the backend runs extensive algorithmic validation.

## 2. Dynamic Transaction DNA (Psychometric Modeling)
**The Concept**: AI perfectly mimics human inputs, but humans are inherently imperfect.
**How it Works**: The `dna_engine.py` calculates a "Behavioral Entropy Score" based on typing latency, geographic rhythm, and origin consistency. If a transaction is submitted with superhuman speed (<50ms latency), it triggers a `BIOMETRIC LOCKOUT` for AI-spoofing.

## 3. Autonomous AI Guardian Swarms
**The Concept**: A single cybersecurity firewall is a single point of failure.
**How it Works**: The `guardian_swarm.py` deploys 5 distinct micro-agent models (Fraud, Geo, Timing, Pattern, Quantum Crypto). They argue about the validity of a packet. At least 4 out of 5 agents must reach "Safe Consensus". If consensus breaks, the transaction is dropped.

## 4. Shadow Ledger Cryptographic Verification
**The Concept**: An AGI might exploit memory buffers to alter a transaction after it passes the firewall but before it hits the database.
**How it Works**: `shadow_ledger.py` generates a deterministic SHA-384 hash of the intended transaction state. Right before committing to the COBOL core, it compares the current memory state to the shadow hash. Any tampering results in an immediate block.

## 5. Fractional Skimming Monitor ("Salami Slicing" Defense)
**The Concept**: An advanced AI wouldn't steal billions at once; it would steal $0.001 from 100 million accounts, flying under standard fraud velocity radars.
**How it Works**: `fractional_monitor.py` tracks micro-cent discrepancies across the entire global state. If the aggregate fractional drift exceeds mathematical norms, the system flags the anomalous transactions.

## 6. Temporal Transaction Graphing
**The Concept**: AI could exploit legacy End-of-Day batch processing windows by spoofing timestamps to create race-conditions or double-spends.
**How it Works**: `temporal_graph.py` enforces a strict Directed Acyclic Graph (DAG) for causal ordering. Packets that violate the temporal laws of physics (arriving before they were sent, or trying to bypass causal sequence) are rejected.

## 7. Quantum-Resistant Vault Sharding
**The Concept**: A compromised server gives an attacker access to an entire liquidity pool.
**How it Works**: `vault_sharding.py` fragments large transactions (>$10,000) into encrypted micro-vaults. An attacker breaching one node only intercepts a useless, fragmented cryptographic hash. It requires Multi-Party Computation (MPC) to reassemble the transaction.

## 8. Generative Deception Networks (Honeypots)
**The Concept**: Hackers map networks to find vulnerabilities. We give them a fake map.
**How it Works**: `deception_network.py` hosts highly-privileged, fake API endpoints (e.g., `/api/v1/swift_gateway_override`). If any incoming packet touches these traps, the originating IP is permanently and globally shadow-banned.

## 9. Moving Target Topology
**The Concept**: Static infrastructure is a sitting duck. 
**How it Works**: `moving_target.py` runs an asynchronous background loop that actively mutates internal gateway ports, COBOL bridge IPs, and generative API schema endpoints every 15-30 seconds. A mapped network becomes obsolete almost instantly.

## 10. The "Dead Man's Switch" (Autonomous Core Severance)
**The Concept**: If an AGI breaches the perimeter, its first move would be locking humans out. The system must know how to kill itself to save the bank.
**How it Works**: Found in `main.py`, if the backend detects an overwhelming, coordinated anomaly velocity (8 critical threats in a row), it executes a `CORE SEVERANCE`. It intentionally corrupts its own routing tables and logically isolates the COBOL core from the network. It requires a physical human hardware reset in the data center to move funds again.
