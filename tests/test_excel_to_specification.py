import os
import pytest
from datacontract_specification.converters.excel_to_specification import convert_excel_to_specification

SAMPLE_EXCEL = "tests/fixtures/shipments-odcs.xlsx"

@pytest.mark.skipif(not os.path.exists(SAMPLE_EXCEL), reason="Sample Excel file not found.")
def test_excel_to_full_spec(tmp_path):
    odcs_file = Path(tmp_path) / "intermediate_odcs.yaml"
    spec_file = Path(tmp_path) / "datacontract_spec.yaml"

    convert_excel_to_specification(SAMPLE_EXCEL, str(odcs_file), str(spec_file))

    assert odcs_file.exists(), "Intermediate YAML ODCS not created"
    assert spec_file.exists(), "Final dataContractSpecification not created"

    output_content = spec_file.read_text()
    assert "dataContractSpecification" in output_content or "info" in output_content
