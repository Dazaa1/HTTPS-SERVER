# 🔒 Simple HTTPS File Server in Python

This project is a minimal Python server that serves files securely over **HTTPS** using Python's built-in modules: `http.server`, `socketserver`, and `ssl`.

It's a great starting point for learning how secure servers work and how to serve static files over encrypted connections.

---

## 🚀 Features

- Serves files over **HTTPS**
- Uses a self-signed SSL certificate
- Built entirely with Python's standard library
- Clean and minimal setup (under 30 lines of code!)

---

## 🧠 Requirements

- Python 3.x
- SSL certificate and private key (e.g., `cert.pem` and `domain.key`)

---

## ⚙️ How to Run

1. **Generate a self-signed certificate** (if you don’t already have one):

   ```bash
   openssl req -new -x509 -keyout domain.key -out cert.pem -days 365 -nodes
    ```
2. **Run the server**
   ```bash
    python3 server.py
    ```

3. **Open your browser and go to:**
   ```
   https://localhost:5678
   ```
- You may see a security warning — this is normal for self-signed certificates. Click “Advanced” → “Proceed to localhost”.

## 📂 Folder Structure
```
├── README.md
├── cert.pem
├── domain.csr
├── domain.key
├── index.html
├── notes.md
└── src
    └── server.py
```

## 🛑 Disclaimer

This server is for learning and testing purposes only.
Do not use it in production — it's not optimized or secure enough for public deployment.

## ✍️ Author

A personal learning project to understand how HTTPS works in Python.

Feel free to fork or contribute!