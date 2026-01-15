import sys
import textwrap

from rdflib import RDF, Graph, Namespace


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


def format_filenames(filenames: list, width: int = 150) -> list:
    formatted_lines = []
    current_line = "["
    for i, file in enumerate(filenames):
        if i > 0:
            current_line += ", "
        if len(current_line) + len(file) + 2 >= width - 4:
            formatted_lines.append(f"{current_line}")
            current_line = f"  '{file}'"
        else:
            current_line += f"'{file}'"
    formatted_lines.append(f"{current_line}]")
    return formatted_lines


def _extract_and_sort_errors(report_graph: Graph):
    """Helper to extract and sort errors from SHACL report graph."""
    SH = Namespace("http://www.w3.org/ns/shacl#")
    results = list(report_graph.subjects(RDF.type, SH.ValidationResult))
    error_rows = []
    for result in results:
        focus_node = report_graph.value(result, SH.focusNode)
        result_path = report_graph.value(result, SH.resultPath)
        result_message = report_graph.value(result, SH.resultMessage)
        severity = report_graph.value(result, SH.resultSeverity)
        error_rows.append(
            {
                "focus_node": focus_node,
                "result_path": result_path,
                "result_message": result_message,
                "severity": severity,
            }
        )
    # Sort deterministically
    error_rows.sort(
        key=lambda x: (
            str(x["focus_node"]),
            str(x["result_path"]) if x["result_path"] else "",
            str(x["result_message"]) if x["result_message"] else "",
        )
    )
    return error_rows


def _get_visual_width(text: str) -> int:
    """
    Calculate visual width of string, counting wide characters (emojis) as 2.
    """
    wide_chars = ["🔹", "❌", "✅", "⚠️", "🔍", "📌"]
    length = len(text)
    for char in wide_chars:
        length += text.count(char)
    return length


def _print_boxed_line(text: str, width: int, file=None):
    """
    Helper to print a line framed by "= ... =".
    Handles wide characters (emojis) correctly for alignment.
    """
    inner_width = width - 4
    visual_len = _get_visual_width(text)

    padding = inner_width - visual_len
    if padding < 0:
        padding = 0

    print(f"= {text}{' ' * padding} =", file=file)


def print_validation_result(
    success: bool,
    onto_files: list = None,
    v_text: str = "",
    report_graph: Graph = None,
    exit_code: int = None,
    file=None,
):
    width = 150
    border_line = "=" * width
    inner_width = width - 4

    if file is None:
        file = sys.stdout

    header_text = (
        ["✅ SHACL validation passed for:"]
        if success
        else ["❌ SHACL validation failed for:"]
    )

    # 1. Top Border
    print(border_line, file=file)

    # 2. Header
    for line in header_text:
        vis_len = _get_visual_width(line)
        total_padding = inner_width - vis_len
        left_pad = total_padding // 2
        right_pad = total_padding - left_pad
        print(f"= {' ' * left_pad}{line}{' ' * right_pad} =", file=file)

    # 3. Files
    if onto_files:
        _print_boxed_line(" ", width, file=file)  # Spacer
        formatted_filenames = format_filenames(onto_files, width)
        for line in formatted_filenames:
            print(f"= {line.center(inner_width)} =", file=file)

    # 4. Content (Errors)
    if not success and report_graph:
        # Structured Output inside the box
        _print_boxed_line(" ", width, file=file)
        print(f"= {'-' * inner_width} =", file=file)
        print(f"= {'Structured Validation Errors'.center(inner_width)} =", file=file)
        print(f"= {'-' * inner_width} =", file=file)

        errors = _extract_and_sort_errors(report_graph)

        for i, row in enumerate(errors):
            severity = (
                str(row["severity"]).split("#")[-1] if row["severity"] else "Violation"
            )

            # --- Node Line ---
            node_prefix_raw = f"🔹 [{severity}] Node: "
            node_prefix_vis_width = _get_visual_width(node_prefix_raw)

            prop_prefix_raw = "   Property: "
            err_prefix_raw = "   Error:    "

            # Pad prefixes to match Node prefix visual width
            prop_padding = node_prefix_vis_width - _get_visual_width(prop_prefix_raw)
            err_padding = node_prefix_vis_width - _get_visual_width(err_prefix_raw)

            prop_prefix = prop_prefix_raw + (" " * max(0, prop_padding))
            err_prefix = err_prefix_raw + (" " * max(0, err_padding))

            indent_str = " " * node_prefix_vis_width
            wrap_width = inner_width - node_prefix_vis_width

            # --- Node Value ---
            node_val = str(row["focus_node"])
            node_wrapper = textwrap.TextWrapper(width=wrap_width)
            node_lines = node_wrapper.wrap(node_val)

            if not node_lines:
                _print_boxed_line(node_prefix_raw, width, file=file)
            else:
                _print_boxed_line(f"{node_prefix_raw}{node_lines[0]}", width, file=file)
                for nl in node_lines[1:]:
                    _print_boxed_line(f"{indent_str}{nl}", width, file=file)

            # --- Property Line ---
            if row["result_path"]:
                prop_val = str(row["result_path"])
                prop_wrapper = textwrap.TextWrapper(width=wrap_width)
                prop_lines = prop_wrapper.wrap(prop_val)

                if not prop_lines:
                    _print_boxed_line(prop_prefix, width, file=file)
                else:
                    _print_boxed_line(f"{prop_prefix}{prop_lines[0]}", width, file=file)
                    for pl in prop_lines[1:]:
                        _print_boxed_line(f"{indent_str}{pl}", width, file=file)

            # --- Error Message ---
            if row["result_message"]:
                msg_text = str(row["result_message"])
                msg_wrapper = textwrap.TextWrapper(width=wrap_width)
                msg_lines = msg_wrapper.wrap(msg_text)

                if not msg_lines:
                    _print_boxed_line(err_prefix, width, file=file)
                else:
                    _print_boxed_line(f"{err_prefix}{msg_lines[0]}", width, file=file)
                    for ml in msg_lines[1:]:
                        _print_boxed_line(f"{indent_str}{ml}", width, file=file)

            # Separator between errors
            if i < len(errors) - 1:
                sep = "-" * inner_width
                print(f"= {sep} =", file=file)

    # 5. Bottom Border
    print(border_line, file=file)

    if exit_code is not None:
        print(f"Exiting with code {exit_code}", file=file)
        sys.exit(exit_code)


def print_validate_jsonld_against_shacl_result(
    success: bool,
    onto_files: list = None,
    v_text: str = "",
    report_graph: Graph = None,
    exit_code: int = None,
    file=None,
):
    print_validation_result(
        success,
        onto_files,
        v_text,
        report_graph=report_graph,
        exit_code=exit_code,
        file=file,
    )
