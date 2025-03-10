import math
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
from math import *
from utils import *

class MyRobot2(RCJSoccerRobot):
    def run(self):
        tarif_moteghayer(self)
        while self.robot.step(TIME_STEP) != -1:  # تا زمانی که بازی در حال اجراست
            if self.is_new_data():  # اگر دیتای جدیدی آماده خواندن بود
                readData(self)
                if self.is_ball:
                    move(self, self.xb , self.yb)
                else:
                    formation(self)