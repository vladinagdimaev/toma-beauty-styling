from pathlib import Path

# Pelican loads this file directly, so do not rely on the repository root
# being present on sys.path. Load the base config by file path instead.
_base_config = Path(__file__).with_name("pelicanconf.py")
exec(
    compile(
        _base_config.read_text(encoding="utf-8"),
        str(_base_config),
        "exec",
    ),
    globals(),
)

SITEURL = ""
RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True
