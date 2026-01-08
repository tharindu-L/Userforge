# 🔥 UserForge

UserForge is a **Python-based username wordlist generator** designed for **ethical hacking, penetration testing labs, and educational purposes**.  
It helps generate realistic username combinations using **names, roles, separators, and case variations**.

---

## ⚠️ Disclaimer

UserForge is intended **only for educational purposes and authorized security testing**.

❌ Do **NOT** use this tool on systems you do not own or do not have **explicit permission** to test.  
⚠️ The author is **not responsible for any misuse** of this tool.

---

## 📌 Features

- Generate username wordlists for login testing  
- Case variations (`admin`, `Admin`, `ADMIN`)  
- Custom separators (`_`, `.`, etc.)  
- CLI-based (easy to integrate with other tools)  
- Clean & colored banner  
- Lightweight and fast  

---

## 🛠️ Requirements

- Python **3.7 or higher**
- `pip`
- `git` (for cloning)

---

## 📥 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/tharindu-L/Userforge.git
```
### 2️⃣ Navigate into the project directory
```bash
cd Userforge
```
## 🚀 Usage
 - Run the tool using Python
```bash
python Userforge.py -n <names> -r <roles> [options]
```
## 📖 Command-Line Options
| Option               | Description                            |
| -------------------- | -------------------------------------- |
| `-n`, `--names`      | Names (comma-separated)                |
| `-r`, `--roles`      | Roles (comma-separated)                |
| `-s`, `--separators` | Separators (default: `_`, `.`)         |

## 🧪 Examples
```bash
python Userforge.py -n john,alice -r admin,administrator
```
## 📜 License
This project is licensed under the **MIT License**.
## ⭐ Support
If you find this tool useful, please ⭐ star the repository!
