marked_students = set()

def should_mark_attendance(name):
    """
    Runtime me duplicate attendance rokta hai
    """
    if name in marked_students:
        return False
    marked_students.add(name)
    return True
