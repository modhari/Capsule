# Capsule Architecture

## 1. High Level Architecture

                    +----------------------+
                    |   Operator Interface |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |       AI Agent       |
                    |  Plan and Reason     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |      MCP Server      |
                    | Structured Tools     |
                    +----------+-----------+
                               |
                               v
+------------------------------+----------------------------------+
|                           Capsule Core                          |
|                                                                  |
|  Capability Discovery | Baseline Engine | Alert Engine | Store  |
+-----------+------------------+----------------+------------------+
            |                  |
            v                  v
     +-------------+     +-------------+
     |  gNMI Layer |     | Host Layer  |
     |  get stream |     | cpu ram tcp |
     +------+------+     +------+------+
            |                   |
            v                   v
   +----------------+     +----------------+
   | Network Devices|     | Linux Hosts    |
   | Cisco Juniper  |     | Bare metal VM  |
   | Nokia Arista   |     +----------------+
   +----------------+
