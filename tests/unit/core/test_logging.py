#!/usr/bin/env python3
"""
Unit tests for src.tools.core.logging module.
"""

import io
import logging


class TestGetLogger:
    """Tests for get_logger function."""

    def test_returns_logger_instance(self):
        """get_logger should return a Logger instance."""
        from src.tools.core.logging import get_logger

        logger = get_logger("test_module")

        assert logger is not None
        assert isinstance(logger, logging.Logger)

    def test_shortens_module_path(self):
        """get_logger should shorten long module paths."""
        from src.tools.core.logging import get_logger

        logger = get_logger("src.tools.utils.file_collector")

        assert logger.name == "file_collector"

    def test_preserves_simple_name(self):
        """get_logger should preserve simple names without dots."""
        from src.tools.core.logging import get_logger

        logger = get_logger("simple_name")

        assert logger.name == "simple_name"

    def test_same_name_returns_same_logger(self):
        """get_logger should return the same logger for the same name."""
        from src.tools.core.logging import get_logger

        logger1 = get_logger("same_module")
        logger2 = get_logger("same_module")

        assert logger1 is logger2


class TestConfigureLogging:
    """Tests for configure_logging function."""

    def test_sets_log_level(self):
        """configure_logging should set the specified log level."""
        from src.tools.core.logging import LogLevel, configure_logging, get_logger

        test_stream = io.StringIO()
        configure_logging(level=LogLevel.DEBUG, stream=test_stream)
        logger = get_logger("test_level_config")

        logger.debug("Debug message")

        output = test_stream.getvalue()
        assert "Debug message" in output

    def test_filters_below_level(self):
        """configure_logging should filter messages below the set level."""
        from src.tools.core.logging import LogLevel, configure_logging, get_logger

        test_stream = io.StringIO()
        configure_logging(level=LogLevel.WARNING, stream=test_stream)
        logger = get_logger("test_filter")

        logger.info("Info message")
        logger.warning("Warning message")

        output = test_stream.getvalue()
        assert "Info message" not in output
        assert "Warning message" in output

    def test_custom_format(self):
        """configure_logging should accept custom format string."""
        from src.tools.core.logging import LogLevel, configure_logging, get_logger

        test_stream = io.StringIO()
        custom_format = "CUSTOM: %(message)s"
        configure_logging(
            level=LogLevel.INFO, format_string=custom_format, stream=test_stream
        )
        logger = get_logger("test_custom_format")

        logger.info("Test message")

        output = test_stream.getvalue()
        assert "CUSTOM: Test message" in output


class TestLogLevel:
    """Tests for LogLevel enum."""

    def test_debug_matches_logging_debug(self):
        """LogLevel.DEBUG should match logging.DEBUG."""
        from src.tools.core.logging import LogLevel

        assert LogLevel.DEBUG == logging.DEBUG

    def test_info_matches_logging_info(self):
        """LogLevel.INFO should match logging.INFO."""
        from src.tools.core.logging import LogLevel

        assert LogLevel.INFO == logging.INFO

    def test_warning_matches_logging_warning(self):
        """LogLevel.WARNING should match logging.WARNING."""
        from src.tools.core.logging import LogLevel

        assert LogLevel.WARNING == logging.WARNING

    def test_error_matches_logging_error(self):
        """LogLevel.ERROR should match logging.ERROR."""
        from src.tools.core.logging import LogLevel

        assert LogLevel.ERROR == logging.ERROR

    def test_critical_matches_logging_critical(self):
        """LogLevel.CRITICAL should match logging.CRITICAL."""
        from src.tools.core.logging import LogLevel

        assert LogLevel.CRITICAL == logging.CRITICAL


class TestSetLevel:
    """Tests for set_level function."""

    def test_changes_root_logger_level(self):
        """set_level should change the root logger level."""
        from src.tools.core.logging import LogLevel, set_level

        set_level(LogLevel.ERROR)

        assert logging.getLogger().level == logging.ERROR

        # Reset
        set_level(LogLevel.INFO)


class TestEnableDebug:
    """Tests for enable_debug function."""

    def test_sets_debug_level(self):
        """enable_debug should set level to DEBUG."""
        from src.tools.core.logging import LogLevel, enable_debug

        enable_debug()

        assert logging.getLogger().level == LogLevel.DEBUG

        # Reset
        from src.tools.core.logging import set_level

        set_level(LogLevel.INFO)
