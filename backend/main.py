from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="GreenOps Telemetry API")

# Define request body
class Telemetry(BaseModel):
    vcpu_seconds: float
    memory_gb_seconds: float
    network_gb: float
    workload: str

@app.post("/telemetry")
def telemetry_endpoint(data: Telemetry):
    # Simple emission calculation (dummy values)
    emissions = data.vcpu_seconds * 0.5 + data.memory_gb_seconds * 0.2 + data.network_gb * 0.1
    return {"workload": data.workload, "estimated_co2_kg": emissions}
