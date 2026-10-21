import cv2

cap = cv2.VideoCapture(0)
mode = "CYAN"

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(blur, 50, 150)

    black = edges * 0 
    if mode == "CYAN":
        neon_lines = cv2.merge([edges, edges, black])
    elif mode == "RED":
        neon_lines = cv2.merge([black, black, edges])
    elif mode == "GREEN":
        neon_lines = cv2.merge([black, edges, edges])


    glow = cv2.GaussianBlur(neon_lines, (15,15), 0)


    neon_filter = cv2.addWeighted(frame, 0.2, glow, 2.5, 0)
    neon_filter = cv2.add(neon_filter, neon_lines)

    cv2.putText(neon_filter, f"COLOUR: {mode} , PRESS 1:CYAN, 2 : RED, 3:GREEN  AND Q:QUIT IF YOU ARE READY "
                , (15,35), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255,255,255),2)
    cv2.imshow("cyberpunk neon filter!!", neon_filter)


    key = cv2.waitKey(20) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("1"):
        mode = "CYAN"
    elif key == ord("2"):
        mode = "RED"
    elif key == ord("3"):
        mode = "GREEN"

cap.release()
cv2.destroyAllWindows()



        
