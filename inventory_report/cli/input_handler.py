from typing import List

from inventory_report.importers import CsvImporter, JsonImporter
from inventory_report.inventory import Inventory
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def process_report_request(file_paths: List[str], report_type: str) -> str:
    report_options = {"simple": SimpleReport(), "complete": CompleteReport()}
    inventory = Inventory()

    if report_type not in report_options.keys():
        raise ValueError("Report type is invalid.")

    for file_path in file_paths:
        if file_path.endswith(".json"):
            from_json = JsonImporter(file_path)
            data = from_json.import_data()
        elif file_path.endswith(".csv"):
            from_csv = CsvImporter(file_path)
            data = from_csv.import_data()
        else:
            continue
        report = report_options[report_type]
        inventory.add_data(data)
        report.add_inventory(inventory)
    return report.generate()
