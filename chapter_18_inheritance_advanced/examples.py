"""
Chapter 18: Inheritance (Advanced)
Examples demonstrating Multiple Inheritance, MRO, and Abstract Base Classes.
"""
from abc import ABC, abstractmethod

# --- Abstract Base Classes ---

class Document(ABC):
    """An abstract base class. You cannot instantiate Document()."""
    
    @abstractmethod
    def read(self) -> str:
        """Any child class MUST implement this method."""
        pass

class PDFDocument(Document):
    def read(self) -> str:
        return "Reading PDF bytes..."

# --- Multiple Inheritance ---

class LoggerMixin:
    """A mixin providing logging capability."""
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")

class DatabaseNode:
    """A primary base class."""
    def connect(self) -> str:
        return "Connected to database."

class AuditedDatabaseNode(DatabaseNode, LoggerMixin):
    """
    Inherits primary identity from DatabaseNode, 
    but acquires behavior from LoggerMixin.
    """
    def secure_connect(self) -> None:
        self.log("Attempting secure connection...")
        print(self.connect())
        self.log("Secure connection established.")

def main():
    print("--- Abstract Base Classes ---")
    try:
        doc = Document() # This will raise a TypeError
    except TypeError as e:
        print(f"Expected Error: {e}")
        
    pdf = PDFDocument()
    print(pdf.read())
    
    print("\n--- Multiple Inheritance & Mixins ---")
    node = AuditedDatabaseNode()
    node.secure_connect()
    
    print("\n--- Method Resolution Order (MRO) ---")
    # Shows the path Python takes to find methods
    for cls in AuditedDatabaseNode.__mro__:
        print(cls.__name__)

if __name__ == "__main__":
    main()
