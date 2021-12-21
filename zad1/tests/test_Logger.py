from unittest import TestCase
from unittest.mock import mock_open, patch, call
from assertpy import assert_that
from src.Logger import Logger
from src.Log import Log


class TestLogger(TestCase):
    def setUp(self) -> None:
        self.temp_logger = Logger()

    def test_add_log(self) -> None:
        new_log = Log(1, "hehe log 1")
        self.temp_logger.add_log(new_log)
        assert_that(len(self.temp_logger.logs)).is_equal_to(1)

    def test_add_log_already_exist(self) -> None:
        new_log = Log(1, "hehe log 1")
        self.temp_logger.logs = {
            1: new_log
        }
        assert_that(self.temp_logger.add_log).raises(
            ValueError).when_called_with(new_log)

    def test_get_log(self) -> None:
        new_log = Log(1, "hehe log 1")
        self.temp_logger.logs = {
            1: new_log
        }
        assert_that(self.temp_logger.get_log(1)).is_equal_to(new_log)

    def test_clear_logs(self) -> None:
        new_log = Log(1, "hehe log 1")
        new_log2 = Log(2, "hehe log 2")
        self.temp_logger.logs = {
            1: new_log,
            2: new_log2
        }
        self.temp_logger.clear_logs()
        assert_that(len(self.temp_logger.logs)).is_equal_to(0)

    def test_import_log_file(self) -> None:
        with patch("builtins.open", mock_open(read_data="1, hmm_test")) as mock_file:
            self.temp_logger.import_log_file('test_file')
        assert_that(self.temp_logger.logs.get(1).text).is_equal_to(" hmm_test")

    def test_write_log_file(self) -> None:
        new_log = Log(1, "hehe log 1")
        new_log2 = Log(2, "hehe log 2")
        self.temp_logger.logs = {
            1: new_log,
            2: new_log2
        }
        with patch("builtins.open") as mock_file:
            self.temp_logger.write_log_file('test')
        mock_write = mock_file.return_value.__enter__.return_value.write
        mock_write.assert_has_calls(
            [call("1, hehe log 1\n"), call("2, hehe log 2\n")])

    def test_delete_log_file(self) -> None:
        with patch("os.path.exists") as mock_os_path_exist:
            mock_os_path_exist.return_value = True
            with patch("os.remove") as mock_os_remove:
                self.temp_logger.delete_log_file("test")
        mock_os_remove.assert_has_calls([call("test.log")])

    def test_delete_log_file_no_file(self) -> None:
        with patch("os.path.exists") as mock_os_path_exist:
            mock_os_path_exist.return_value = False
            assert_that(self.temp_logger.delete_log_file).raises(
                FileNotFoundError).when_called_with("no_file")
