# Socket Connection Auditor

Real-time network monitoring and auditing tool designed for **Linux** environments. The platform inspects active network connections directly at the operating system's kernel level, associating each open port and socket with its corresponding process name and PID through an interactive web dashboard.

---

## Technical Contributions (Laura Eraso Lorenzo)

* **Backend & OS Integration:** Developed the core **Django** backend and integrated the Linux networking subsystem using Python's `subprocess` module and system utilities (`ss`).
* **Data Parsing & Processing:** Engineered optimized Regular Expressions (**Regex**) to parse, sanitize, and structure low-level socket data in real time.
* **Monitoring Interface:** Designed dynamic views and structured templates for real-time network metric visualization.

---

## Tech Stack

* **Backend:** Python 3.x, Django Framework
* **OS / Kernel Integration:** Linux Network Stack, `ss` utility, `subprocess`
* **Data Parsing:** Regular Expressions (Regex)
* **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript

---

## Key Features

* **Real-Time Kernel Auditing:** Direct extraction of open ports, active TCP/UDP connections, and listening states.
* **Process Mapping:** Automated mapping between low-level network sockets, system PIDs, and process names.
* **Lightweight Dashboard:** Clean web interface built with Bootstrap 5 tailored for system administration and security auditing workflows.

---

## Installation & Local Setup

> **Note:** Requires a Linux-based environment to inspect low-level socket connections.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/laueralor/socket-connection-auditor.git](https://github.com/laueralor/socket-connection-auditor.git)
   cd socket-connection-auditor
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations and run the server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
   Access the dashboard at `http://127.0.0.1:8000/`.

---

## Development Team (Erasmus)

* **Laura Eraso Lorenzo** ([@laueralor](https://github.com/laueralor))
* **Alejandro Bolívar Corpas** ([@Bolivaar16](https://github.com/Bolivaar16))
