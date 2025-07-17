import subprocess
from typing import Optional


def convert_excel_to_yaml(input_file: str, output_file: Optional[str] = None) -> str:
    """
    Converts an Excel ODCS file to YAML using the datacontract CLI.

    Args:
        input_file (str): Path to the Excel file.
        output_file (Optional[str]): Path to write YAML output to. If None, output is returned to screen.

    Returns:
        str: The YAML output if output_file is None; otherwise, empty string.
    """
    cmd = ["datacontract", "import", "--format", "excel", "--source", input_file]

    if output_file:
        print(f"Writing YAML ODCS to file: {output_file}")
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
