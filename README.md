# 🚀 ASG Hourly CPU Monitoring & Owner Alerting

Cloud reality check ⚡
VMs eat 30–40% of cloud bills. Around 35% compute sits idle doing absolutely nothing.

Meanwhile… most workloads hide behind Auto Scaling Groups — EKS, ECS, node groups — everything.
Instances come and go. Watching individual VMs is basically chasing ghosts.

👉 So instead of watching instances… this project watches ASG behavior itself — where the real truth lives.

It scans AWS, understands ASGs, reads CPU patterns hour-by-hour, and quietly sends owners a clear picture of what their compute actually did in the last 24 hours.

---

## ⚙️ What This Script Does (Algorithm)

1. Looks across AWS like a radar and finds every active region.

2. Walks into each region and discovers every ASG hiding there.

3. Pulls identity details — size, capacity limits, creation time, and owner tags.

4. Asks CloudWatch: “what really happened every hour for the last 24h?”

5. If metrics disappear → marks No instances, not fake zeros.

6. If instances exist but sleep → shows honest 0% CPU.

7. Groups infrastructure by actual humans responsible for it.

8. Builds clean hourly timelines in IST so nobody does timezone math.

9. Generates simple HTML dashboards — one owner, only their ASGs.

10. Sends reports directly to inboxes without noise or drama.
