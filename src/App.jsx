import React, { useState, useEffect, useRef } from 'react';
import { 
  ShieldAlert, 
  ShieldCheck, 
  Activity, 
  Network, 
  DatabaseZap,
  Fingerprint,
  Terminal,
  Cpu
} from 'lucide-react';
import './index.css';

const LogStream = ({ logs }) => {
  const endRef = useRef(null);
  
  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [logs]);

  return (
    <div className="log-stream">
      {logs.map((log, i) => (
        <div key={i} className="log-entry">
          <span className="log-time">[{log.time}]</span>
          <span className={`log-level-${log.level}`}>
            {log.level === 'crit' ? '[CRITICAL]' : log.level === 'warn' ? '[WARNING]' : '[INFO]'}
          </span>
          <span className="log-msg">{log.message}</span>
        </div>
      ))}
      <div ref={endRef} />
    </div>
  );
};

const TransactionCard = ({ tx }) => {
  return (
    <div className={`transaction-card status-${tx.status}`}>
      <div className="tx-header">
        <span className="tx-id">{tx.id}</span>
        <span className={`tx-amount ${tx.status === 'blocked' ? 'text-red' : tx.status === 'verified' ? 'text-green' : 'text-orange'}`}>
          ${parseFloat(tx.amount).toLocaleString()}
        </span>
      </div>
      <div className="tx-details">
        <div className="tx-detail-item">
          <span className="tx-detail-label">Origin</span>
          <span className="tx-detail-value">{tx.origin}</span>
        </div>
        <div className="tx-detail-item">
          <span className="tx-detail-label">Target</span>
          <span className="tx-detail-value">{tx.dest}</span>
        </div>
      </div>
      
      {tx.status === 'quarantine' && (
        <div className="analysis-track">
          <div className={`track-step ${tx.progress > 0 ? 'pass' : 'active'}`}></div>
          <div className={`track-step ${tx.progress > 1 ? 'pass' : (tx.progress === 1 ? 'active' : '')}`}></div>
          <div className={`track-step ${tx.progress > 2 ? 'pass' : (tx.progress === 2 ? 'active' : '')}`}></div>
        </div>
      )}
      
      {tx.status === 'blocked' && (
        <div className="text-red mono" style={{ fontSize: '0.7rem', marginTop: '5px', display: 'flex', alignItems: 'center', gap: '5px' }}>
          <ShieldAlert size={12} /> ALGORITHMIC BLOCK (CONSENSUS FAILED)
        </div>
      )}
    </div>
  );
};

export default function App() {
  const [transactions, setTransactions] = useState([]);
  const [logs, setLogs] = useState([]);
  const [metrics, setMetrics] = useState({
    scanned: 0,
    blocked: 0,
    activeAgents: 14052
  });
  
  const wsRef = useRef(null);
  
  const addLog = (message, level = 'info') => {
    setLogs(prev => [...prev.slice(-49), { time: new Date().toLocaleTimeString(), message, level }]);
  };

  const [topology, setTopology] = useState("STATIC");
  const [isSevered, setIsSevered] = useState(false);

  useEffect(() => {
    // Connect to Python Backend Algorithm Engine
    wsRef.current = new WebSocket('ws://localhost:8000/ws');
    
    wsRef.current.onopen = () => {
      addLog("WebSocket connected to Python Sentinel Backend. Engine Online.", "info");
    };

    wsRef.current.onmessage = (event) => {
      const msg = JSON.parse(event.data);
      
      if (msg.type === 'severance') {
          setIsSevered(true);
      }
      else if (msg.type === 'log') {
        addLog(msg.message, msg.level);
        if (msg.message.includes("Topology & Schema Mutation")) {
          setTopology(msg.message.match(/API (.*)/)[1]);
        }
      } 
      else if (msg.type === 'tx_update') {
        const updatedTx = msg.data;
        
        setTransactions(prev => {
          const exists = prev.find(t => t.id === updatedTx.id);
          if (exists) {
            return prev.map(t => t.id === updatedTx.id ? updatedTx : t);
          } else {
            setMetrics(m => ({ ...m, scanned: m.scanned + 1 }));
            return [updatedTx, ...prev].slice(0, 15);
          }
        });
        
        if (updatedTx.status === 'blocked' && updatedTx.progress === 3) {
            setMetrics(m => {
                return { ...m, blocked: m.blocked + 1 };
            });
        }
      }
    };
    
    wsRef.current.onclose = () => {
      addLog("Connection to backend lost.", "crit");
    };

    return () => {
      if (wsRef.current) {
        wsRef.current.close();
      }
    };
  }, []);

  if (isSevered) {
      return (
          <div style={{ height: '100vh', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', background: '#110000', color: '#ff2a4b', fontFamily: 'var(--font-mono)' }}>
              <ShieldAlert size={120} style={{ marginBottom: '20px', animation: 'pulse-bg 1s infinite alternate' }} />
              <h1 style={{ fontSize: '3rem', letterSpacing: '5px', textShadow: '0 0 20px #ff2a4b' }}>CORE SEVERANCE EXECUTED</h1>
              <p style={{ marginTop: '20px', fontSize: '1.2rem', color: '#fff', textAlign: 'center', maxWidth: '600px' }}>
                  DEAD MAN'S SWITCH TRIGGERED.<br/><br/>
                  Massive anomalous assault detected. The Aegis Sentinel has physically isolated the COBOL mainframe from the external network.<br/><br/>
                  MANUAL HARDWARE RESET REQUIRED.
              </p>
          </div>
      );
  }

  return (
    <>
      <header className="header">
        <h1><ShieldCheck size={28} color="var(--neon-blue)" /> AEGIS SENTINEL <span style={{fontSize: '1rem', color: 'var(--text-dim)'}}>| POST-AGI DEFENSE ARCHITECTURE</span></h1>
        <div style={{ display: 'flex', gap: '20px' }}>
          <div className="stat-item"><div className="indicator" style={{background: 'var(--neon-orange)', boxShadow: '0 0 8px var(--neon-orange)'}}></div> API PORT: {topology}</div>
          <div className="stat-item"><div className="indicator"></div> COBOL Core Protected</div>
        </div>
      </header>
      
      <main className="dashboard-grid">
        
        <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
          <div className="panel">
            <h2 className="section-title"><Network size={16} /> Distributed Guardian Swarms</h2>
            <div className="metrics-grid">
              <div className="metric-card">
                <div className="metric-value">{metrics.scanned.toLocaleString()}</div>
                <div className="metric-label">Packets Sequenced</div>
              </div>
              <div className="metric-card" style={{ borderColor: metrics.blocked > 0 ? 'rgba(255,42,75,0.4)' : ''}}>
                <div className="metric-value text-red">{metrics.blocked.toLocaleString()}</div>
                <div className="metric-label">Autonomous Blocks</div>
              </div>
              <div className="metric-card">
                <div className="metric-value">{(99.999).toFixed(3)}%</div>
                <div className="metric-label">Swarm Consensus</div>
              </div>
              <div className="metric-card">
                <div className="metric-value">{metrics.activeAgents.toLocaleString()}</div>
                <div className="metric-label">Micro-AIs Active</div>
              </div>
            </div>
            
            <h2 className="section-title"><Fingerprint size={16} /> Live DNA Behavior Analysis</h2>
            <div className="dna-chart">
              {Array.from({length: 40}).map((_, i) => {
                const height = Math.random() * 100 + 20;
                const isAnomaly = height > 105 && Math.random() > 0.5;
                return (
                  <div key={i} className={`dna-bar ${isAnomaly ? 'anomaly' : ''}`} style={{ height: `${height}px` }}></div>
                );
              })}
            </div>
          </div>
          
          <div className="panel">
            <h2 className="section-title"><Terminal size={16} /> Python Algorithmic Logs</h2>
            <LogStream logs={logs} />
          </div>
        </div>
        
        <div className="panel alert">
          <h2 className="section-title"><DatabaseZap size={16} /> Money Quarantine Layer</h2>
          <div className="text-dim" style={{fontSize: '0.8rem', marginBottom: '15px'}}>
            All incoming COBOL transactions are delayed in isolated memory cells for behavioral validation.
          </div>
          <div className="transaction-list">
            {transactions.map(tx => (
              <TransactionCard key={tx.id} tx={tx} />
            ))}
          </div>
        </div>
        
      </main>
      
      <footer className="footer-stats">
        <div>SYS: ONLINE</div>
        <div>ALGORITHM: FASTAPI PYTHON ENGINE</div>
        <div>ENCLAVE: HARDWARE LOCKED</div>
      </footer>
    </>
  );
}
