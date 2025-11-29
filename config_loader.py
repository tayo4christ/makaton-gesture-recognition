from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class CameraConfig:
    index: int = 0


@dataclass
class GUIConfig:
    refresh_ms: int = 10


@dataclass
class GestureThresholds:
    hello_min_distance: float = 0.2
    goodbye_max_distance: float = 0.1


@dataclass
class LoggingConfig:
    level: str = "INFO"


@dataclass
class AppConfig:
    camera: CameraConfig = field(default_factory=CameraConfig)
    gui: GUIConfig = field(default_factory=GUIConfig)
    gesture_thresholds: GestureThresholds = field(default_factory=GestureThresholds)
    logging: LoggingConfig = field(default_factory=LoggingConfig)


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        logging.warning("Config file %s not found. Using default settings.", path)
        return {}
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        logging.warning(
            "Config file %s has unexpected structure. Using defaults.", path
        )
        return {}
    return data


def load_config(path: str | Path = "config.yaml") -> AppConfig:
    """
    Load application configuration from a YAML file.

    Missing fields fall back to sensible defaults.
    """
    path_obj = Path(path)
    raw = _load_yaml(path_obj)

    camera = CameraConfig(**(raw.get("camera") or {}))
    gui = GUIConfig(**(raw.get("gui") or {}))
    thresholds = GestureThresholds(**(raw.get("gesture_thresholds") or {}))
    logging_cfg = LoggingConfig(**(raw.get("logging") or {}))

    return AppConfig(
        camera=camera,
        gui=gui,
        gesture_thresholds=thresholds,
        logging=logging_cfg,
    )
