"""Tests for public application metadata."""

from src.utils.constants import APP_LAST_UPDATED, APP_VERSION


def test_public_release_metadata_matches_semver_reset() -> None:
    """The public release must expose the version and date documented for 1.0.0."""

    assert APP_VERSION == "1.0.0"
    assert APP_LAST_UPDATED == "2026-06-10"
