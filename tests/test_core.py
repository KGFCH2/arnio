import pytest
import sys
import importlib

def test_missing_cpp_extension_error_message(monkeypatch):
    """Ensure that a missing _arnio_cpp extension raises an ImportError with a helpful message."""
    # Temporarily hide the _arnio_cpp module to simulate a missing extension
    monkeypatch.setitem(sys.modules, "_arnio_cpp", None)
    
    # We must also ensure arnio._core is removed so it is re-imported
    if "arnio._core" in sys.modules:
        monkeypatch.delitem(sys.modules, "arnio._core")

    with pytest.raises(ImportError) as exc_info:
        importlib.import_module("arnio._core")

    error_msg = str(exc_info.value)
    
    assert "arnio C++ extension (_arnio_cpp) not found" in error_msg
    assert "pip install -e ." in error_msg
    assert "Desktop development with C++" in error_msg
    assert "gcc or clang" in error_msg
