from http import HTTPStatus


class ApplicationException(Exception):
    """
    Base exception for all application-specific errors.
    """

    def __init__(
        self,
        message: str,
        error_code: str,
        status_code: int,
    ) -> None:
        self.message = message
        self.error_code = error_code
        self.status_code = status_code

        super().__init__(message)


class ValidationException(ApplicationException):
    def __init__(self, message: str) -> None:
        super().__init__(
            message=message,
            error_code="VALIDATION_ERROR",
            status_code=HTTPStatus.BAD_REQUEST,
        )


class AuthenticationException(ApplicationException):
    def __init__(self, message: str = "Authentication failed") -> None:
        super().__init__(
            message=message,
            error_code="AUTHENTICATION_ERROR",
            status_code=HTTPStatus.UNAUTHORIZED,
        )


class AuthorizationException(ApplicationException):
    def __init__(self, message: str = "Permission denied") -> None:
        super().__init__(
            message=message,
            error_code="AUTHORIZATION_ERROR",
            status_code=HTTPStatus.FORBIDDEN,
        )


class ResourceNotFoundException(ApplicationException):
    def __init__(self, resource: str):
        super().__init__(
            message=f"{resource} not found.",
            error_code="RESOURCE_NOT_FOUND",
            status_code=HTTPStatus.NOT_FOUND,
        )


class DatabaseException(ApplicationException):
    def __init__(self) -> None:
        super().__init__(
            message="Database operation failed.",
            error_code="DATABASE_ERROR",
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        )


class ExternalServiceException(ApplicationException):
    def __init__(self, service: str) -> None:
        super().__init__(
            message=f"{service} is currently unavailable.",
            error_code="EXTERNAL_SERVICE_ERROR",
            status_code=HTTPStatus.BAD_GATEWAY,
        )
