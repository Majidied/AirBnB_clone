#!/usr/bin/python3
"""Module for testing the HBNBcommand Class"""
from unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO

class Test_Console(unittest.TestCase):
    """Test the HBNBCommand Console"""

    def test_help(self):
        """Test the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        s = """ 
        Documented commands (type help <topic>):
        ========================================
        EOF all count create destroy help quit show update\n
        """
        self.asserEqual(s, f.getvalue())
        
    def test_do_quit(self):
        """Tests the qui command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)
        
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit garbage")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)
        
    def test_do_EOF(self):
        """Tests the EOF command"""
        
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("\n", msg)
        
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF garbage")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("\n", msg)
        
    def test_do_emptyline(self):
        """Tests the emptyline command"""
        
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)
        
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("                     \n")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)
    def test_do_all(self):
        """Tests the do_all command"""
        
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")

if __name__ == "__main__":
    unittest.main()
