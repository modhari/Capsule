# Capsule Design Document

## 1. Overview

Capsule is a multivendor network and host observability system designed around capability driven telemetry collection using gRPC gNMI and OpenConfig models.

The system is built incrementally. Each layer is introduced with unit tests and extended over time. The design favors clarity, composability, and separation of concerns over premature optimization.

Capsule focuses on:

• Structured telemetry collection  
• Vendor abstraction  
• Baseline driven anomaly detection  
• Safe AI assisted investigation  

Capsule does not perform direct device modification. Observability and reasoning precede automation.

---

## 2. Design Principles

### 2.1 OpenConfig First

OpenConfig models are preferred wherever supported by the device. This ensures:

• Cross vendor consistency  
• Reduced schema duplication  
• Easier normalization  

Vendor specific models are used only when required.

---

### 2.2 Capability Driven Behavior

Devices are not assumed to support specific telemetry paths.

Instead:

1. Capabilities are discovered via gNMI
2. A capability profile is constructed
3. Vendor packs generate sensor groups based on supported models

This prevents rigid, hardcoded telemetry assumptions.

---

### 2.3 Incremental Growth

Capsule evolves gradually:

• One vendor at a time  
• One protocol at a time  
• One monitoring feature at a time  

Each capability is introduced with unit tests before expansion.

---

### 2.4 Observability Before Automation

Capsule is designed as an investigative system.

AI components provide reasoning and explanation but do not execute changes directly. Any future automation would be explicitly gated and auditable.

---

## 3. Core Components

### 3.1 Core Layer

Responsibilities:

• Device identity modeling  
• Capability profiles  
• Baseline tracking  
• Anomaly detection  
• Alert generation  

The baseline engine uses rolling windows and statistical deviation. Flat baselines are handled via standard deviation flooring to avoid detection dead zones.

---

### 3.2 gNMI Layer

Responsibilities:

• Path abstraction  
• Capability discovery  
• Client interface  
• Subscription orchestration  

The gNMI layer is abstracted so that unit tests can use a fake client implementation.

---

### 3.3 Vendor Packs

Each vendor pack defines:

• Matching logic based on device identity  
• Sensor groups  
• Sampling intervals  
• Preferred OpenConfig paths  
• Vendor native fallbacks  

This isolates vendor specific differences from the rest of the system.

Current vendors:

• Arista  
• Cisco  
• Juniper  
• Nokia  

---

### 3.4 Host Telemetry

Host collectors gather:

• CPU load  
• Memory  
• TCP retransmissions  
• Disk metrics  

Host and network signals can later be correlated.

---

### 3.5 AI and MCP Layer

Capsule includes:

• A planning agent  
• A retrieval augmented document store  
• A structured MCP tool interface  

The agent can:

• Select relevant telemetry groups  
• Retrieve documentation  
• Query structured metrics  
• Provide reasoned explanations  

The MCP layer ensures all tool calls are explicit and auditable.

---

## 4. Data Flow

Device or Host
        |
        v
Telemetry Collection
        |
        v
Normalization
        |
        v
Baseline Tracking
        |
        v
Anomaly Detection
        |
        v
Alert Generation
        |
        v
AI Reasoning and Explanation

---

## 5. Future Design Evolution

Near term:

• Interface counters  
• BGP session monitoring  
• Protocol specific anomaly detection  

Long term:

• EVPN and VXLAN awareness  
• MPLS monitoring  
• Topology correlation  
• Cross signal correlation  
• Structured investigation workflows  

Capsule is designed so these capabilities can be added without refactoring core abstractions.
