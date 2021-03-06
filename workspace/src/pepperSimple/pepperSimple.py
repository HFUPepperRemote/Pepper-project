# pepperSimple.py
# -*- coding: latin-1 -*-
# implements simple Pepper-Class for moving the arms
#
#

import time 
import almath
import qi 
from naoqi import ALProxy 
import commentjson 
import argparse         # for testing


#class Pepper(GeneratedClass):
class Pepper():

    def __init__(self, arguments):
        # get config parameteres
        self.conf= commentjson.load(open(arguments["conf"]))
        self.IP=str(self.conf["PepperIP"])
        #print("IP: ",self.IP, "Type: ", type(self.IP))
        self.PORT= self.conf["PepperPORT"]
        self.behaviorName= str()    # set name of current behavior to ""
        
        


    def onLoad(self):
        #put initialization code here
        # set up connection to real Pepper robot and init all proxies required
        # 1) Motion proxy used later
        self.motionProxy = ALProxy("ALMotion", self.IP, self.PORT)
        self.motionProxy.wakeUp()
        self.postureProxy = ALProxy("ALRobotPosture", self.IP, self.PORT)
        
        # 2) Proxy for pre-defined Behaviors used later
        self.behaviorProxy = ALProxy("ALBehaviorManager", self.IP, self.PORT)
        
        # 3) Speech proxy for TTS output for warnings
        #warning= "Achtung, ich werde mich jetzt bewegen!"
        self.tts = ALProxy('ALTextToSpeech', self.IP, self.PORT)
        sentence = "\RSPD="+ str(100) + "\ "
        sentence += "\VCT="+ str(100) + "\ "
        #sentence += warning
        sentence +=  "\RST\ "
        self.tts.post.say(str(sentence))
        self.motionProxy.setStiffnesses("Head", 1.0)
        self.motionProxy.setStiffnesses("LArm", 1.0)
        self.motionProxy.setStiffnesses("RArm", 1.0)


    def onUnload(self):
        #put clean-up code here
        pass
    
    def onStopped(self):
        # used in Choregraphe
        #put clean-up code here
        pass

    def nodHead(self, num=1):
        while (num >0) :
            names            = "HeadPitch"
            angles           = 30.0*almath.TO_RAD
            fractionMaxSpeed = 0.3
            self.motionProxy.setAngles(names,angles,fractionMaxSpeed)
            time.sleep(0.5)
            names            = "Head"
            angleLists       = [0.0*almath.TO_RAD, 0.0*almath.TO_RAD]
            fractionMaxSpeed = 0.3
            self.motionProxy.setAngles(names,angleLists,fractionMaxSpeed)
            time.sleep(0.5)
            num -= 1 

    def moveArm(self, angle, speed, isRight):
        names            = "RShoulderPitch" if isRight else "LShoulderPitch"
        #self.logger.info("Arm= "+ names)
        angles           = angle * almath.TO_RAD
        fractionMaxSpeed = speed
        self.motionProxy.setAngles(names,angles,fractionMaxSpeed)

    def defaultPose(self, isInit= False):
        self.postureProxy.goToPosture("StandInit", 0.5)
        # test: self.sayText("Hallo, guten Morgen", 150, 50)
        if isInit :
            self.nodHead()
            self.postureProxy.goToPosture("StandZero", 0.5)
            # Arms in default pos. incl. offset
            self.moveArm(0, 0.8, True)
            self.moveArm(0, 0.8, False)
            names            = ["RWristYaw", "LWristYaw", "RElbowYaw", "LElbowYaw"]
            angles           = [90.0*almath.TO_RAD,-90.0*almath.TO_RAD, 90.0*almath.TO_RAD, -90.0*almath.TO_RAD]
            fractionMaxSpeed = 0.4
            self.motionProxy.setAngles(names,angles,fractionMaxSpeed)
            time.sleep(0.5)
            self.motionProxy.openHand("RHand")
            self.motionProxy.openHand("LHand")
        self.nodHead(1)

    # set 1 or 2 arms to the same angle position using speed, and sleep
    def setArms(self, angle, speed, useBothArms):
        if useBothArms :
            names = ["RShoulderPitch", "LShoulderPitch"]
            angles= [angle * almath.TO_RAD, angle * almath.TO_RAD]
        else :
            names = "RShoulderPitch"
            angles= angle * almath.TO_RAD
        fractionMaxSpeed = speed
        self.motionProxy.setAngles(names,angles,fractionMaxSpeed)
        time.sleep(0.1 + abs(angle)/50)

    def doHickUp(self):
        self.motionProxy.setStiffnesses("Body", 1.0) 
        self.setArms(5, 0.9, True)
        self.setArms(-20, 0.9, True)
        self.setArms(0, 0.9, True)
        sentence = "\RSPD="+ str(100) + "\ "
        sentence += "\VCT="+ str(100) + "\ "
        sentence += "Ups tut mir leid!"
        sentence +=  "\RST\ "
        self.tts.post.say(str(sentence))
        
    def executeBehavior(self, myBehavior):
        if len(self.behaviorName) > 0 and self.behaviorName != myBehavior:
            sentence = "Ups, bin gerade noch beschäftigt"
            self.tts.post.say(str(sentence))
            time.sleep(1)
            self.nodHead(1)
            raise RuntimeError("this box is already running another behavior")
        try:
            self.behaviorName = myBehavior
            self.behaviorProxy.runBehavior(myBehavior)
        finally:
            self.behaviorName = str() # empty name
            self.onStopped()
            
    def sayText(self, myText, speed, pitch):
        sentence = "\RSPD="+ str(speed) + "\ "
        sentence += "\VCT="+ str(pitch) + "\ "
        sentence += myText
        sentence +=  "\RST\ "
        self.tts.post.say(str(sentence))

    def gotoSleep(self):
        self.postureProxy.goToPosture("StandInit", 0.5)
        sentence = "\RSPD="+ str(100) + "\ "
        sentence += "\VCT="+ str(100) + "\ "
        sentence += "Ich gehe mal schlafen!"
        sentence +=  "\RST\ "
        self.tts.post.say(str(sentence))
        self.motionProxy.setStiffnesses("Body", 0.0) 

    def onInput_onStart(self):
        self.defaultPose(True)
        #self.nodHead(1)
        time.sleep(1)
        self.setArms(0, 0.5, True)
        self.nodHead(1)
        time.sleep(1)
        # test predefined Behavior from internal AnimationLibrary
        self.sayText("Ich probiere eine Bewegung aus meiner Bibliothek", 100, 130)
        self.executeBehavior("Stand/Waiting/Binoculars_1")
        self.sayText("Nicht schlecht, oder? Jetzt noch was anderes", 80, 80)
        self.executeBehavior("Stand/Waiting/MysticalPower_1")
        self.gotoSleep()
        self.onStopped() #activate the output of the box

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
        
    
        
    def halloZusammenWA(self):
        self.sayText("Hallo Zusammen, ich arbeite gerade an meiner Bachelor Thesis. Hoert also auf mir lustige Katzenvideos zu schicken", 90, 100)
        self.executeBehavior("Stand/Gestures/Desperate_1")
        self.executeBehavior("Stand/Gestures/Desperate_2")
        self.executeBehavior("Stand/Gestures/Desperate_3")
        self.executeBehavior("Stand/Gestures/Desperate_3")
        self.executeBehavior("Pepper Tablet Event Example")
    
    
    

        
    def halloHerrCochlovius(self):
        self.sayText("Hallo Herr Cochlovius. hier rufe ich eine Funktion auf mit selbst definierten Bewegungen", 90, 100)
        # Choregraphe simplified export in Python.
        from naoqi import ALProxy
        names = list()
        times = list()
        keys = list()
        
        names.append("HeadPitch")
        times.append([1.12, 3.32, 5.68, 7.96, 9.96])
        keys.append([-0.121185, -0.133456, -0.111981, -0.110447, -0.110447])
        
        names.append("HeadYaw")
        times.append([1.12, 3.32, 5.68, 7.96, 9.96])
        keys.append([-1.27014, 1.44961, 0.0260777, 0.0245438, 0.0245438])
        
        names.append("HipPitch")
        times.append([1.12, 3.32, 5.68, 7.96, 9.96])
        keys.append([-0.0199418, -0.0199418, -0.0199418, -0.00920391, -0.00920391])
        
        names.append("HipRoll")
        times.append([1.12, 3.32, 5.68, 7.96, 9.96])
        keys.append([-0.0107379, 0, 0, -0.00153399, -0.00153399])
        
        names.append("KneePitch")
        times.append([1.12, 3.32, 5.68, 7.96, 9.96])
        keys.append([-0.00153399, -0.00153399, -0.00153399, 0.00920391, 0.00920391])
        
        names.append("LElbowRoll")
        times.append([1.12, 3.32, 5.68, 7.96, 9.96])
        keys.append([-0.116583, -0.116583, -0.116583, -0.116583, -0.116583])
        
        names.append("LElbowYaw")
        times.append([1.12, 3.32, 5.68, 7.96, 9.96])
        keys.append([-1.71499, -1.71499, -1.71499, -1.71499, -1.71499])
        
        names.append("LHand")
        times.append([1.12, 3.32, 5.68, 7.96, 9.96])
        keys.append([0.690685, 0.690685, 0.690685, 0.680141, 0.680141])
        
        names.append("LShoulderPitch")
        times.append([1.12, 3.32, 5.68, 7.96, 9.96])
        keys.append([1.75948, 1.75948, 1.75948, 1.75948, 1.75948])
        
        names.append("LShoulderRoll")
        times.append([1.12, 3.32, 5.68, 7.96, 9.96])
        keys.append([0.0997088, 0.0997088, 0.0997088, 0.0997088, 0.0997088])
        
        names.append("LWristYaw")
        times.append([1.12, 3.32, 5.68, 7.96, 9.96])
        keys.append([0.0444441, 0.0444441, 0.0444441, 0.0444441, 0.0444441])
        
        names.append("RElbowRoll")
        times.append([1.12, 3.32, 5.68, 7.96, 9.96])
        keys.append([0.0935729, 0.0935729, 0.0935729, 0.543029, 0.167204])
        
        names.append("RElbowYaw")
        times.append([1.12, 3.32, 5.68, 7.96, 9.96])
        keys.append([1.69198, 1.69198, 1.69198, 1.67511, 1.67511])
        
        names.append("RHand")
        times.append([1.12, 3.32, 5.68, 7.96, 9.96])
        keys.append([0.676626, 0.676626, 0.676626, 0.596661, 0.596661])
        
        names.append("RShoulderPitch")
        times.append([1.12, 3.32, 5.68, 7.96, 9.96])
        keys.append([1.75027, 1.75027, 1.75027, 0.0276117, 1.57693])
        
        names.append("RShoulderRoll")
        times.append([1.12, 3.32, 5.68, 7.96, 9.96])
        keys.append([-0.0935729, -0.0935729, -0.0935729, -0.0184078, -0.0122719])
        
        names.append("RWristYaw")
        times.append([1.12, 3.32, 5.68, 7.96, 9.96])
        keys.append([-0.047596, -0.047596, -0.047596, 1.47873, -0.00310993])
        
        try:
          # uncomment the following line and modify the IP if you use this script outside Choregraphe.
          # motion = ALProxy("ALMotion", IP, 9559)
          #motion = ALProxy("ALMotion")
            self.motionProxy.angleInterpolation(names, keys, times, True)
        except BaseException, err:
            print err

        
        
        
if __name__ == "__main__":
    # construct the argument parse and parse the arguments
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    #ap.add_argument("-v", "--video",
        #help="path to the (optional) video file")
    #ap.add_argument("-b", "--buffer", type=int, default=16,
        #help="max buffer size")
    ap.add_argument("-c", "--conf", required=True,
        help="path to the JSON configuration file")
    args = vars(ap.parse_args())
    myPepper= Pepper(args)
    myPepper.onLoad()
    #myPepper.onInput_onStart()
    myPepper.halloHerrCochlovius()











