# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  loading.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/21 18:18:55 by laveerka        #+#    #+#               #
#  Updated: 2026/11/07 02:03:50 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
from typing import Any
from types import ModuleType
from importlib import import_module
from importlib.metadata import version, PackageNotFoundError


def build_version_string(version_info: str | None) -> str | None:
    version_string  = ""
    digit = False
    dot = False
    if version_info:
        for char in version_info:
            if char.isdigit() and not dot:
                digit = True
                version_string +=  char
            elif char.isdigit() and dot:
                digit = True
                dot = False
                version_string += "." + char
            elif char == "." and digit:
                dot = True
                digit = False
            else:
                if digit or dot:
                    break
        if len(version_string) > 0:
            return version_string
    return None


def compare_versions(required_version: str, installed_version: str) -> bool:
    required = tuple(map(int, required_version.split(".")))
    clean = tuple(map(int, installed_version.split(".")))
    length = max(len(required), len(clean))
    required = required + (0,) * (length - len(required))
    clean = clean + (0,) * (length - len(clean))
    return clean >= required  


def check_requirements() -> dict[str, str | None] | None:
    requirements: dict[str, str | None] | None = {}
    with open("requirements.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if ">=" in line:
                package, required_version = line.split(">=", 1)
                if package and required_version:
                    version_string = build_version_string(required_version)
                    if version_string:
                        requirements[package.strip()] = version_string
                    else:
                        requirements[package.strip()] = None
                elif package and not required_version:
                    requirements[package.strip()] = None
            elif line:
                requirements[line] = None
    if requirements:
        return requirements
    else:
        return None


def check_dependencies() -> list[tuple[str, str]]:
    required: dict[str, str | None] | None =  check_requirements()
    missing: list[tuple[str, str | None]] = []
    wrong_version: list[tuple[str, str, str]] = []
    present: list[tuple[str, str]] = []
    missing_count = 0
    version_count = 0
    if required:
        for package, required_version in required.items():
            if package:
                try:
                    installed_version = version(package)
                    clean_installed = build_version_string(installed_version)
                    if required_version and clean_installed:
                        comparison = compare_versions(required_version, clean_installed)
                        if comparison:
                            present.append((package, clean_installed))
                        else:
                            version_count += 1
                            wrong_version.append((package, required_version, clean_installed))
                    elif clean_installed:
                        present.append((package, clean_installed))
                except PackageNotFoundError:
                    missing_count += 1
                    missing.append((package, required_version))
    if missing:
        if missing_count == 1:
            print(f"\nYou have {missing_count} missing dependency")
        elif missing_count > 1:
            print(f"\nYou have {missing_count} missing dependendies")
        for package, required_version in missing:
            if required_version:
                print(f"- {package} version {required_version} is missing")
            else:
                print(f"- {package} is missing, no required version is specified")
    if wrong_version:
        if version_count == 1:
            print(f"\nYou have {version_count} dependency which version is inadequate")
        elif version_count > 1:
            print(f"\nYou have {version_count} dependencies which version is inadequate")
        for package, required_version, installed in wrong_version:
            print(f"- {package} has version {installed} installed, whereas it needs version {required_version}")
    if missing or wrong_version:
        print("\nTo satisfy the dependency requirements")
        print("\n* with pip\n")
        print("  create the virtual environment")
        print("   - python3 -m venv matrix_env")
        print("  activate it with")
        if "linux" in sys.platform.lower():
            print("   - source matrix_env/bin/activate")
        elif "win" in sys.platform.lower():
            print("   - matrix_env\\Scripts\\activate\n")
        print("  install requirements")
        print("   - pip install -r requirements.txt")
        print("  run the code")
        print("   - python3 loading.py")
        print("\n* with poetry\n")
        print("  install requirements")
        print("   - poetry install")
        print("  run the code")
        print("   - poetry run python3 loading.py")
        sys.exit(1)
    return present


def dependency_info(packages: list[tuple[str, str]]) -> None:
    print("Checking dependencies:")
    for package, installed in packages:
        print(f"[OK] {package} ({installed})", end="")
        if package == "pandas":
            print(" - Data manipulation ready")
        elif package == "numpy":
            print(" - Numerical computation ready")
        elif package == "matplotlib":
            print(" - Visualization ready")


def import_modules(packages: list[tuple[str, str]]) -> dict[str, ModuleType]:
    imported: dict[str, ModuleType] = {}
    for package, installed in packages:
        try:
            if package == "matplotlib":
                package += ".pyplot"
            module = import_module(package)
            imported[package] = module
        except ImportError:
            print(f"Unable to import dependency {package} of version {installed}")
    if len(packages) != len(imported):
        print("\nMake sure to install all dependencies with either pip or poetry")
        sys.exit(1)
    return imported


def generate_data(np: ModuleType, data_points: int) -> Any:
    rng = np.random.default_rng()
    size_m2 = rng.uniform(20, 60, size=data_points)
    age_years = rng.integers(1, 101, size=data_points)
    price_noise = rng.normal(0, 25_000, size=data_points)
    price = (35_0000 + size_m2 * 3_500 + age_years * 1_200 + price_noise)
    return np.column_stack((size_m2, age_years, price))


def data_manipulation(pd: ModuleType, data: Any) -> Any:
    print("\nAnalyzing Matrix data...")
    print(f"Processing {data.shape[0]} data points...")
    df = pd.DataFrame(
        data,
        columns=["size_m2", "age_years", "price"]
    )
    return df


def create_visualization(plt: ModuleType, df: Any, filename: str) -> None:
    print("Generating visualization...\n")
    fig: Any = plt.figure(figsize=(10, 7))
    ax: Any = fig.add_subplot(111, projection="3d") # type: ignore[reportUnknownMemberType]
    scatter = ax.scatter( # type: ignore[reportUnknownMemberType]
        df["size_m2"],
        df["age_years"],
        df["price"],
        c=df["price"],
        cmap="viridis",
        alpha=0.7
    )
    ax.set_xlabel("House size (m²)")
    ax.set_ylabel("House age (years)")
    ax.set_zlabel("Price (€)")
    ax.set_title("House Price Analysis")
    fig.colorbar(scatter, ax=ax, label="Price (€)", pad=0.12)
    fig.tight_layout()
    fig.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    packages: list[tuple[str, str]] = check_dependencies()
    imported: dict[str, ModuleType] = import_modules(packages)
    np = imported["numpy"]
    pd = imported["pandas"]
    plt = imported["matplotlib.pyplot"]
    if packages and all(package and installed for package, installed in packages):
        print("\nLOADING STATUS: Loading programs...\n")
        dependency_info(packages)
        filename = "matrix_analysis.png"
        data_points = 1000
        data = generate_data(np, data_points)
        dataframe = data_manipulation(pd, data)
        create_visualization(plt, dataframe, filename)
        print("Analysis complete!")
        print(f"Results saved to: {filename}")


if __name__ == "__main__":
    main()
