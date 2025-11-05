import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


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


if __name__ == "__main__":
    app.run()
