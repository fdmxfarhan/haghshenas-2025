import math
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
from math import *

class MyRobot3(RCJSoccerRobot):
    def readData(self):
        gps = self.get_gps_coordinates() # خواندن سنسور GPS
        self.heading = degrees(self.get_compass_heading()) # خواندن سنسور قطب نما
        self.xr = gps[0] # x robot
        self.yr = gps[1] # y robot
        if self.is_new_ball_data():
            self.is_ball = True
            ball_data = self.get_new_ball_data()
            ball_angle = degrees(atan2(ball_data['direction'][1], ball_data['direction'][0]))
            ball_distance = abs(0.01666666/(abs(ball_data['direction'][2])/sqrt(1 - ball_data['direction'][2]**2)))
            self.xb = -sin(radians(ball_angle + self.heading)) * ball_distance + self.xr # x toop
            self.yb =  cos(radians(ball_angle + self.heading)) * ball_distance + self.yr # y toop

            self.is_ball = True
        else:
            self.is_ball = False



    def move(self, xt, yt):
        at = degrees(atan2(self.xr - xt, yt - self.yr))
        e = at - self.heading
        if e > 10: self.motor(10, -10)
        elif e < -10:self.motor(-10, 10)
        else: self.motor(10,10)
    def motor(self, vl, vr):
        self.left_motor.setVelocity(vl)
        self.right_motor.setVelocity(vr)
    def run(self):
        self.xb = 0
        self.yb = 0
        self.heading = 0
        self.xr = 0
        self.yr = 0
        step = 1
        while self.robot.step(TIME_STEP) != -1: # تا زمانی که بازی در حال اجراست
            if self.is_new_data(): # اگر دیتای جدیدی آماده خواندن بود
                self.readData()
                if self.is_ball: # اگر توپ دیده شد
                    # رفتن به سمت توپ
                    if step == 1:
                        self.move(self.xb, self.yb-0.1)
                        if math.sqrt((self.xr - self.xb)**2 + (self.yr - (self.yb - 0.1))**2) < 0.1:
                            step = 2
                    if step == 2:
                        self.move(self.xb, self.yb)
                        if math.sqrt((self.xr - self.xb)**2 + (self.yr - self.yb)**2) > 0.2:
                            step = 1
                else: # اگر توپ رو ندید
                    self.move(-0.5, -0.2)