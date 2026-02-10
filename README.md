Capsule

Capsule is an evolving multivendor network and host observability system focused on gRPC gNMI telemetry, OpenConfig modeling, and progressive monitoring capabilities.

The project is built incrementally, starting from basic capability discovery and telemetry collection, and expanding toward protocol aware monitoring, alerting, and AI assisted analysis.

Motivation

Modern data center networks expose rich telemetry through gRPC gNMI and standardized models, but most tooling still treats devices as static metric sources.

Capsule is built around the idea that observability should be capability driven. Devices are discovered, understood, and monitored based on what they actually support, rather than forcing a fixed schema everywhere.

The long term goal is to combine structured telemetry with reasoning and context, so operators can move from raw signals to explanations.

Design principles
	1.	OpenConfig first
OpenConfig models are used wherever available to ensure consistency across vendors.
	2.	Vendor specific where necessary
When OpenConfig coverage is incomplete, vendor native models are used and normalized.
	3.	Capability driven behavior
Devices advertise what they support. Collection plans are derived from capabilities, not assumptions.
	4.	Incremental development
Features are added one at a time, with unit tests from the beginning.
	5.	Observability before automation
The system focuses on collection, monitoring, and analysis. Any future actions are explicitly gated.

Current capabilities

As of the current stage, Capsule includes:
	1.	Core identity and capability modeling for network devices
	2.	gNMI path abstractions and a test friendly fake gNMI client
	3.	Capability discovery with OpenConfig detection
	4.	Baseline tracking for metrics using rolling windows
	5.	Simple anomaly detection using statistical deviation
	6.	Alert generation built on top of baseline behavior
	7.	Initial OpenConfig system telemetry support
	8.	A first vendor pack using Arista as the starting point

All functionality is covered by unit tests from the first commit onward.

Architecture overview

Capsule is structured into clear layers:

Core
Foundational types, baseline tracking, alerting, and shared utilities.

gNMI
Path definitions, capability discovery, and client abstractions.

Vendors
Per vendor mapping packs that define sensor groups and telemetry paths.

Host
Host level telemetry collectors for system and TCP level signals.

RAG
Document storage and retrieval used to support reasoning and explanation.

MCP
A tool interface layer that exposes structured read only capabilities to an agent.

Agent
A planning and reasoning layer that selects telemetry based on investigation intent.

Each layer can evolve independently without forcing changes across the system.

Why tests exist from day one

Capsule is intentionally built test first.

Every capability is introduced alongside a unit test that defines its expected behavior. This makes the commit history readable and shows how the system evolves over time.

Tests are fast, deterministic, and do not require real network devices.

Example use cases
	1.	Discover what telemetry a device supports before collecting anything
	2.	Track system health metrics and detect abnormal behavior
	3.	Gradually add protocol awareness such as BGP or EVPN without redesign
	4.	Provide structured telemetry access to an AI reasoning layer
	5.	Build operator facing explanations instead of raw metric dumps

Project status

Capsule is under active development.

The focus is currently on:
	1.	Expanding protocol level telemetry coverage
	2.	Adding more vendor packs
	3.	Improving correlation between metrics and events
	4.	Growing the AI assisted investigation layer

Stability and correctness are prioritized over feature count.

Roadmap outline

Near term goals include:
	1.	Interface and traffic counter telemetry
	2.	BGP session and prefix monitoring
	3.	Host TCP and system level correlation
	4.	Vendor registry and selection logic
	5.	MCP tool expansion for structured queries

Longer term goals include:
	1.	EVPN and VXLAN observability
	2.	MPLS and transport monitoring
	3.	Topology awareness and correlation
	4.	Rich AI assisted investigation workflows

Philosophy

Capsule is not meant to be a monolithic platform.

It is a composable system that grows as understanding grows. The codebase is designed to reflect real engineering progress, not a finished product snapshot.
