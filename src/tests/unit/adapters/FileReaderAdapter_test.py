import io
from adapters.FileReaderAdapter import read_file


def test_read_file_gets_file_content():
    file_content = "Some content to be in file"
    file = io.StringIO(file_content)

    file_reader_result = read_file(file)

    assert [file_content] == file_reader_result

