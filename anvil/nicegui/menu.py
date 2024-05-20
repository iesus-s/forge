import pandas
import toml
from nicegui import ui
from importlib.metadata import version
from utils.helper import get_project_root


def load_pyproject_toml() -> str:
    project_root = get_project_root().parent
    pyproject_file = toml.load(f"{project_root}/pyproject.toml")
    return pyproject_file


def get_project_version() -> str:
    pyproject_file = load_pyproject_toml()
    project_version = pyproject_file["tool"]["poetry"]["version"]
    return project_version


def get_python_package_version() -> pandas.DataFrame:
    pyproject_file = load_pyproject_toml()
    python_packages = pyproject_file["tool"]["poetry"]["dependencies"]
    python_packages_data = []
    for key, value in python_packages.items():
        # Skip python itself
        if key == "python":
            continue
        get_version = version(key)
        python_packages_data.append({"Package": key, "Version": get_version})
    python_packages_version = pandas.DataFrame(data=python_packages_data).sort_values(
        by="Package"
    )
    return python_packages_version


def get_about(dialog) -> None:
    project_version = get_project_version()
    python_packages_versions = get_python_package_version()
    with ui.column().classes("items-center"):
        ui.label("uBlue-OS Forge").classes("text-h5")
        ui.label(f"v{project_version}").classes("text-h6")
        ui.table.from_pandas(df=python_packages_versions)
        ui.button("Close", on_click=dialog.close)


def menu() -> None:
    with ui.button(icon="menu"):
        with ui.menu().props("auto-close"):
            ui.menu_item("Home", lambda: ui.navigate.to(target="/"))
            ui.menu_item("Ansible", lambda: ui.navigate.to(target="/ansible"))
            ui.menu_item("Registry", lambda: ui.navigate.to(target="/registry"))
            ui.menu_item("About", lambda: dialog.open())

    with ui.dialog() as dialog, ui.card():
        get_about(dialog)
