# 🚀 ASG Hourly CPU Monitoring & Owner Alerting

VMs are nearly 30–40% of total cloud bills, and studies often show ~35% compute is wasted across companies.  
Today most workloads run behind Auto Scaling Groups (ASG) — whether via EKS node groups, ECS capacity providers, or traditional autoscaling. Instances are ephemeral by design, so monitoring individual instances is unreliable.

👉 The correct approach is to monitor ASG-level compute behavior.  
This script automates ASG CPU monitoring and sends owner-specific hourly utilization reports.

---

## ⚙️ What This Script Does (Algorithm)

1. Scans AWS globally and quietly builds a live map of every region.  
2. Hunts down ASGs and extracts their identity, capacity DNA, and ownership clues from tags.  
3. Pulls 24-hour CPU signals from CloudWatch and reshapes them into hourly intelligence.  
4. Detects silence in metrics and translates gaps into “No instances” or true idle `0%`.  
5. Filters out broken or suspicious ASGs before they contaminate reports.  
6. Clusters infrastructure by real human owners using tag intelligence.  
7. Converts raw telemetry into clean IST-based hourly timelines with context.  
8. Crafts structured HTML dashboards and delivers personalized reports straight to inboxes.
