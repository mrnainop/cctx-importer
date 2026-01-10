# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def get_current_context() -> str | None:
    result = subprocess.run(["cctx", "-c"], capture_output=True, text=True)
    if result.returncode == 0 and result.stdout.strip():
        return result.stdout.strip()
    return None


def load_default_config(configs_dir: Path) -> dict[str, Any]:
    default_path = configs_dir / "default.json"
    if default_path.exists():
        return json.loads(default_path.read_text())
    return {}


def unset_context(context: str) -> None:
    print(f"Unsetting active context {context}")
    subprocess.run(["cctx", "-u"], capture_output=True, text=True)


def restore_context(context: str) -> None:
    print(f"Restoring context {context}")
    subprocess.run(["cctx", context], capture_output=True)


def import_profile(profile_name: str, merged: dict[str, Any]) -> bool:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp:
        json.dump(merged, tmp, indent=2)
        tmp_path = tmp.name
    try:
        subprocess.run(["cctx", "-d", profile_name], capture_output=True, text=True)
        with open(tmp_path, "r") as f:
            result = subprocess.run(
                ["cctx", "--import", profile_name],
                stdin=f,
                capture_output=True,
                text=True,
            )
        if result.returncode != 0:
            print(f"Error processing {profile_name}: {result.stderr}", file=sys.stderr)
            return False
        print(f"Processed {profile_name}")
        return True
    finally:
        Path(tmp_path).unlink()


def process_profile(
    config_path: Path,
    default_config: dict[str, Any],
    current_context: str | None,
) -> None:
    profile_name = config_path.stem
    config = json.loads(config_path.read_text())
    if config_path.name == "default.json":
        merged = config
    else:
        merged = deep_merge(default_config, config)
    if current_context is not None and current_context == profile_name:
        unset_context(current_context)
    import_profile(profile_name, merged)


def main() -> None:
    configs_dir = Path(__file__).parent / "configs"
    default_config = load_default_config(configs_dir)
    current_context = get_current_context()
    for config_path in configs_dir.glob("*.json"):
        process_profile(config_path, default_config, current_context)
    if current_context:
        restore_context(current_context)


if __name__ == "__main__":
    main()
