# 🚀 ASG Hourly CPU Monitoring & Owner Alerting

Cloud reality check ⚡ VMs consume 30–40% of cloud bills, yet ~35% of compute sits idle. Most workloads hide behind Auto Scaling Groups (EKS, ECS, node groups) where instances are ephemeral—chasing individual VMs is like chasing ghosts.

## The Problem
We cannot delete or modify instances without the owner's permission.  

## The Solution
Instead of taking blind action, this script monitors ASG behavior and sends precise hourly metrics to the exact owner who created that specific ASG, empowering them to optimize their own resources.

## ⚙️ How it Works (The Algorithm)

### Global Radar
Scans all active AWS regions to discover every ASG, pulling metadata like capacity limits and owner tags.

### True Ownership Routing
Unlike standard tools, it does not spam admins. It maps each specific ASG to the person responsible for it.

### Honest Metrics
It queries CloudWatch to differentiate between "Idle" (0% CPU) and "Empty" (No instances), ensuring data accuracy.

### No-Math Timeline
Automatically converts all data into a clean, hourly IST timeline to eliminate timezone confusion for the owners.

### Direct Delivery
Generates a custom HTML dashboard for each owner and sends it directly to their inbox via Amazon SES.




[📺 Video Demo](https://youtu.be/90AloMeLQe8)


