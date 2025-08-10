# 📇 Contact Book (Python)

A simple **command-line contact book** written in Python.  
You can add, view, search, and delete contacts — all from your terminal.

---

## 🚀 Features
- ➕ **Add a Contact** — Save a name and phone number.
- 📜 **Show All Contacts** — View all saved contacts.
- 🔍 **Search** — Look up a contact by name.
- 🗑 **Delete** — Remove a contact from the list.
- ❌ **Quit** — Exit the program.

---

## 🛠 How It Works
The program stores all contacts in a Python dictionary:
- **Keys** → Contact names (saved in lowercase to avoid duplicates)
- **Values** → Phone numbers

---

## 📂 File Structure
```
📦 contact-book
 ┣ 📜 contact_book.py
 ┗ 📜 README.md
```

---

## 💻 Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/contact-book.git
cd contact-book
```

### 2️⃣ Run the program
```bash
python contact_book.py
```

---

## 📋 Example Output
```
<--- Contact Details --->
<--- press 1 to add a contact --->
<--- press 2 to show all contacts --->
<--- press 3 to search for a contact --->
<--- press 4 to delete a contact --->
<--- press 5 to Quit --->
choose a number: 1
name: john
phone number: 123456789
added successfully.
```

---

## 📝 Notes
- All names are stored in **lowercase** for easier searching.
- The contacts are stored **in-memory only** — closing the program will erase them.
- You can enhance it by saving contacts to a file for persistence.

---

## 📜 License
This project is licensed under the MIT License.
