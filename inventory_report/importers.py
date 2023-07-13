import json
from typing import Dict, Type
from abc import ABC, abstractmethod

from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        products = []
        try:
            with open(self.path) as file:
                data_products = json.load(file)
            for product in data_products:
                new_product = Product(
                    product["id"],
                    product["product_name"],
                    product["company_name"],
                    product["manufacturing_date"],
                    product["expiration_date"],
                    product["serial_number"],
                    product["storage_instructions"],
                )
                products.append(new_product)
            return products
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: {self.path}")


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
