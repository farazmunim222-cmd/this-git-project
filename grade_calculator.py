def get_grade(mark):
    if mark is None:
        raise TypeError("Mark cannot be None")

    if not isinstance(mark, (int, float)) or isinstance(mark, bool):
        raise TypeError("Mark must be a number")

    if mark < 0 or mark > 100:
        raise ValueError("Mark must be between 0 and 100")

    if mark >= 80:
        return 'A+'
    elif mark >= 70:
        return 'A'
    elif mark >= 60:
        return 'A-'
    elif mark >= 50:
        return 'B'
    elif mark >= 40:
        return 'C'
    else:
        return 'F'

