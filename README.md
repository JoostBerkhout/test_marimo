# test_marimo

This project explores how to integrate **Marimo notebooks** into an **MkDocs** documentation site.

The goal is to make Marimo notebooks viewable directly in the published documentation while keeping their interactive versions available on **molab**.

## Workflow (Current Routine)

1. **Create or edit notebooks using** `marimo edit`.
2. Configure Marimo to **automatically export an `.html` copy** of each notebook when saving.  
   See: https://docs.marimo.io/guides/exporting/#export-from-a-running-notebook  
   → This places the exported HTML in a `__marimo__` folder next to the notebook.
3. Store your notebooks in: `docs/notebooks/`  
   Since this folder is part of the MkDocs documentation tree, the exported HTML is **included automatically**—no manual copying required.
4. To include a **header link back to the interactive notebook on molab**, use the **copy notebook link** button in molab.

## Embedding in MkDocs

Create or edit a page such as `docs/examples.md`:

```markdown
# Examples

## Notebook Example

<iframe src="/notebooks/test_notebook_in_folder.html" width="100%" height="800px"></iframe>
