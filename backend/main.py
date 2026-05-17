import asyncio
import json
import random
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from dna_engine import DNAEngine
from guardian_swarm import GuardianSwarm
from shadow_ledger import ShadowLedger
from deception_network import DeceptionNetwork
from moving_target import MovingTargetDefense
from fractional_monitor import FractionalMonitor
from temporal_graph import TemporalGraph
from vault_sharding import VaultSharding

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dna_engine = DNAEngine()
swarm = GuardianSwarm()
ledger = ShadowLedger()
deception = DeceptionNetwork()
mtd = MovingTargetDefense()
fractional_monitor = FractionalMonitor()
temporal_graph = TemporalGraph()
vault = VaultSharding()

active_websockets = []
system_severed = False  # Global state for Dead Man's Switch
anomaly_counter = 0

async def broadcast_topology_shift(message: str):
    for ws in active_websockets:
        try:
            await ws.send_json({"type": "log", "level": "warn", "message": message})
        except Exception:
            pass

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(mtd.run_topology_shifter(broadcast_topology_shift))

async def process_transaction(tx: dict, websocket: WebSocket):
    global system_severed
    global anomaly_counter
    
    if system_severed:
        tx["status"] = "blocked"
        tx["progress"] = 3
        await websocket.send_json({"type": "tx_update", "data": tx})
        return

    # 0. Check Deception Network
    deception_check = deception.check_and_trap(tx)
    if deception_check["trapped"]:
        tx["status"] = "blocked"
        tx["progress"] = 3
        anomaly_counter += 2
        await websocket.send_json({"type": "log", "level": "crit", "message": f"[DECEPTION TRAP] {deception_check['reason']}"})
        await websocket.send_json({"type": "tx_update", "data": tx})
        return

    # 1. Quarantine
    tx["status"] = "quarantine"
    tx["progress"] = 0
    await websocket.send_json({"type": "tx_update", "data": tx})
    await asyncio.sleep(0.5)
    
    # 2a. Temporal Graphing (Race Conditions)
    temporal_res = temporal_graph.check_causality(tx)
    if temporal_res["flagged"]:
        tx["status"] = "blocked"
        tx["progress"] = 3
        anomaly_counter += 1
        await websocket.send_json({"type": "log", "level": "crit", "message": temporal_res['reason']})
        await websocket.send_json({"type": "tx_update", "data": tx})
        return
        
    # 2b. Fractional Skimming Monitor
    frac_res = fractional_monitor.check_fractional_drift(tx)
    if frac_res["flagged"]:
        tx["status"] = "blocked"
        tx["progress"] = 3
        anomaly_counter += 1
        await websocket.send_json({"type": "log", "level": "crit", "message": frac_res['reason']})
        await websocket.send_json({"type": "tx_update", "data": tx})
        return

    # 2c. DNA Engine & Psychometric Biometrics
    dna_res = dna_engine.analyze_entropy(tx)
    tx["dna_result"] = dna_res
    tx["progress"] = 1
    
    if dna_res["flagged"]:
        anomaly_counter += 1
        await websocket.send_json({"type": "log", "level": "warn", "message": f"DNA Engine flagged {tx['id']}: {dna_res['reason']}"})
    else:
        await websocket.send_json({"type": "log", "level": "info", "message": f"DNA Engine passed {tx['id']}. Entropy: {dna_res['entropy_score']}"})
        
    await websocket.send_json({"type": "tx_update", "data": tx})
    await asyncio.sleep(1.0)
    
    # 3. Guardian Swarm
    swarm_res = swarm.evaluate(tx, dna_res)
    tx["progress"] = 2
    
    for log_msg in swarm_res["logs"]:
         await websocket.send_json({"type": "log", "level": "warn", "message": log_msg})
         
    if not swarm_res["consensus"]:
        tx["status"] = "blocked"
        tx["progress"] = 3
        anomaly_counter += 1
        await websocket.send_json({"type": "log", "level": "crit", "message": f"Swarm consensus failed for {tx['id']}. Blocking packet."})
        await websocket.send_json({"type": "tx_update", "data": tx})
    else:
        await websocket.send_json({"type": "log", "level": "info", "message": f"Swarm consensus reached ({swarm_res['votes_safe']}/{swarm_res['total_agents']}) for {tx['id']}."})
        await websocket.send_json({"type": "tx_update", "data": tx})
        
    await asyncio.sleep(0.5)
    
    # Dead Man's Switch Logic
    if anomaly_counter >= 8 and not system_severed:
        system_severed = True
        await websocket.send_json({"type": "log", "level": "crit", "message": "CRITICAL: DEAD MAN'S SWITCH TRIGGERED. Massive anomalous assault detected."})
        await websocket.send_json({"type": "log", "level": "crit", "message": "AUTONOMOUS CORE SEVERANCE EXECUTED. Hardware relay disconnected. COBOL Core offline."})
        await websocket.send_json({"type": "severance"})
        return
        
    if tx["status"] == "blocked": return
    
    # 4. Shadow Ledger
    ledger_res = ledger.verify(tx)
    if not ledger_res["verified"]:
        tx["status"] = "blocked"
        tx["progress"] = 3
        await websocket.send_json({"type": "log", "level": "crit", "message": f"Shadow Ledger mismatch for {tx['id']}: {ledger_res['reason']}"})
        await websocket.send_json({"type": "tx_update", "data": tx})
        return
        
    # 5. Quantum-Resistant Vault Sharding
    shard_res = vault.shard_transaction(tx)
    if shard_res["sharded"]:
        await websocket.send_json({"type": "log", "level": "info", "message": shard_res["message"]})
        
    # Commit
    tx["status"] = "verified"
    tx["progress"] = 3
    await websocket.send_json({"type": "log", "level": "info", "message": f"Validation complete. Forwarding to COBOL via {mtd.current_topology['cobol_bridge_ip']}."})
    await websocket.send_json({"type": "tx_update", "data": tx})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_websockets.append(websocket)
    
    id_counter = 105000
    try:
        while True:
            await asyncio.sleep(random.uniform(2.0, 4.0))
            if system_severed:
                await asyncio.sleep(10)
                continue
                
            id_counter += 1
            is_anomalous = random.random() > 0.7
            
            node_id = random.randint(1, 15)
            origin_name = f"UNKNOWN_NODE_{node_id}" if is_anomalous else f"NODE_{random.randint(1, 99)}"
            
            tx = {
                "id": f"TX-{str(id_counter).zfill(6)}",
                "amount": round(random.uniform(100, 50000), 2),
                "origin": origin_name,
                "dest": f"ACCT_{random.randint(1000, 9999)}",
                "typing_latency_ms": random.uniform(5, 40) if is_anomalous else random.uniform(100, 800)
            }
            
            await websocket.send_json({"type": "log", "level": "info", "message": f"Intercepted packet {tx['id']}. Routing to Quarantine."})
            asyncio.create_task(process_transaction(tx, websocket))
            
    except WebSocketDisconnect:
        active_websockets.remove(websocket)
        print("Client disconnected")
