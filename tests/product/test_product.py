from inventory_report.product import Product


def test_create_product() -> None:
    id = "1"
    product_name = "Nicotine Polacrilex"
    company_name = "Target Corporation"
    manufacturing_date = "2021-02-18"
    expiration_date = "2023-09-17"
    serial_number = "CR25 1551 4467 2549 4402 1"
    storage_instructions = "instrucao 1"
    product = Product(
        id,
        product_name,
        company_name,
        manufacturing_date,
        expiration_date,
        serial_number,
        storage_instructions,
    )
    assert product.id == id
    assert product.product_name == product_name
    assert product.company_name == company_name
    assert product.manufacturing_date == manufacturing_date
    assert product.expiration_date == expiration_date
    assert product.serial_number == serial_number
    assert product.storage_instructions == storage_instructions
