def angle_type(angle):
    if angle == 180:
        return "Semicircle"
    elif angle == 360:
        return "Circle"
    elif 0 < angle < 180:
        return "Chord"
    else:
        return "Invalid angle"

angle = float(input("Enter the angle in degrees: "))
print("Angle type:", angle_type(angle))
