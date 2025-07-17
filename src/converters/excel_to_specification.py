from datacontract_specification.converters.excel_to_yaml import convert_excel_to_yaml
from datacontract_specification.converters.yaml_to_specification import convert_yaml_to_specification


def convert_excel_to_specification(
    excel_file_path: str,
    odcs_file_path: str,
    datacontract_file_path: str
) -> None:
    """
    Converts an Excel ODCS file directly into a DataContractSpecification JSON file
    by first converting it to YAML, then to JSON using the datacontract CLI.

    Args:
        excel_file_path (str): Path to the Excel (.xlsx) ODCS file.
        odcs_file_path (str): Path where intermediate YAML ODCS will be written.
        datacontract_file_path (str): Path where final DataContractSpecification JSON will be saved.

    Raises:
        Exception: If conversion fails at any step.
    """
    print(f"Converting Excel -> YAML -> DataContractSpecification YAML...")
    try:
        convert_excel_to_yaml(excel_file_path, odcs_file_path)
        convert_yaml_to_specification(odcs_file_path, datacontract_file_path)
        print(f"✔️ Conversion completed. Output saved to {datacontract_file_path}")
    except Exception as e:
        raise Exception(f"Error during conversion pipeline: {e}\nCheck that no output path is 'None'")