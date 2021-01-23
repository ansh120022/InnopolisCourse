from main import valid_email, log
import pytest



class TestEmail:

    @pytest.mark.parametrize("email, log_file,  expected_result", [
        # positive scenarios
        pytest.param("test@test.ru", "passed.txt", True),
        pytest.param("w@w.com", "passed.txt", True),
        pytest.param("123QWE@mmm.mmm", "passed.txt", True),

        # negative scenarios
        pytest.param("test@test.", "failed.txt", False),
        pytest.param("test@test.", "failed.txt", False),
        pytest.param("@tt", "failed.txt", False)

    ])
    def test_valid_email(self, email, log_file, expected_result):
        func_result = valid_email(email)
        log(log_file, f"{email} -> expected_result is {expected_result} -> actual_result is {func_result}\n")
        assert func_result == expected_result

