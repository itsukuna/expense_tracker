import unittest
import os
from expense_tracker import add_expenses, update_expenses, delete_expenses, list_expenses, expense_summary, load_expenses, save_expenses

class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        """Set up a temporary expenses file for testing."""
        self.test_file = "test_expenses.json"
        global expenses_file
        expenses_file = self.test_file
        save_expenses([])

    def tearDown(self):
        """Clean up the temporary expenses file after testing."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_expenses(self):
        add_expenses("Test Expense", 100.0)
        expenses = load_expenses()
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0]["description"], "Test Expense")
        self.assertEqual(expenses[0]["amount"], 100.0)

    def test_update_expenses(self):
        add_expenses("Test Expense", 100.0)
        expenses = load_expenses()
        expense_id = expenses[0]["id"]
        update_expenses(expense_id, "Updated Expense", 150.0)
        expenses = load_expenses()
        self.assertEqual(expenses[0]["description"], "Updated Expense")
        self.assertEqual(expenses[0]["amount"], 150.0)

    def test_delete_expenses(self):
        add_expenses("Test Expense", 100.0)
        expenses = load_expenses()
        expense_id = expenses[0]["id"]
        delete_expenses(expense_id)
        expenses = load_expenses()
        self.assertEqual(len(expenses), 0)

    def test_list_expenses(self):
        add_expenses("Test Expense", 100.0)
        # Capture the output of list_expenses
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        list_expenses()
        sys.stdout = sys.__stdout__
        self.assertIn("Test Expense", captured_output.getvalue())

    def test_expense_summary(self):
        add_expenses("Test Expense", 100.0)
        # Capture the output of expense_summary
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        expense_summary()
        sys.stdout = sys.__stdout__
        self.assertIn("Total expenses is 100.0", captured_output.getvalue())

if __name__ == "__main__":
    unittest.main()
