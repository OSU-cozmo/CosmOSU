from ..Robot import Robot
def say(self, msg = "some message"):
        self.robot.say_text(msg).wait_for_completed();
Robot.say = say;
