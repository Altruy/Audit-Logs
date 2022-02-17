# Audit-Logs

When one observes Auditd logs while fuzzing a linux guest machine with Syzkaller, you can see descripencies between both the logs. 

This project contains multiple approaches to confirm and corroborate the losses, isolate and identify the circumstances surrouning the descripency.

We make use of tracing and stressing tools like ftrace, perf, stress / stress-ng tools in a fully linux-qemu (host and guest) environment. 

#### This Repo contains
- The scripts and codes we wrote to gather, clean and analyse data
- The post-processed and semi-processed logs
