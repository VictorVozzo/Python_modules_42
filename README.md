# Python Modules 42

![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)
![Code style](https://img.shields.io/badge/code%20style-flake8-informational)
![Type checking](https://img.shields.io/badge/type%20checking-mypy-informational)
![School](https://img.shields.io/badge/42-Porto-black)

My solutions to the **Python modules (00 – 10)** of the 42 curriculum, completed at **42 Porto**.

Each module is a themed project (gardens, game data, archives, alchemy, creature cards, the Matrix, space stations, mages…) that introduces a new part of Python, from basic syntax to object-oriented design, packages, data validation and functional programming.



---

## Table of contents

- [Overview](#overview)
- [Repository structure](#repository-structure)
- [Requirements](#requirements)
- [How to run](#how-to-run)
- [Modules](#modules)
- [Code quality](#code-quality)
- [Author](#author)

---

## Overview

| Module | Project | Main topics |
|:------:|---------|-------------|
| [00](#module-00--growing-code) | **Growing Code** | Syntax, variables, functions, control flow, recursion, type hints |
| [01](#module-01--code-cultivation) | **Code Cultivation** | Classes, encapsulation, class/static methods, inheritance |
| [02](#module-02--garden-guardian) | **Garden Guardian** | Exceptions, `try/except/finally`, custom errors |
| [03](#module-03--data-quest) | **Data Quest** | Lists, tuples, dicts, sets, comprehensions, generators |
| [04](#module-04--data-archivist) | **Data Archivist** | File I/O, context managers, `stdin`/`stdout`/`stderr` |
| [05](#module-05--code-nexus) | **Code Nexus** | Abstract classes, polymorphism, method overriding, duck typing |
| [06](#module-06--the-codex) | **The Codex** | Packages, `__init__.py`, absolute/relative imports, circular imports |
| [07](#module-07--datadeck) | **DataDeck** | Abstract Factory, Strategy pattern, interfaces/capabilities |
| [08](#module-08--the-matrix) | **The Matrix** | Virtual environments, `pip` vs Poetry, environment variables |
| [09](#module-09--cosmic-data) | **Cosmic Data** | Pydantic v2 models, custom validation, nested models |
| [10](#module-10--funcmage) | **FuncMage** | Lambdas, higher-order functions, closures/scope, `functools`, decorators |

---

## Repository structure

Every module folder contains the solution files for its exercises.

```
Python_modules_42/
├── Python_Module_00/      # Growing Code
│   └── ex0/ … ex7/
├── Python_Module_01/      # Code Cultivation
│   └── ex0/ … ex6/
├── Python_Module_02/      # Garden Guardian
│   └── ex0/ … ex4/
├── Python_Module_03/      # Data Quest
│   └── ex0/ … ex6/
├── Python_Module_04/      # Data Archivist
│   └── ex0/ … ex3/
├── Python_Module_05/      # Code Nexus
│   └── ex0/ … ex2/
├── Python_Module_06/      # The Codex
│   ├── alchemy/           # the package (with grimoire/ and transmutation/ sub-packages)
│   ├── elements.py
│   └── ft_alembic_*.py, ft_distillation_*.py, ft_transmutation_*.py, ft_kaboom_*.py
├── Python_Module_07/      # DataDeck
│   ├── ex0/ ex1/ ex2/     # packages: factories, capabilities, strategies
│   └── battle.py, capacitor.py, tournament.py
├── Python_Module_08/      # The Matrix
│   └── ex0/ ex1/ ex2/
├── Python_Module_09/      # Cosmic Data
│   └── ex0/ ex1/ ex2/
└── Python_Module_10/      # FuncMage
    └── ex0/ … ex4/
```

---

## Requirements

- **Python 3.10+**
- `flake8` and `mypy` (for linting and type checking)
- Module-specific dependencies:

| Module | Dependencies |
|:------:|--------------|
| 08 – ex1 | `pandas`, `numpy`, `matplotlib` (via `requirements.txt` or `pyproject.toml`) |
| 08 – ex2 | `python-dotenv` |
| 09 | `pydantic` 2.x |

Quick setup (recommended, inside a virtual environment):

```bash
git clone <your-repo-url>
cd Python_modules_42

python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install flake8 mypy pydantic python-dotenv
```

---

## How to run

Most exercises are standalone scripts. Run them from the exercise (or module) folder:

```bash
# Modules 00–05, 09, 10
cd Python_Module_00/ex0
python3 ft_hello_garden.py
```

Modules with packages must be run **from the module root**, so imports resolve correctly:

```bash
# Module 06 – import experiments
cd Python_Module_06
python3 ft_alembic_0.py
python3 ft_kaboom_1.py

# Module 07 – DataDeck
cd Python_Module_07
python3 battle.py
python3 capacitor.py
python3 tournament.py
```

---

## Modules

### Module 00 – Growing Code
*Python fundamentals through garden data.*

| Ex | File(s) | Concept |
|:--:|---------|---------|
| 0 | `ft_hello_garden.py` | First function and output |
| 1 | `ft_garden_name.py` | Variables and string formatting |
| 2 | `ft_plot_area.py` | Arithmetic expressions |
| 3 | `ft_harvest_total.py` | Input and sums |
| 4 | `ft_plant_age.py` | Conditionals |
| 5 | `ft_water_reminder.py` | Conditionals and thresholds |
| 6 | `ft_count_harvest_iterative.py`, `ft_count_harvest_recursive.py` | Loops vs. recursion |
| 7 | `ft_seed_inventory.py` | Type annotations |

### Module 01 – Code Cultivation
*Object-oriented garden systems.*

| Ex | File | Concept |
|:--:|------|---------|
| 0 | `ft_garden_intro.py` | Your first class |
| 1 | `ft_garden_data.py` | Organizing data in objects |
| 2 | `ft_plant_growth.py` | Methods and state changes |
| 3 | `ft_plant_factory.py` | Object creation / factory approach |
| 4 | `ft_garden_security.py` | Encapsulation and validation |
| 5 | `ft_plant_types.py` | Inheritance and specialized plants |
| 6 | `ft_garden_analytics.py` | Putting it all together |

### Module 02 – Garden Guardian
*Resilient data pipelines with exception handling.*

| Ex | File | Concept |
|:--:|------|---------|
| 0 | `ft_first_exception.py` | `try` / `except` |
| 1 | `ft_raise_exception.py` | Raising exceptions |
| 2 | `ft_different_errors.py` | Handling different error types |
| 3 | `ft_custom_errors.py` | Custom exception classes |
| 4 | `ft_finally_block.py` | `finally` and cleanup |

### Module 03 – Data Quest
*Mastering Python collections with game data.*

| Ex | File | Concept |
|:--:|------|---------|
| 0 | `ft_command_quest.py` | Command-line arguments (`sys.argv`) |
| 1 | `ft_score_analytics.py` | Lists and statistics |
| 2 | `ft_coordinate_system.py` | Tuples |
| 3 | `ft_achievement_tracker.py` | Sets |
| 4 | `ft_inventory_system.py` | Dictionaries |
| 5 | `ft_data_stream.py` | Generators |
| 6 | `ft_data_alchemist.py` | Comprehensions |

### Module 04 – Data Archivist
*File operations and data streams.*

| Ex | File | Concept |
|:--:|------|---------|
| 0 | `ft_ancient_text.py` | Reading files |
| 1 | `ft_archive_creation.py` | Writing files |
| 2 | `ft_stream_management.py` | `stdin`, `stdout`, `stderr` |
| 3 | `ft_vault_security.py` | Context managers (`with`) and safe file access |

### Module 05 – Code Nexus
*Polymorphic data streams.*

| Ex | File | Concept |
|:--:|------|---------|
| 0 | `data_processor.py` | Abstract base classes (`abc`) |
| 1 | `data_stream.py` | Polymorphic processing of a data stream |
| 2 | `data_pipeline.py` | Pipelines with duck typing |

### Module 06 – The Codex
*The four mysteries of Python imports.*

- **Part I – The Alembic** (`ft_alembic_0…5.py`): `import x`, `from x import y`, package access and partial imports.
- **Part II – Distillation** (`ft_distillation_0…1.py`): package initialization and `__all__`.
- **Part III – The Great Transmutation** (`ft_transmutation_0…2.py`): absolute vs. relative imports.
- **Part IV – Avoid the Explosion** (`ft_kaboom_0…1.py`): breaking circular dependencies.

The `alchemy/` package contains the `elements`, `potions` modules and the `grimoire` (light/dark spellbooks and validators) and `transmutation` (recipes) sub-packages.

### Module 07 – DataDeck
*Abstract card architecture.*

| Ex | Package | Concept |
|:--:|---------|---------|
| 0 | `ex0/` + `battle.py` | **Abstract Factory**: families of creatures (e.g. Flameling / Aquabub) |
| 1 | `ex1/` + `capacitor.py` | **Capabilities**: healing and transforming creatures via interfaces |
| 2 | `ex2/` + `tournament.py` | **Strategy pattern**: Normal, Aggressive and Defensive battle strategies |

### Module 08 – The Matrix
*Virtual environments, dependencies and configuration.*

| Ex | File(s) | Concept |
|:--:|---------|---------|
| 0 | `construct.py` | Detects whether you are inside a virtual environment |
| 1 | `loading.py`, `requirements.txt`, `pyproject.toml` | `pip` vs. **Poetry** dependency management |
| 2 | `oracle.py`, `.env.example`, `.gitignore` | Environment variables with `.env` / `python-dotenv` |

```bash
# ex0
python3 -m venv matrix_env
source matrix_env/bin/activate
python3 ex0/construct.py

# ex1 – pip
pip install -r ex1/requirements.txt
python3 ex1/loading.py

# ex1 – Poetry
cd ex1 && poetry install && poetry run python loading.py

# ex2
cp ex2/.env.example ex2/.env      # then edit your values
python3 ex2/oracle.py
```

> `.env` files and virtual environments are **not** versioned. Use `.env.example` as a template.

### Module 09 – Cosmic Data
*Pydantic v2 models and validation.*

| Ex | File | Concept |
|:--:|------|---------|
| 0 | `space_station.py` | `BaseModel`, `Field` constraints |
| 1 | `alien_contact.py` | `Enum`, `@model_validator`, custom rules |
| 2 | `space_crew.py` | Nested models and business-rule validation |

### Module 10 – FuncMage
*Functional programming.*

| Ex | File | Concept |
|:--:|------|---------|
| 0 | `lambda_spells.py` | Lambda functions |
| 1 | `higher_magic.py` | Higher-order functions (`map`, `filter`, `sorted`…) |
| 2 | `scope_mysteries.py` | Closures, `nonlocal`, lexical scope |
| 3 | `functools_artifacts.py` | `functools` and `operator` |
| 4 | `decorator_mastery.py` | Decorators |

---

## Code quality

All projects follow the 42 requirements for the Python modules:

- Python **3.10+**
- **flake8** compliant
- Type annotations checked with **mypy** (from the modules that require it)

```bash
flake8 .
mypy .
```

> Module 08 – ex1 is explicitly exempted from flake8/mypy errors in the project requirements.

---

## Author

**Victor Vozzo Telles** (`vivozzo-`) – 42 Porto

- GitHub: [@VictorVozzo](https://github.com/VictorVozzo)
