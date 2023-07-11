# flake8: noqa

import pytest

from inventory_report.cli import input_handler


@pytest.mark.parametrize(
    "report_type",
    [
        pytest.param("simple", marks=pytest.mark.dependency),
        pytest.param("complete", marks=pytest.mark.dependency),
    ],
)
def test_process_report_returns_correct_oldest_date(report_type: str) -> None:
    result = input_handler.process_report_request(
        ["tests/mocks/inventory.csv"], report_type
    )
    assert "Oldest manufacturing date: 2020-09-06" in result


@pytest.mark.parametrize(
    "report_type",
    [
        pytest.param("simple", marks=pytest.mark.dependency),
        pytest.param("complete", marks=pytest.mark.dependency),
    ],
)
def test_process_report_returns_correct_closest_expiration_date(
    report_type: str,
) -> None:
    result = input_handler.process_report_request(
        ["tests/mocks/inventory.csv"], report_type
    )
    assert "Closest expiration date: 2023-09-17" in result


@pytest.mark.parametrize(
    "report_type",
    [
        pytest.param("simple", marks=pytest.mark.dependency),
        pytest.param("complete", marks=pytest.mark.dependency),
    ],
)
def test_process_report_returns_correct_company_with_largest_inventory(
    report_type: str,
) -> None:
    result = input_handler.process_report_request(
        ["tests/mocks/inventory.csv"], report_type
    )
    assert "Company with the largest inventory: Target Corporation" in result


def test_process_report_should_raise_error_with_invalid_report_type() -> None:
    with pytest.raises(ValueError, match="Report type is invalid."):
        input_handler.process_report_request(["tests/mocks/inventory.csv"], "invalid")


@pytest.mark.parametrize(
    "report_type",
    [
        pytest.param("simple", marks=pytest.mark.dependency),
        pytest.param("complete", marks=pytest.mark.dependency),
    ],
)
def test_process_report_should_ignore_unsuported_inventory_files(
    report_type: str,
) -> None:
    first_result = input_handler.process_report_request(
        ["tests/mocks/inventory.csv"], report_type
    )

    second_result = input_handler.process_report_request(
        ["tests/mocks/inventory.csv", "tests/mocks/inventory.txt"], report_type
    )

    assert first_result == second_result


def test_process_report_should_use_all_supported_files_available() -> None:
    result = input_handler.process_report_request(
        ["tests/mocks/inventory.csv", "tests/mocks/inventory.json"], "complete"
    )

    assert (
        """Stocked products by company:
- Target Corporation: 8
- Galena Biopharma: 4
- Cantrell Drug Company: 4
- Moore Medical LLC: 2
- REMEDYREPACK: 2"""
        in result
    )


# Testes do requisito 10
@pytest.mark.dependency(
    depends=[
        "test_process_report_returns_correct_oldest_date[simple]",
        "test_process_report_returns_correct_oldest_date[complete]",
        "test_process_report_returns_correct_closest_expiration_date[simple]",
        "test_process_report_returns_correct_closest_expiration_date[complete]",
        "test_process_report_returns_correct_company_with_largest_inventory[simple]",
        "test_process_report_returns_correct_company_with_largest_inventory[complete]",
        "test_process_report_should_ignore_unsuported_inventory_files[simple]",
        "test_process_report_should_ignore_unsuported_inventory_files[complete]",
        "test_process_report_should_raise_error_with_invalid_report_type",
        "test_process_report_should_use_all_supported_files_available",
    ],
)
def test_process_report_final() -> None:
    pass
