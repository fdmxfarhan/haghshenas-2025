from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
from math import *
from utils import *

class MyRobot1(RCJSoccerRobot):
    def goalKeeper(self):
        if self.yb < -0.7:
            if self.xb > 0:
                move(self, self.xb-0.01, self.yb)
            else:
                move(self, self.xb+0.01, self.yb)
        elif self.xb < 0.35 and self.xb > -0.35:
            move(self, self.xb, -0.55)
        elif self.yb < -0.5:
            move(self, self.xr, self.yb-0.05)
        elif self.xb > 0.4:
            move(self, 0.4, -0.55)
        elif self.xb < -0.4:
            move(self, -0.4, -0.55)
    def run(self):
        tarif_moteghayer(self)
        while self.robot.step(TIME_STEP) != -1: # تا زمانی که بازی در حال اجراست
            if self.is_new_data(): # اگر دیتای جدیدی آماده خواندن بود
                readData(self)
                if self.is_ball:
                    self.goalKeeper()
                else:
                    formation(self)
