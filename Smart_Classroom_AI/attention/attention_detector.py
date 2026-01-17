def detect_attention(face_x, face_y, face_w, face_h, frame_w, frame_h):
    """
    Simple Attention Detection
    --------------------------
    Returns: "Focused" or "Not Focused"
    """

    # Face center
    face_center_x = face_x + face_w // 2
    face_center_y = face_y + face_h // 2

    # Frame center
    frame_center_x = frame_w // 2
    frame_center_y = frame_h // 2

    # Allowable focus region (center 40%)
    x_min = frame_center_x * 0.6
    x_max = frame_center_x * 1.4
    y_min = frame_center_y * 0.6
    y_max = frame_center_y * 1.4

    if x_min <= face_center_x <= x_max and y_min <= face_center_y <= y_max:
        return "Focused"
    else:
        return "Not Focused"
