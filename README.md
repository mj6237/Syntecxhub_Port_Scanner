# 🛡️ Advanced TCP Port Scanner

## 📌 Project Overview

This project is part of my **Week 1 Task** for the **SYNTECXHUB Virtual Internship Program**. The objective was to build a robust tool that identifies open ports on a target host, providing essential network reconnaissance capabilities.

Through this project, I implemented core concepts of **Socket Programming**, **Multi-threading**, and **Log Management**.

## ✨ Key Features

* **High-Speed Scanning:** Utilizes Python's `threading` library to scan multiple ports concurrently, significantly reducing execution time.
* **Flexible Input:** Supports scanning for a single host and allows users to define a specific range of ports.
* **Automated Logging:** Saves all scan results (open/closed ports) into a `scan_results.txt` file for future reference.
* **Exception Handling:** Gracefully handles network timeouts, invalid hostnames, and connection errors.
* **Performance Metrics:** Calculates and displays the total duration of the scan upon completion.

## 🛠️ Technical Stack

* **Language:** Python 3.x
* **Core Modules:** `socket` (Networking), `threading` (Concurrency), `datetime` (Time Tracking).

## 🚀 How to Run

1. **Clone the Repository:**
```bash
git clone https://github.com/YOUR_USERNAME/Syntecxhub_Port_Scanner.git

```


2. **Navigate to Directory:**
```bash
cd Syntecxhub_Port_Scanner

```


3. **Execute the Script:**
```bash
python main.py

```



## 📊 Sample Output

```text
--------------------------------------------------
Scanning Target: 127.0.0.1
Time Started: 2026-02-18 10:00:00
--------------------------------------------------
[+] Port 80 is OPEN
[+] Port 443 is OPEN
--------------------------------------------------
Scan Complete!
Total Time Taken: 0:00:02.45
Results saved in scan_results.txt
--------------------------------------------------

```

## 📜 Internship Context

* 
**Organization:** SYNTECXHUB 


* 
**Domain:** Cybersecurity 


* 
**Duration:** 1 Month 


* 
**Mode:** Remote 



---

**Developed by Muhammad Jamshaid**
*Connect with me on [LinkedIn*](https://www.linkedin.com/in/muhammad-jamshaid-a04054370/)

---
