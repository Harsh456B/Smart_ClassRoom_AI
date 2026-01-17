# ist lgic 
# from datetime import datetime

# CLASS_START_TIME = "10:00"   # apni class timing yahan set karo

# def is_late():
#     current_time = datetime.now().strftime("%H:%M")
#     return current_time > CLASS_START_TIME

# 2nd logic 

# first_marked = False

# def is_late():
#     global first_marked
#     if not first_marked:
#         first_marked = True
#         return False   # First student always on-time
#     return True

# 3rd logic 

from datetime import datetime, timedelta

CLASS_START_TIME = "10:00"
GRACE_MINUTES = 10   # 10 min allowed

def is_late():
    now = datetime.now()

    class_time = datetime.strptime(CLASS_START_TIME, "%H:%M")
    class_time = now.replace(
        hour=class_time.hour,
        minute=class_time.minute,
        second=0
    )

    grace_time = class_time + timedelta(minutes=GRACE_MINUTES)

    return now > grace_time




