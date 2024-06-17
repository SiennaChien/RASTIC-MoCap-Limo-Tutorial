import time
from cav_for_line_follower import CAV

#helper function to get equation of a line in the form Ax + By + C = 0
def line_coef(x1, x2, y1, y2):
    A = y1-y2
    B = x2-x1
    C = x1*y2-x2*y1
    return A, B, C

def main():
    #creating cav object for the limo, setting PID values
    limo = CAV("limo770")
    eprev_lateral = 0
    eint_lateral = 0
    dt = 0.1
    e = 0
    transmissionRate = 30
    dt = 1/transmissionRate
    vel = 0.5 #velocity of limo

    #the two points that define the line to travel on
    p1_x = 3044
    p1_y = 2536

    p2_x = 683
    p2_y = 2536
    
    #calculates equation of line
    [A,B,C] = line_coef(p1_x,p2_x,p1_y,p2_y)

    while True:
        if limo.position_x > 3200 or limo.position_x < -4900 or limo.position_z > 2600 or limo.position_z < -1800: 
            print("Limo out of range of motion capture system, setting velocity to 0")
            vel = 0

        #calculate error (distance from limo to line), get steering, publish steering and velocity information to limo
        e = -(A*limo.position_x + B*limo.position_z + C)/((A**2 + B**2)**0.5)
        eprev_lateral, eint_lateral, limo_drive_msg = limo.control(e, vel, eprev_lateral, eint_lateral, dt)
        limo.pub.publish(limo_drive_msg)

        time.sleep(dt)

if __name__ == '__main__':
    main()
