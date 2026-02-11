# BiteBook Application

**Your personal command-line recipe manager**

BiteBook is a recipe catalog application that lets you store, view, search, and manage all your favorite recipes directly from the terminal.

## ✨ Features

- **📋 View Catalog** - Browse all your recipes
- **🔍 Search Recipes** - Find recipes by name
- **➕ Add Recipes** - Save new recipes with ingredients & instructions
- **🗑️ Delete Recipes** - Remove recipes you no longer need
- **🔧 Unit Converter** - Convert cooking measurements (oz, cups, tbsp, etc.)

## ✨ Architecture

Built with **ZeroMQ microservices** - each feature runs on its own dedicated port.

| Service | File | Port |
|---------|------|------|
| View Catalog | `view_catalog_service.py` | 4680 |
| View Recipe | `view_recipe_service.py` | 4682 |
| Add Recipe | `add_recipe_service.py` | 8648 |
| Delete Recipe | `delete_recipe_service.py` | 4694 |
| Search Recipe | `search_recipe_service.py` | 7645 |
| Unit Converter | `convert_service.py` | 4600 |

## ✨ Quick Start

### 1. Install dependencies
```pip install -r requirements.txt```

### 2. Run All Servers
```python add_recipe_service.py```

```python convert_service.py```

```python delete_recipe_service.py```

```python search_recipe_service.py```

```python view_catalog_service.py```

```python view_recipe_service.py```

### 3. Run Main
```python main.py```

## ⚠️ Important Notes
- All 6 servers must be running before starting main.py