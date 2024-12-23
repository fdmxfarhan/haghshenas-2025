from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
from math import *

class MyRobot1(RCJSoccerRobot):
    def motor(self, vl, vr):
        self.left_motor.setVelocity(vl)
        self.right_motor.setVelocity(vr)
    def run(self):
        xb = 0
        yb = 0
        while self.robot.step(TIME_STEP) != -1: # تا زمانی که بازی در حال اجراست
            if self.is_new_data(): # اگر دیتای جدیدی آماده خواندن بود
                gps = self.get_gps_coordinates()
                heading = degrees(self.get_compass_heading())
                xr = gps[0]
                yr = gps[1]
                if self.is_new_ball_data():
                    self.is_ball = True
                    ball_data = self.get_new_ball_data()
                    ball_angle = degrees(atan2(ball_data['direction'][1], ball_data['direction'][0]))
                    ball_distance = abs(0.01666666/(abs(ball_data['direction'][2])/sqrt(1 - ball_data['direction'][2]**2)))
                    xb = -sin(radians(ball_angle + heading)) * ball_distance + xr
                    yb =  cos(radians(ball_angle + heading)) * ball_distance + yr
                xt = xb
                yt = yb
                at = degrees(atan2(xr - xt, yt - yr))
                e = at - heading
                if e > 10:
                    self.motor(10, -10)
                elif e < -10:
                    self.motor(-10, 10)
                else:
                    self.motor(10,10)
                    
                