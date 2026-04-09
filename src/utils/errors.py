from __future__ import annotations


class AppError(Exception):
    """Error base de la aplicacion."""


class ValidationError(AppError):
    """Error de validacion de entradas."""


class MissingFileError(ValidationError):
    """Se lanza cuando no se ha indicado un archivo requerido."""


class EmptyFileError(ValidationError):
    """Se lanza cuando el archivo existe pero no contiene datos utiles."""


class MissingTargetFormatError(ValidationError):
    """Se lanza cuando no se ha seleccionado un formato de salida."""


class UnsupportedFormatError(AppError):
    """Se lanza cuando el formato no es soportado."""


class ConversionError(AppError):
    """Se lanza cuando la conversion falla."""


class ReadError(ConversionError):
    """Se lanza cuando un archivo no puede leerse correctamente."""


class WriteError(ConversionError):
    """Se lanza cuando un archivo no puede escribirse correctamente."""


class PreviewError(AppError):
    """Se lanza cuando no es posible generar la previsualizacion."""


class PendingConversionError(AppError):
    """Se lanza cuando se intenta guardar sin una conversion preparada."""
