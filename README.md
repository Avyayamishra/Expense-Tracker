# 💰 Expense Tracker CLI

> **Day 3 of 100** - Building a command-line expense tracking application
> 
> **Today's Learning**: Working with SQLite databases in Python, implementing CRUD operations, and creating user-friendly CLI interfaces with formatted table outputs using the tabulate library.

A lightweight and efficient command-line expense tracking application built with Python and SQLite. Track your daily expenses, view spending history, and manage your financial records—all from your terminal.

---

## ✨ Features

- **📝 Add Expenses** - Record expenses with description, amount, and date
- **👀 View All Records** - Display expenses in a beautifully formatted table
- **🗑️ Delete Entries** - Remove expenses by their unique ID
- **✏️ Update Records** - Modify existing expense details
- **💾 Persistent Storage** - SQLite database ensures your data is never lost
- **📅 Date Validation** - Ensures proper date format (YYYY-MM-DD)
- **🛡️ Error Handling** - Comprehensive error management for smooth operation

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/expense-tracker-cli.git
   cd expense-tracker-cli
   ```

2. **Install dependencies**
   ```bash
   pip install tabulate
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

---

## 📖 Usage Guide

Upon launching the application, you'll see a menu with four options:

### 1️⃣ Add Expense
Record a new expense with:
- **Description**: Brief description of the payment
- **Amount**: Expense amount (numeric value)
- **Date**: Date of expense in YYYY-MM-DD format

**Example:**
```
Description of the payment: Grocery Shopping
Enter amount: 2500
Enter date (YYYY-MM-DD): 2024-10-01
```

### 2️⃣ View Expenses
Displays all recorded expenses in a formatted table showing:
- Transaction ID
- Description
- Amount
- Expense Date
- Recorded Timestamp

### 3️⃣ Delete Expense
Remove an expense by entering its unique Transaction ID.

### 4️⃣ Update Expense
Modify an existing expense by entering its ID and providing new details.

---

## 🗄️ Database Schema

The application uses SQLite with the following structure:

```sql
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    amount REAL NOT NULL,
    expense_date TEXT NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

| Field | Type | Description |
|-------|------|-------------|
| `id` | INTEGER | Auto-incrementing primary key |
| `title` | TEXT | Description of the expense |
| `amount` | REAL | Expense amount |
| `expense_date` | TEXT | Date when expense occurred |
| `recorded_at` | TIMESTAMP | Auto-generated recording time |

---

## 📁 Project Structure

```
expense-tracker-cli/
│
├── main.py          # Main application file with all functionality
├── data.db          # SQLite database (auto-created on first run)
└── README.md        # Project documentation
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Core programming language |
| **SQLite3** | Lightweight embedded database |
| **Tabulate** | Beautiful table formatting |
| **Datetime** | Date validation and handling |

---

## 📸 Sample Output

```
Choose your option: 
[1] Add Expense
[2] View Expenses
[3] Delete Expense
[4] Update Expense
Enter your choice: 2

╒══════╤════════════════════╤══════════╤════════════════╤═══════════════════════╕
│   ID │ Title              │   Amount │ Expense Date   │ Recorded At           │
╞══════╪════════════════════╪══════════╪════════════════╪═══════════════════════╡
│    1 │ Grocery Shopping   │     2500 │ 2024-10-01     │ 2024-10-01 14:30:25   │
│    2 │ Electricity Bill   │     1200 │ 2024-09-28     │ 2024-10-01 14:32:10   │
│    3 │ Restaurant         │      850 │ 2024-10-01     │ 2024-10-01 18:45:33   │
╘══════╧════════════════════╧══════════╧════════════════╧═══════════════════════╛
```

---

## 🔮 Future Enhancements

- [ ] **Categories & Tags** - Organize expenses by categories (food, transport, utilities, etc.)
- [ ] **Budget Tracking** - Set monthly budgets and track spending against limits
- [ ] **Analytics & Reports** - Generate spending summaries and visualizations
- [ ] **Export Functionality** - Export data to CSV, Excel, or JSON formats
- [ ] **Search & Filter** - Search expenses by date range, amount, or description
- [ ] **Multi-currency Support** - Handle different currencies with conversion
- [ ] **Recurring Expenses** - Automatically log recurring payments
- [ ] **Data Backup** - Automated backup and restore functionality

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/Expense-Tracker`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/Expense-Tracker`)
5. Open a Pull Request

---

## 🐛 Known Issues

- Delete operation doesn't properly check if result is empty (uses `is None` instead of length check)
- Update operation doesn't validate date format
- No confirmation prompt before deletion

---

## 💡 Tips for Users

- Always use the YYYY-MM-DD format for dates
- Keep expense descriptions concise but informative
- Regularly back up your `data.db` file
- Use the view option frequently to track spending patterns

---

## 📧 Contact & Support

For questions, suggestions, or bug reports:
- Open an issue on GitHub
- Contact: avyayamishra1@gmail.com

---

<div align="center">

**Built with ❤️ using Python**

⭐ Star this repo if you find it helpful!

</div>
