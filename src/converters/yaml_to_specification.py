import subprocess
from typing import Optional


def convert_yaml_to_specification(input_file: str, output_file: Optional[str] = None) -> str:
    """
    Converts a YAML ODCS file to a DataContractSpecification JSON format using the datacontract CLI.

    Args:
        input_file (str): Path to the YAML file.
        output_file (Optional[str]): Path to save the output. If None, output is returned.

    Returns:
        str: The JSON output if output_file is None; otherwise, an empty string.

    Raises:
        RuntimeError: If the CLI command fails.
    """
    cmd = ["datacontract", "import", "--format", "odcs", "--source", input_file]

    if output_file:
        print(f"Writing DataContractSpecification to file: {output_file}")
        cmd.extend(["--output", output_file])
    else:
        print(f"Writing output to screen...")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.stdout:
        return result.stdout
    elif result.stderr:
        raise RuntimeError(f"Error during conversion: {result.stderr}")
    else:
        raise RuntimeError("Unknown error during datacontract conversion.")