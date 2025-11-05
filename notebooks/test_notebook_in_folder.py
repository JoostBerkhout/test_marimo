import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium", auto_download=["html", "ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This file can also be opened in molab which requires to first install pyjobshop, which takes around 50 seconds.
    [![Open in molab](https://molab.marimo.io/molab-shield.png)](https://molab.marimo.io/notebooks/nb_UJ5NfkajNLCnUFn8SBMe5b)
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    a = 10
    return


@app.cell
def _():
    b = 10
    return


@app.cell
def _():
    from pyjobshop import Model

    model = Model()

    jobs = [model.add_job() for _ in range(4)]
    tasks = [[model.add_task(job=job) for _ in range(2)] for job in jobs]
    machines = [model.add_machine() for _ in range(2)]

    for j in range(len(jobs)):
        for t in tasks[j]:
            for m in machines:
                duration = j + 1
                model.add_mode(t, m, duration)
    return (model,)


@app.cell
def _(model):
    result = model.solve(display=False)
    result.status
    return (result,)


@app.cell
def _(result):
    for task in result.best.tasks:
        print(task)
    return


@app.cell
def _():
    print("Hoi Joost")
    return


@app.cell
def _():
    print("Als het goed is wordt nu ook een html opgeslagen.")
    return


@app.cell
def _():
    print("Nieuwe stukje tekst om te checken of dit wordt opgeslagen.")
    return


if __name__ == "__main__":
    app.run()
