import { useState } from "react";

function App() {
  const [logMessage, setLogMessage] = useState("");
  const [response, setResponse] = useState(null);
  const [logs, setLogs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [severityFilter, setSeverityFilter] = useState("ALL");

  // -------- Helpers --------
  const severityColor = (level, anomaly) => {
    if (anomaly) return "bg-red-200 border-red-400";
    if (level === "ERROR" || level === "CRITICAL")
      return "bg-orange-100 border-orange-300";
    if (level === "WARNING") return "bg-yellow-100 border-yellow-300";
    return "bg-green-100 border-green-300";
  };

  // -------- API calls --------
  const analyzeLog = async () => {
    if (!logMessage) return;

    setLoading(true);

    // Send log
    await fetch("http://backend:8000/logs", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        timestamp: new Date().toISOString(),
        level: "ERROR",
        service: "frontend-ui",
        message: logMessage,
      }),
    });

    // Analyze
    const res = await fetch("http://backend:8000/analyze", {
      method: "POST",
    });

    const data = await res.json();
    setResponse(data);
    setLogMessage("");

    await fetchLogs();
    setLoading(false);
  };

  const fetchLogs = async () => {
    const res = await fetch("http://backend:8000/logs");
    const data = await res.json();
    setLogs(data.logs);
  };

  // -------- Filtered logs --------
  const displayedLogs = logs.filter(
    (log) => severityFilter === "ALL" || log.level === severityFilter
  );

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-4xl mx-auto bg-white p-6 rounded shadow">
        <h1 className="text-2xl font-bold mb-6">
          AI Log Intelligence Dashboard
        </h1>

        {/* Input */}
        <textarea
          className="w-full border p-3 mb-4 rounded"
          rows="3"
          placeholder="Paste application log here..."
          value={logMessage}
          onChange={(e) => setLogMessage(e.target.value)}
        />

        <button
          className="bg-blue-600 text-white px-4 py-2 rounded mb-6"
          onClick={analyzeLog}
          disabled={loading}
        >
          {loading ? "Analyzing..." : "Analyze Log"}
        </button>

        {/* Analysis Summary */}
        {response && (
          <div className="mb-8">
            <p className="font-semibold">
              Anomalies Detected:{" "}
              <span className="text-red-600">
                {response.anomalies_detected}
              </span>
            </p>

            <h3 className="mt-4 font-semibold">Root Cause Explanation</h3>
            <pre className="bg-gray-200 p-3 text-sm rounded mt-2 whitespace-pre-wrap">
              {response.root_cause_analysis}
            </pre>
          </div>
        )}

        {/* Filters */}
        <div className="flex items-center gap-4 mb-4">
          <span className="font-semibold">Filter by severity:</span>
          <select
            className="border p-2 rounded"
            value={severityFilter}
            onChange={(e) => setSeverityFilter(e.target.value)}
          >
            <option value="ALL">ALL</option>
            <option value="INFO">INFO</option>
            <option value="WARNING">WARNING</option>
            <option value="ERROR">ERROR</option>
            <option value="CRITICAL">CRITICAL</option>
          </select>
        </div>

        {/* Logs Table */}
        <h3 className="font-semibold mb-2">Stored Logs</h3>
        <div className="space-y-2 text-sm">
          {displayedLogs.map((log, idx) => {
            const anomaly =
              response?.results?.find((r) => r.message === log.message)
                ?.anomaly || false;

            return (
              <div
                key={idx}
                className={`border p-3 rounded ${severityColor(
                  log.level,
                  anomaly
                )}`}
              >
                <div className="flex justify-between text-xs text-gray-600">
                  <span>{new Date(log.timestamp).toLocaleString()}</span>
                  <span className="font-semibold">{log.level}</span>
                </div>

                <p className="mt-1">{log.message}</p>

                {anomaly && (
                  <p className="text-red-700 text-xs mt-1 font-semibold">
                    ⚠ Anomalous log — explained above
                  </p>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

export default App;
