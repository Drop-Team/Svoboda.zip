class ZippError(Exception):
    status_code = 503
    message = ""


class DirectoryConsistencyError(ZippError):
    def __init__(self, data):
        self.data = data
        self.status_code = 503
        self.message = "Your directory consistency were corrupted! This error occurs in: "
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}{self.data}'


class FileConsistencyError(ZippError):
    def __init__(self, data):
        self.data = data
        self.status_code = 503
        self.message = "Your file consistency were corrupted! This error occurs in: "
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}{self.data}'


class NoSuchZippError(ZippError):
    def __init__(self, data):
        self.data = data
        self.status_code = 404
        self.message = "Zipp package is not installed! "
        super().__init__(self.message)

    def __str__(self):
        return f'<{self.data}>{self.message}'


class CorruptedZippError(ZippError):
    def __init__(self, data):
        self.data = data
        self.status_code = 503
        self.message = "This zipp package is corrupted! This error occurs in: "
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}{self.data}'



class CorruptedFileError(ZippError):
    def __init__(self, file_name, data):
        self.data = data
        self.file_name = file_name
        self.message = " is corrupted! Can't start due to: "
        super().__init__(self.message)

    def __str__(self):
        return f'"{self.file_name}"{self.message}{self.data}'


class ZippConflictError(ZippError):
    def __init__(self, data):
        self.data = data
        self.status_code = 503
        self.message = "Zipp package conflicting with another one!"
        super().__init__(self.message)

    def __str__(self):
        return f'<{self.data}>{self.message}'
