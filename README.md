# 🔐 Secure File Access with PIN  

A simple **Python-based security tool** that allows users to set a **4-digit PIN** to protect a text file (`file_3.txt`). Users must enter the correct PIN to access the file's content.  

---

## 🌟 Features  
✅ **Set and Save PIN**: Users set a **4-digit PIN**, which is securely stored in `pin_file.txt`.  
✅ **PIN Verification**: Users must enter the correct PIN to access the protected file.  
✅ **Secure File Access**: Prevents unauthorized access.  
✅ **Input Validation**: Ensures only numeric **4-digit PINs** are accepted.  
✅ **Error Handling**: Prevents crashes if the file doesn't exist.  

---

## 📌 Installation & Setup  
### **🔧 Prerequisites**  
Ensure you have **Python 3.x** installed. If not, download it from:  
🔗 [Python Official Website](https://www.python.org/downloads/)  

### **📥 Install Required Libraries**  
This project only uses built-in Python functions, so **no additional pip installations** are required! 🎉  

---

## 🚀 How to Use  
### **1️⃣ Clone the Repository**  
Open your terminal or command prompt and run:  
```bash
git clone https://github.com/AREEB-08/SecureFileAccess.git
cd SecureFileAccess
```

### **2️⃣ Run the Script**  
Start the program by running:  
```bash
python main.py
```

### **3️⃣ Set Your PIN**  
- Enter a **4-digit PIN** (e.g., `1234`).  
- The PIN will be **saved** in `pin_file.txt` for verification.  

### **4️⃣ Access the Protected File**  
- Enter the correct **4-digit PIN** when prompted.  
- If the PIN matches, you can view the contents of `file_3.txt`.  
- If the PIN is incorrect, access is **denied**.  

---

## 📂 Project Structure  
```
SecureFileAccess/
│── main.py              # Main script
│── pin_file.txt         # Stores the saved PIN
│── file_3.txt           # The protected file (must exist)
│── README.md            # Project documentation
```

---

## ❗ Important Notes  
🔹 The **PIN is stored in plain text** (`pin_file.txt`). In a real-world application, **encryption** should be used.  
🔹 Ensure `file_3.txt` exists; otherwise, an error will occur.  
🔹 The program currently supports **only numeric 4-digit PINs**.  

---
