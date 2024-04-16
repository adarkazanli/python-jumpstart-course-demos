import pytest
from io import StringIO
import program  # Assuming the provided code is saved in a file named program.py


# Helper function to capture print statements
def capture_print(monkeypatch, input_value):
    # Mock input() to return the provided input_value
    monkeypatch.setattr("builtins.input", lambda _: input_value)
    # Capture the output of print()
    output = StringIO()
    monkeypatch.setattr("sys.stdout", output)
    return output


@pytest.mark.parametrize(
    "input_value,expected_output",
    [
        # Happy path tests
        pytest.param("Alice", "Have a nice day Alice!", id="happy-path-name-Alice"),
        pytest.param("Bob", "Have a nice day Bob!", id="happy-path-name-Bob"),
        # Edge case: empty input
        pytest.param("", "You didn't enter your name", id="edge-case-empty-input"),
        # Edge case: long name
        pytest.param(
            "A" * 100, f"Have a nice day {'A' * 100}!", id="edge-case-long-name"
        ),
        # Edge case: special characters
        pytest.param(
            "@lice!", "Have a nice day @lice!!", id="edge-case-special-characters"
        ),
        # Error case: input as None (simulating unexpected behavior, though not directly applicable without mocking input differently)
        # This is more of a theoretical case, as input() would not normally return None, but it's included for completeness
        pytest.param(
            None,
            "You didn't enter your name",
            id="error-case-none-input",
            marks=pytest.mark.xfail(
                reason="input() mocked to return None, which is not standard behavior"
            ),
        ),
    ],
)
def test_main(monkeypatch, input_value, expected_output):
    output = capture_print(monkeypatch, input_value)
    program.main()
    output.seek(0)  # Go back to the beginning of the StringIO buffer
    output_text = output.read()
    assert expected_output in output_text
