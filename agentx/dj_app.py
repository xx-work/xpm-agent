import sys


class Application:

    def start_server(self):
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "请确定是不是环境错误, 找不到Django的包,检查PYTHON_PATH"
            ) from exc
        execute_from_command_line(sys.argv[1:])


if __name__ == '__main__':
    pass