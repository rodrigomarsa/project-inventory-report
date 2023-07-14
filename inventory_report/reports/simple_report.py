from typing import List
from inventory_report.inventory import Inventory
from datetime import date
from inventory_report.product import Product
from inventory_report.reports.report import Report


class SimpleReport(Report):
    def __init__(self) -> None:
        self.inventories: List[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def generate(self) -> str:
        for inventory in self.inventories:
            sorted_by_m_d = sorted(
                inventory.data, key=lambda p: p.manufacturing_date
            )

            def expiration_date_key(product: Product) -> str:
                if product.expiration_date >= str(date.today()):
                    return product.expiration_date
                else:
                    return str(date.max)

            sorted_by_e_d = sorted(inventory.data, key=expiration_date_key)
            company = max(inventory.data, key=lambda p: p.company_name)
        return (
            f"Oldest manufacturing date: {sorted_by_m_d[0].manufacturing_date}"
            f"Closest expiration date: {sorted_by_e_d[0].expiration_date}"
            f"Company with the largest inventory: {company.company_name}"
        )
