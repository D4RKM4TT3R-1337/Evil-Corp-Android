# Evil-Corp-Android

# NOTE!

This repository provides an **educational phishing simulation toolkit** designed for security awareness training, authorized red team exercises, and defensive cybersecurity learning. The tool is **not intended for malicious use** or targeting real-world users, and it is explicitly designed for controlled, ethical environments where users have permission to conduct testing. It leverages **Cloudflare Argo Tunnels** to create ephemeral URLs, ensuring that all phishing simulations are temporary and automatically terminated when the process is stopped using `CTRL+C`. No persistent endpoints or background data collection occur, and all URLs disappear immediately after shutdown, making it a safe and contained platform for learning and experimentation.

The primary goal of this project is to provide **hands-on experience with phishing techniques** in a way that helps defenders understand attacker workflows, recognize social engineering tactics, and develop more effective detection and response strategies. By simulating common phishing scenarios in a controlled lab environment, security teams, educators, and students can explore the mechanics of phishing without exposing real users to risk. The repository comes with an **MIT License**, but it is accompanied by an ethical usage disclaimer emphasizing that unauthorized phishing, impersonation, or credential harvesting is illegal and strictly prohibited. Users are fully responsible for ensuring that their activities comply with applicable laws and organizational policies.

This toolkit is suitable for use in cybersecurity training labs, penetration testing exercises with written authorization, and awareness campaigns where participants can safely explore the methodology behind phishing attacks. By combining ephemeral tunnels, ethical guidance, and educational intent, this repository serves as a **practical, low-risk resource** for anyone seeking to deepen their understanding of phishing threats and defensive strategies, all while maintaining a strong focus on legal and responsible use.

- [x] Supported Architecture : ARM64 ONLY
- [x] Supported Operating System : Android, Termux

---

## Usage Example

```bash
# Start the phishing simulation (ephemeral URL)
python3 main.py

# View Available Commands
evilcorp >> help
```

---

## INSTALLATION

```bash

git clone https://github.com/D4RKM4TT3R-1337/Evil-Corp-Android
cd Evil-Corp-Android
bash setup.sh
python3 main.py
```
