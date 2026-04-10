"""Jerarquia de excepciones controladas de la aplicacion.

Estas clases permiten que la GUI capture errores del dominio y muestre
mensajes consistentes sin depender de excepciones genericas.
"""

from __future__ import annotations


class AppError(Exception):
    """Clase base para errores controlados de la aplicacion."""


class ValidationError(AppError):
    """Agrupa errores relacionados con datos o entradas invalidas."""


class MissingFileError(ValidationError):
    """Se usa cuando el usuario aun no ha indicado un archivo necesario."""


class EmptyFileError(ValidationError):
    """Se usa cuando el archivo existe, pero no aporta datos procesables."""


class MissingTargetFormatError(ValidationError):
    """Se usa cuando el formato de salida aun no fue seleccionado."""


class UnsupportedFormatError(AppError):
    """Se usa cuando la extension o formato solicitado no esta registrado."""


class ConversionError(AppError):
    """Error base para fallos ocurridos durante una conversion."""


class ReadError(ConversionError):
    """Representa un fallo controlado al leer un archivo de entrada."""


class WriteError(ConversionError):
    """Representa un fallo controlado al guardar un archivo de salida."""


class PreviewError(AppError):
    """Se usa cuando la aplicacion no puede construir la vista previa."""


class PendingConversionError(AppError):
    """Se usa al intentar guardar sin haber preparado una conversion antes."""
