from __future__ import annotations


class AppError(Exception):
    """Error base de la aplicacion."""


class ValidationError(AppError):
    """Error de validacion de entradas."""


class UnsupportedFormatError(AppError):
    """Se lanza cuando el formato no es soportado."""


class ConversionError(AppError):
    """Se lanza cuando la conversion falla."""


class PreviewError(AppError):
    """Se lanza cuando no es posible generar la previsualizacion."""


class PendingConversionError(AppError):
    """Se lanza cuando se intenta guardar sin una conversion preparada."""
