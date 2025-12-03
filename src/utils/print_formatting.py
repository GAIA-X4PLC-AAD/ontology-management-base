import sys
import textwrap


def format_validate_target_classes_against_owl_classes_result(
    ontology_file,
    num_ontology_classes,
    num_shacl_classes,
    matches,
    missing_classes,
    recovered_classes,
    extra_classes,
):
    """
    Format a summary of the validation results in a properly aligned boxed layout.
    """
    width = 150
    border = "=" * width
    separator = f"=={' ' * (width - 4)}=="

    output_lines = []
    output_lines.append("\n" + border)
    output_lines.append(f"=={' VALIDATION SUMMARY ':^{width-4}}==")
    output_lines.append(border)
    output_lines.append(f"==  Ontology File: {ontology_file.ljust(width - 21)}==")
    output_lines.append(separator)
    output_lines.append(
        f"==  🔹 Ontology Classes: {str(num_ontology_classes).ljust(width - 27)}=="
    )
    output_lines.append(
        f"==  🔹 SHACL Target Classes: {str(num_shacl_classes).ljust(width - 31)}=="
    )
    output_lines.append(
        f"==  ✅ Matched Classes: {str(len(matches) + len(recovered_classes)).ljust(width - 26)}=="
    )
    output_lines.append(
        f"==  ❌ Missing Classes: {str(len(missing_classes)).ljust(width - 26)}=="
    )
    output_lines.append(
        f"==  ⚠️ Extra Classes: {str(len(extra_classes)).ljust(width - 23)}=="
    )
    output_lines.append(border)

    if missing_classes:
        output_lines.append(
            f"==  ❌ Missing SHACL Classes: {str(len(missing_classes)).ljust(width - 32)}=="
        )
        for cls in sorted(missing_classes):
            output_lines.append(f"==  ❌ {cls.ljust(width - 9)}==")
        output_lines.append(border)

    if extra_classes:
        output_lines.append(
            f"==  ⚠️ Extra Ontology Classes: {str(len(extra_classes)).ljust(width - 32)}=="
        )
        for cls in sorted(extra_classes):
            output_lines.append(f"==  ⚠️ {cls.ljust(width - 8)}==")
        output_lines.append(border)

    if missing_classes:
        output_lines.append(f"=={' ❌ Validation failed! ':^{width-5}}==")
    else:
        output_lines.append(f"=={' ✅ Validation successful! ':^{width-5}}==")
    output_lines.append(border)
    return "\n".join(output_lines)


# --- Formatting and Printing Functions ---
def format_validation_report(
    v_text: str, width: int = 150, indent_size: int = 4
) -> str:
    border_line = "=" * width
    formatted_lines = []
    breakpoints = [
        "Validation Report",
        "Conforms:",
        "Results (",
        "Constraint Violation in",
        "Severity:",
        "Source Shape:",
        "Focus Node:",
        "Value Node:",
        "Message:",
        "Result Path:",
    ]
    for bp in breakpoints:
        v_text = v_text.replace(bp, f"\n{bp}")
    indent_level = 0
    last_line_was_blank = False
    for line in v_text.splitlines():
        stripped_line = line.strip()
        if not stripped_line:
            if last_line_was_blank:
                continue
            last_line_was_blank = True
            formatted_lines.append(f"= {' ' * (width - 4)} =")
            continue
        else:
            last_line_was_blank = False
        if stripped_line in breakpoints or stripped_line.endswith(":"):
            indent_level = 0
        elif stripped_line.startswith("sh:") or stripped_line.startswith("skos:"):
            indent_level = 1
        elif stripped_line.startswith("[") or stripped_line.startswith("]"):
            indent_level = 2
        elif stripped_line.startswith("<") and stripped_line.endswith(">"):
            indent_level = 2
        elif stripped_line.startswith("Literal("):
            indent_level = 3
        elif stripped_line.startswith("datatype="):
            indent_level = 4
        indent_space = " " * (indent_level * indent_size)
        wrapped_lines = textwrap.fill(
            stripped_line, width=width - 4 - len(indent_space)
        )
        for wrapped_line in wrapped_lines.split("\n"):
            formatted_lines.append(
                f"= {indent_space}{wrapped_line.ljust(width - 4 - len(indent_space))} ="
            )
    return f"{border_line}\n" + "\n".join(formatted_lines) + f"\n{border_line}"


def format_filenames(filenames: list, width: int = 150) -> list:
    formatted_lines = []
    current_line = "["
    for i, file in enumerate(filenames):
        if i > 0:
            current_line += ", "
        if len(current_line) + len(file) + 2 >= width - 4:
            formatted_lines.append(f"{current_line}")
            current_line = "  " + file
        else:
            current_line += f"'{file}'"
    formatted_lines.append(f"{current_line}]")
    return formatted_lines


def print_validation_result(
    success: bool,
    onto_files: list = None,
    v_text: str = "",
    exit_code: int = None,
    file=None,  # new argument to redirect output
):
    width = 150
    border_line = "=" * width
    header_text_files = [""]
    header_text = (
        ["✅ SHACL validation passed for:"]
        if success
        else ["❌ SHACL validation failed for:"]
    )
    centered_header_lines = [f"= {line.center(width - 5)} =" for line in header_text]
    if onto_files:
        formatted_filenames = format_filenames(onto_files, width)
        header_text_files.extend(formatted_filenames)
        centered_header_file_lines = [
            f"= {line.center(width - 4)} =" for line in header_text_files
        ]
    print(border_line, file=file)
    print("\n".join(centered_header_lines), file=file)
    if onto_files:
        print("\n".join(centered_header_file_lines), file=file)
    print(border_line, file=file)
    if not success:
        formatted_v_text = format_validation_report(v_text, width)
        print(formatted_v_text, file=file)
    if exit_code is not None:
        print(f"Exiting with code {exit_code}")
        sys.exit(exit_code)


def print_validate_jsonld_against_shacl_result(
    success: bool,
    onto_files: list = None,
    v_text: str = "",
    exit_code: int = None,
    file=None,
):
    print_validation_result(success, onto_files, v_text, exit_code, file=file)
