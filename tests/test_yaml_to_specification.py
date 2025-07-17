import os
import pytest
from datacontract_specification.converters.yaml_to_specification import convert_yaml_to_specification

SAMPLE_YAML_PATH = "tests/fixtures/odcs_output.yaml"

@pytest.mark.skipif(not os.path.exists(SAMPLE_YAML_PATH), reason="Test YAML file not found.")
def test_yaml_to_spec_stdout():
    output = convert_yaml_to_specification(SAMPLE_YAML_PATH)
    assert isinstance(output, str)
    assert "dataContractSpecification" in output or "info" in output  # Adjust based on real structure

@pytest.mark.skipif(not os.path.exists(SAMPLE_YAML_PATH), reason="Test YAML file not found.")
def test_yaml_to_spec_file(tmp_path):
    output_path = Path(tmp_path) / "specification_output.yaml"
    convert_yaml_to_specification(SAMPLE_YAML_PATH, str(output_path))
    assert output_path.exists()
    content = output_path.read_text()
    assert "dataContractSpecification" in content or "info" in content
