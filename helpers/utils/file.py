def abs_path_from_project(relative_path: str):
    import helpers
    from pathlib import Path

    return (
        Path(helpers.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
