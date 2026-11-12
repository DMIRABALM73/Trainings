def build_study_plan(name: str, hours_per_week: int) -> str:
    """Return a personalized study plan message."""
    # TODO: update message format as part of exercises.
    return f"{name}, keep a {hours_per_week}-hour weekly practice routine."


if __name__ == "__main__":
    print(build_study_plan("Student", 5))
