class BaseDynamicSidecarError(Exception):
    """Used as base for all exceptions"""

    def __init__(self, message: str, status: int = 500) -> None:
        self.message: str = message
        self.status: int = status
        super().__init__(message)


class UnexpectedDockerError(BaseDynamicSidecarError):
    def __init__(self, message: str, status: int) -> None:
        super().__init__(
            f"An unexpected Docker error occurred {status=}, {message=}", status=status
        )
