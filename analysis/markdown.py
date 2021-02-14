from enum import Enum
from typing import Protocol


class MarkdownSyntax(Enum):
    # Headings
    H1 = ('h1', '# {text}')
    H2 = ('h2', '## {text}')
    H3 = ('h3', '### {text}')
    # 4~6 may not needed?

    # Bold & Italic
    Bold = ('b', '**{text}**')
    Italic = ('i', '*{text}*')


class BufferedFileWrapper(Protocol):
    def push(self) -> None:
        """Push content buffer in FileWrapper object."""
        pass

    def pull(self, size: int) -> None:
        """
        Pull content in file into buffer.
        Args:
            size (int) : size of content to pull from buffer
        """
        pass


class Markdown:
    def __init__(self, fileName: str, override: bool = False) -> None:
        self._fileName = fileName
        self._buffer: str = ''
        self._doOverride: bool = override

    @property
    def fileName(self) -> str:
        return self._fileName

    @property
    def buffer(self) -> str:
        return self._buffer

    @property
    def text(self) -> str:
        with open(self._fileName, mode='rt', encoding='utf-8') as f:
            return f.read()

    def push(self) -> None:
        args = {'file': self._fileName, 'encoding': 'utf-8', 'mode': 'wt' if self._doOverride else 'at'}

        with open(**args) as f:
            f.write(self._buffer)

        if not self._doOverride:
            self._buffer = ''   # flush buffer.

    def _write(self, text: str) -> None:
        """
        Raw write method of markdown text.
        Args:
            text (str) : Markdown-formatted text to write.
        """
        self._buffer += text

    def write(self, syntax: MarkdownSyntax, text: str) -> None:
        self._write(syntax.value[1].format(text))

    def writeLine(self, syntax: MarkdownSyntax, text: str) -> None:
        """
        Args:
            syntax: # Markdown syntax to apply
            text (str) : a single line of text to write.
        """
        self._write(syntax.value[1].format(text + '\n'))

    def close(self) -> None:
        self.push()

    def __del__(self) -> None:
        self.close()


