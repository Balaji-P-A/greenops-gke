# GreenOps — MVP Project Brief

**Objective**
Build an MVP "GreenOps Dashboard" that measures and displays CO₂e impact of GKE workloads, exposes a custom metric to Cloud Monitoring, and demonstrates autoscaling driven by that metric.

**MVP scope (minimum to demo)**
- Collect per-request telemetry from one sample service (simple HTTP API).
- Backend service that converts telemetry → CO₂e estimate and writes a Cloud Monitoring custom metric `custom.googleapis.com/greenops/emissions_per_request`.
- Show the metric in a minimal dashboard (web UI) and in Metrics Explorer.
- Deploy the Custom Metrics adapter so HPA can consume the metric.
- HPA configured to scale based on the carbon metric; show an autoscaling demo (load test).

**Success criteria / Definition of Done**
- Telemetry endpoint accepts sample telemetry and writes a custom metric (verify in Metrics Explorer).
- Dashboard displays per-workload CO₂e (kg) and a "total today" counter.
- HPA uses the custom metric, and we can trigger a scale event visible in `kubectl describe hpa`.
- A short demo script (≤4 steps) clearly shows metric → HPA reaction → dashboard update.

**Must-have tech choices (MVP)**
- GKE Autopilot cluster
- Backend: FastAPI (Python) or Go
- Dashboard: React (Vite)
- Custom metrics → Cloud Monitoring (no node DaemonSets)
- CI: GitHub Actions (build/push image to Artifact Registry)

**Risks & constraints**
- Autopilot limits privileged containers / DaemonSets — design with Cloud Monitoring + app instrumentation.
- Cost: use small test quotas + set a billing budget/alert.
- Metric latency: Cloud Monitoring may be a few seconds/minutes delayed — test and plan demo accordingly.

**First 3 deliverables**
1. Repo + README (this doc).
2. Backend skeleton + Dockerfile, local telemetry test that writes a metric.
3. Deployment manifest + custom metrics adapter + HPA (show scaling / debugging steps).

