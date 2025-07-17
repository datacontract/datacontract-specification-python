import os
import pytest
from datacontract_specification.converters.excel_to_yaml import convert_excel_to_yaml

SAMPLE_EXCEL_PATH = "tests/fixtures/shipments-odcs.xlsx"

@pytest.mark.skipif(not os.path.exists(SAMPLE_EXCEL_PATH), reason="Test file not found.")
def test_excel_to_yaml_stdout():
    yaml_output = convert_excel_to_yaml(SAMPLE_EXCEL_PATH)
    assert isinstance(yaml_output, str)
    assert "title:" in yaml_output or "version:" in yaml_output  # Adapt as needed

@pytest.mark.skipif(not os.path.exists(SAMPLE_EXCEL_PATH), reason="Test file not found.")
def test_excel_to_yaml_output_file(tmp_path):
    output_path = Path(tmp_path) / "odcs_output.yaml"
    convert_excel_to_yaml(SAMPLE_EXCEL_PATH, str(output_path))
    assert output_path.exists()
    content = output_path.read_text()
    assert "title:" in content or "version:" in content
