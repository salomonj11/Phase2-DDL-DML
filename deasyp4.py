from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, Numeric, Float, Date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
import datetime  # Missing import for datetime (added here)

# DB Connection: create_engine(DBMS_name+driver://<username>:<password>@<hostname>/<database_name>)
engine = create_engine("postgresql+psycopg2://postgres:Comp453@localhost/postgres")

# Define Classes/Tables
class Base(DeclarativeBase):  # Correct usage for SQLAlchemy 2.0
    pass

# Supplier Table
class Item(Base):
    __tablename__ = "Item"

    ItemID: Mapped[int] = mapped_column(Integer, primary_key=True)
    ItemName: Mapped[str] = mapped_column(String(100), nullable=False)
    CurrentPrice: Mapped[float] = mapped_column(Numeric(10, 2))
    PurchasePrice: Mapped[float] = mapped_column(Numeric(10, 2))
    Currency: Mapped[str] = mapped_column(String(3), default="USD")
    ExpirationDate: Mapped[Date] = mapped_column(Date)
    Unit: Mapped[str] = mapped_column(String(100))
    Quantity: Mapped[float] = mapped_column(Float)

    # 1-N relationship with Log table (circular reference issue here)
    # FIX: This is referencing the same table ('Item') instead of the 'Log' table.
    InventoryHistoryLogID: Mapped[int] = mapped_column(Integer, ForeignKey("Log.InventoryHistoryLogID"))  # Fix FK column
    InventoryHistoryLog: Mapped["Log"] = relationship("Log", back_populates="items")  # Fix relationship to 'Log'

    def __repr__(self) -> str:
        # FIX: Incorrect usage of non existent attributes in the __repr__. Remove or correct.
        return f"Item(ItemID={self.ItemID}, ItemName={self.ItemName})"


# Item Table
class Log(Base):  # FIX: Rename this table consistently; avoid spaces in table names
    __tablename__ = "Inventory History Log"  # FIX: Spaces in table names are problematic. Use snake_case.

    InventoryHistoryLogID: Mapped[int] = mapped_column(Integer, primary_key=True)
    ChangeDate: Mapped[Date] = mapped_column(Date, nullable=False)
    ChangeType: Mapped[str] = mapped_column(String(100))
    Reason: Mapped[str] = mapped_column(String(100))
    User: Mapped[str] = mapped_column(String(100))

    # FIX: Redundant column definition. Remove one of the InventoryHistoryLogID definitions.
    # InventoryHistoryLogID: Mapped[int] = mapped_column(Integer, ForeignKey("Item.ItemID"))

    items: Mapped[List["Item"]] = relationship("Item", back_populates="InventoryHistoryLog")  # Corrected relationship

    def __repr__(self) -> str:
        # FIX: Incorrect usage of non-existent attributes in __repr__. Remove or correct.
        return f"Log(InventoryHistoryLogID={self.InventoryHistoryLogID}, ChangeDate={self.ChangeDate})"

# Create Tables
Base.metadata.create_all(engine)

# Insert Data
with Session(engine) as session:
    # Logs
    # FIX: Log objects are referenced before they are defined in the Items section below.
    # Create these first, then reference them in Items.
    log1 = Log(ChangeDate=datetime.date(2023, 10, 17), ChangeType="Removal", Reason="Updated Quantity", User="John Doe")
    log2 = Log(ChangeDate=datetime.date(2023, 10, 18), ChangeType="Correction", Reason="Corrected Quantity", User="Jack Doe")
    log3 = Log(ChangeDate=datetime.date(2023, 10, 19), ChangeType="Removal", Reason="Shrinkage", User="Jill Doe")

    # Items
    # FIX: Dates like "2025-12-31" should be converted to datetime.date objects.
    item1 = Item(ItemName="Queen Butter", CurrentPrice=5.99, PurchasePrice=4.99, ExpirationDate=datetime.date(2025, 12, 31), Unit="Can", Quantity=100, InventoryHistoryLog=log1)
    item2 = Item(ItemName="Angus Beef Stew", CurrentPrice=10.99, PurchasePrice=8.99, ExpirationDate=datetime.date(2025, 6, 30), Unit="Pack", Quantity=80, InventoryHistoryLog=log1)
    item3 = Item(ItemName="ABC Frozen Salmon", CurrentPrice=15.99, PurchasePrice=17.99, ExpirationDate=datetime.date(2025, 10, 31), Unit="Pack", Quantity=200, InventoryHistoryLog=log1)
    item4 = Item(ItemName="DEF Pepperoni", CurrentPrice=2.99, PurchasePrice=2.89, ExpirationDate=datetime.date(2025, 4, 15), Unit="Pack", Quantity=80, InventoryHistoryLog=log1)
    item5 = Item(ItemName="I20 Barbecue Sauce", CurrentPrice=3.75, PurchasePrice=3.50, ExpirationDate=datetime.date(2025, 10, 10), Unit="Can", Quantity=50, InventoryHistoryLog=log1)

    # Add and commit all objects
    session.add_all([log1, log2, log3, item1, item2, item3, item4, item5])
    session.commit()

# Querying Data
with Session(engine) as session:
    stmt = (
        select(Item.ItemName, Item.Quantity)
        # FIX: 'InventoryHistoryLog.InventoryHistoryLogID' should be 'Log.InventoryHistoryLogID'
        .join(Log, Log.InventoryHistoryLogID == Item.InventoryHistoryLogID)
        # FIX: Reference the correct table ('Log') here
        .where(Log.ChangeType == "Removal")
    )
    results = session.execute(stmt).all()

    print("## Items with Inventory Log = Removal ##")
    # FIX: Loop is unpacking incorrect attributes. Adjust to match the selected columns.
    for item_name, quantity in results:
        print(f"Item: {item_name}, Quantity: {quantity}")
