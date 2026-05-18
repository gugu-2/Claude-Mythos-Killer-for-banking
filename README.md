# Aegis Sentinel: AI-Native Banking Defense Layer

**Aegis Sentinel** is a next-generation cybersecurity architecture designed to protect legacy COBOL mainframe systems from Advanced Artificial General Intelligence (AGI) threats. 

Instead of undertaking a decades-long, risky migration to rewrite 40-year-old banking infrastructure, Aegis Sentinel acts as a **Predictive AI Proxy Layer**. It wraps around legacy systems in a zero-trust envelope, analyzing, simulating, and neutralizing threats *before* they touch the core banking ledgers.

### System Demonstrations

#### 1. Live Defense Dashboard (Deception & Moving Target Topology)
![Aegis Sentinel Advanced Defense](./assets/aegis_advanced_features.webp)

#### 2. The "Dead Man's Switch" (Autonomous Core Severance)
![Aegis Sentinel Core Severance](./assets/aegis_phase3_severance.webp)

## Project Architecture

This project consists of two main components:
1. **Python FastAPI Backend (`/backend`)**: The algorithmic brain. It intercepts packets and runs them through multiple complex defensive mathematical models.
2. **React + Vite Dashboard (`/src`)**: A high-fidelity, Palantir-inspired "cyber nervous system" dashboard that visualizes the packet processing and autonomous decisions made by the backend in real-time via WebSockets.

## How to Run the Simulation

You must run both the Frontend and the Backend servers simultaneously to view the live simulation.

### 1. Start the React Frontend
Open a terminal in the root directory (`AegisSentinel`):
```bash
npm install
npm install lucide-react
npm run dev
```

### 2. Start the Python Backend
Open a second terminal, navigate to the `backend` directory, and start the FastAPI server:
```bash
cd backend
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Mac/Linux:
# source venv/bin/activate
pip install fastapi uvicorn websockets
uvicorn main:app --port 8000
```

Once both are running, open your browser to `http://localhost:5173` to watch the Aegis Sentinel actively intercept and neutralize simulated AI attacks.

## Core Philosophy: The Immune System

Most modern cybersecurity focuses on static defenses ("detect malware"). This system assumes AGI-level attackers already exist and will bypass static defenses instantly. 
Therefore, Aegis Sentinel uses:
- **Autonomous Consensus**: AI guarding against AI.
- **Continuous Validation**: Trust is mathematically proven on every packet.
- **Moving Target Architecture**: The underlying infrastructure constantly changes shape.

For a full breakdown of the defensive features, please read `FEATURES.md`.

### Email me on majipritam47@gmail.com For any enquiry
