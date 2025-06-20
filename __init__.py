class CP:
    COLOR_CODES = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'white': '\033[97m',
    }

    SHORTCUTS = {
        'r': 'red',
        'g': 'green',
        'y': 'yellow',
        'b': 'blue',
    }

    def __init__(self):
        self.reset = '\033[0m'
        self.bold = '\033[1m'

    def _resolve_color(self, color_input):
        """컬러 입력을 실제 ANSI 코드로 변환"""
        if color_input in self.SHORTCUTS:
            color_input = self.SHORTCUTS[color_input]
        return self.COLOR_CODES.get(color_input, self.COLOR_CODES['white'])  # ❗기본값: white

    def printc(self, color=None, **kwargs):
        """기본 컬러 출력"""
        c = self._resolve_color(color)
        for key, value in kwargs.items():
            print(f"{c}{key} = {value}{self.reset}")

    def printcb(self, color=None, **kwargs):
        """볼드 컬러 출력"""
        c = self._resolve_color(color)
        for key, value in kwargs.items():
            print(f"{c}{self.bold}{key} = {value}{self.reset}")

    def printB(self, color=None, line=3, **kwargs):
        """볼드 + 컬러 + 줄바꿈 포함 상자 출력"""
        c = self._resolve_color(color)
        linear = "=" * 15
        top_bottom = "\n" * line
        lines = []

        for key, value in kwargs.items():
            line_str = f"{c}{self.bold}{key} = {value}{self.reset}"
            lines.append(line_str)

        content = "\n".join(lines)
        print(f"{c}{linear}{self.reset}{top_bottom}{content}{top_bottom}{c}{linear}{self.reset}")
