# Socket Connection Auditor 

**Socket Connection Auditor** is a real-time monitoring tool designed for Linux systems. The project enables the auditing of active network connections directly from the operating system's kernel, linking each port with its corresponding process name and PID through a modern and professional web interface.

---

## Authors
*   **Laura Eraso** - [GitHub Profile](https://github.com/laueralor)
*   **[Alejandro Bolivar]** - [GitHub Profile](https://github.com/Bolivaar16)

---

## Technologies Used
*   **Backend:** Python 3, Django Framework.
*   **Frontend:** HTML5, CSS3 (Bootstrap 5), JavaScript.
*   **OS Integration:** Linux `ss` utility and Python `subprocess` module.
*   **Processing:** Regular Expressions (Regex) for structured data parsing.

---

## GitHub repository: 
[https://github.com/laueralor/socket-connection-auditor.git](https://github.com/laueralor/socket-connection-auditor.git)

---

### How to Run
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

