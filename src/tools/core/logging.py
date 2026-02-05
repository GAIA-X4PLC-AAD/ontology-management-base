#!/usr/bin/env python3
"""
Logging - Centralized Logger Configuration

Provides a consistent logging interface for all modules in the validation suite.
Uses Python's standard logging module with a standardized format.

FEATURE SET:
============
1. get_logger - Get a configured logger for a module
2. configure_logging - Set up logging level and format globally
3. LogLevel - Enum for log level constants

USAGE:
======
    from src.tools.core.logging import get_logger

    logger = get_logger(__name__)

    def my_function():
        logger.info("Starting process")
        logger.debug("Detail: %s", some_var)
        logger.warning("Potential issue: %s", warning)
        logger.error("Failed: %s", error)

STANDALONE TESTING:
==================
    python3 -m src.tools.core.logging [--test] [--level DEBUG]

    Options:
      --test      Run self-tests
      --level     Set log level (DEBUG, INFO, WARNING, ERROR)

DEPENDENCIES:
=============
- logging (stdlib)

NOTES:
======
- All modules should use get_logger(__name__) for consistent naming
- CLI output (print) is for user-facing results; logging is for progress/debug
- Default level is INFO; use DEBUG for detailed tracing
"""

import argparse
import logging
import sys
from enum import IntEnum
from typing import Optional

# Default format: timestamp - module - level - message
DEFAULT_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
SHORT_FORMAT = "%(levelname)s: %(message)s"

# Track if logging has been configured globally
_logging_configured = False


class LogLevel(IntEnum):
    """Log level constants matching Python's logging module."""

    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


def configure_logging(
    level: int = logging.INFO,
    format_string: str = None,
    stream: Optional[object] = None,
) -> None:
    """
    Configure logging globally for the application.

    This should be called once at application startup (e.g., in main()).
    Subsequent calls will update the configuration.

    Args:
        level: Logging level (use LogLevel enum or logging constants)
        format_string: Custom format string (default: SHORT_FORMAT)
        stream: Output stream (default: sys.stderr)
    """
    global _logging_configured

    if format_string is None:
        format_string = SHORT_FORMAT

    if stream is None:
        stream = sys.stderr

    # Remove existing handlers to avoid duplicates
    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Configure with new settings
    logging.basicConfig(
        level=level,
        format=format_string,
        stream=stream,
    )

    _logging_configured = True


def get_logger(name: str) -> logging.Logger:
    """
    Get a configured logger for a module.

    Args:
        name: Module name (typically __name__)

    Returns:
        Configured Logger instance

    Example:
        >>> logger = get_logger(__name__)
        >>> logger.info("Processing started")
    """
    # Ensure logging is configured with defaults if not already done
    global _logging_configured
    if not _logging_configured:
        configure_logging()

    # Shorten the module path for cleaner output
    # e.g., "src.tools.utils.file_collector" -> "file_collector"
    short_name = name.split(".")[-1] if "." in name else name

    logger = logging.getLogger(short_name)
    return logger


def set_level(level: int) -> None:
    """
    Set the logging level for the root logger.

    Args:
        level: Logging level (use LogLevel enum or logging constants)
    """
    logging.getLogger().setLevel(level)


def enable_debug() -> None:
    """Enable DEBUG level logging."""
    set_level(LogLevel.DEBUG)


def enable_verbose() -> None:
    """Enable verbose (DEBUG) logging with detailed format."""
    configure_logging(level=LogLevel.DEBUG, format_string=DEFAULT_FORMAT)


def _run_tests() -> bool:
    """Run self-tests for the module."""
    import io

    print("Running logging self-tests...")
    all_passed = True

    # Test 1: get_logger returns a logger
    try:
        logger = get_logger("test_module")
        assert logger is not None
        assert isinstance(logger, logging.Logger)
        print("PASS: get_logger returns Logger instance")
    except AssertionError as e:
        print(f"FAIL: get_logger - {e}")
        all_passed = False

    # Test 2: Logger name is shortened
    try:
        logger = get_logger("src.tools.utils.file_collector")
        assert logger.name == "file_collector"
        print("PASS: Logger name shortened correctly")
    except AssertionError as e:
        print(f"FAIL: Logger name shortening - {e}")
        all_passed = False

    # Test 3: configure_logging changes level
    try:
        test_stream = io.StringIO()
        configure_logging(level=LogLevel.DEBUG, stream=test_stream)
        logger = get_logger("test_level")
        logger.debug("Debug message")
        output = test_stream.getvalue()
        assert "Debug message" in output
        print("PASS: configure_logging sets level correctly")
    except AssertionError as e:
        print(f"FAIL: configure_logging - {e}")
        all_passed = False

    # Test 4: LogLevel enum values match logging constants
    try:
        assert LogLevel.DEBUG == logging.DEBUG
        assert LogLevel.INFO == logging.INFO
        assert LogLevel.WARNING == logging.WARNING
        assert LogLevel.ERROR == logging.ERROR
        print("PASS: LogLevel enum values correct")
    except AssertionError as e:
        print(f"FAIL: LogLevel enum - {e}")
        all_passed = False

    # Reset logging config
    configure_logging()

    print()
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests FAILED!")

    return all_passed


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--test", action="store_true", help="Run self-tests")
    parser.add_argument(
        "--level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Set log level for demo",
    )

    args = parser.parse_args()

    if args.test:
        success = _run_tests()
        sys.exit(0 if success else 1)

    # Demo logging
    level = getattr(LogLevel, args.level)
    configure_logging(level=level)

    logger = get_logger(__name__)
    logger.debug("This is a DEBUG message")
    logger.info("This is an INFO message")
    logger.warning("This is a WARNING message")
    logger.error("This is an ERROR message")


if __name__ == "__main__":
    main()
