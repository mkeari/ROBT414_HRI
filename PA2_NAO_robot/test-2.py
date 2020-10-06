from naoqi import ALProxy
import time

port = 38995

textSpeakProxy = ALProxy("ALTextToSpeech", "127.0.0.1", port)
motionProxy = ALProxy("ALMotion", "127.0.0.1", port)
# textSpeakProxy = ALProxy("ALTextToSpeech", "zhanat-K56CB", 37826)
# motionProxy = ALProxy("ALMotion", "zhanat-K56CB", 37826)

# 10.1.198.45
handName = "LHand"
shoulderJoint = "LShoulderPitch"
wristJoint = "LWristYaw"


def Greetings():
    # Choregraphe bezier export in Python.
    # Choregraphe bezier export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.04, 2.48])
    keys.append([[-0.17, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [-0.17, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0.04, 2.48])
    keys.append([[0, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [0, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([0.04, 2.48])
    keys.append([[0.0850585, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [0.0850584, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([0.04, 2.48])
    keys.append([[-0.12147, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [-0.12147, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.04, 2.48])
    keys.append([[-0.41628, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [-0.41628, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.04, 2.48])
    keys.append([[-1.19444, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [-1.19444, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.04, 2.48])
    keys.append([[0.292188, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [0.292188, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([0.04, 2.48])
    keys.append([[0.123486, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [0.123486, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([0.04, 2.48])
    keys.append([[0.0988769, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [0.0988769, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([0.04, 2.48])
    keys.append([[-0.17, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [-0.17, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([0.04, 2.48])
    keys.append([[-0.0811277, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [-0.0811278, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.04, 0.4, 1.24, 2.08, 2.48])
    keys.append([[1.46936, [3, -0.0133333, 0], [3, 0.12, 0]], [-1.09607, [3, -0.12, 0], [3, 0.28, 0]], [-1.09607,
                                                                                                        [3, -0.28, 0], [3, 0.28, 0]], [-1.09607, [3, -0.28, 0], [3, 0.133333, 0]], [1.46936, [3, -0.133333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.04, 0.4, 0.8, 1.24, 1.68, 2.08, 2.48])
    keys.append([[0.176556, [3, -0.0133333, 0], [3, 0.12, 0]], [0.226893, [3, -0.12, -0.0503368], [3, 0.133333, 0.0559298]], [1.15541, [3, -0.133333, 0], [3, 0.146667, 0]], [0.226893, [3, -
                                                                                                                                                                                         0.146667, 0], [3, 0.146667, 0]], [1.15541, [3, -0.146667, 0], [3, 0.133333, 0]], [0.226893, [3, -0.133333, 0.050337], [3, 0.133333, -0.050337]], [0.176556, [3, -0.133333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.04, 2.48])
    keys.append([[0.096006, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [0.096006, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([0.04, 2.48])
    keys.append([[0.0850585, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [0.0850584, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([0.04, 2.48])
    keys.append([[0.12147, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [0.12147, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.04, 2.48])
    keys.append([[0.41628, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [0.41628, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.04, 2.48])
    keys.append([[1.19444, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [1.19444, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.04, 2.48])
    keys.append([[0.292188, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [0.292188, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([0.04, 2.48])
    keys.append([[0.123486, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [0.123486, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([0.04, 2.48])
    keys.append([[-0.0988769, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [-0.0988769, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([0.04, 2.48])
    keys.append([[-0.17, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [-0.17, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([0.04, 2.48])
    keys.append([[-0.0811277, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [-0.0811278, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.04, 2.48])
    keys.append([[1.46936, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [1.46936, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.04, 2.48])
    keys.append([[-0.176556, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [-0.176556, [3, -0.813333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.04, 2.48])
    keys.append([[0.096006, [3, -0.0133333, 0], [3, 0.813333, 0]],
                 [0.096006, [3, -0.813333, 0], [3, 0, 0]]])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        # motion = ALProxy("ALMotion", IP, 9559)
        # motion = ALProxy("ALMotion")
        motionProxy.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
        print err


def Follow():
    # Choregraphe bezier export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.04, 0.6])
    keys.append([[-0.17, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [-0.17, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0.04, 0.6])
    keys.append([[0, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [0, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([0.04, 0.6])
    keys.append([[0.0850585, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [0.0850585, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([0.04, 0.6])
    keys.append([[-0.12147, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [-0.12147, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.04, 0.6])
    keys.append([[-0.408921, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [-0.0349066, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.04, 0.6])
    keys.append([[-1.18963, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [-1.20137, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.04, 0.6])
    keys.append([[0.292188, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [0.292188, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([0.04, 0.6])
    keys.append([[0.123486, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [0.123486, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([0.04, 0.6])
    keys.append([[0.0988769, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [0.0988769, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([0.04, 0.6])
    keys.append([[-0.17, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [-0.17, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([0.04, 0.6])
    keys.append([[-0.0811277, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [-0.0811277, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.04, 0.6])
    keys.append([[1.47001, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [-0.764454, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.04, 0.6])
    keys.append([[0.178888, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [0.214413, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.04, 0.6])
    keys.append([[0.100959, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [1.01404, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([0.04, 0.6])
    keys.append([[0.0850585, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [0.0850585, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([0.04, 0.6])
    keys.append([[0.12147, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [0.12147, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.04, 0.6])
    keys.append([[0.41628, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [0.41628, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.04, 0.6])
    keys.append([[1.19444, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [1.19444, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.04, 0.6])
    keys.append([[0.292188, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [0.292188, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([0.04, 0.6])
    keys.append([[0.123486, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [0.123486, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([0.04, 0.6])
    keys.append([[-0.0988769, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [-0.0988769, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([0.04, 0.6])
    keys.append([[-0.17, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [-0.17, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([0.04, 0.6])
    keys.append([[-0.0811277, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [-0.0811277, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.04, 0.6])
    keys.append([[1.46763, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [1.44823, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.04, 0.6])
    keys.append([[-0.185496, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [-0.207399, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.04, 0.6])
    keys.append([[0.096006, [3, -0.0133333, 0], [3, 0.186667, 0]],
                 [0.096006, [3, -0.186667, 0], [3, 0, 0]]])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        # motion = ALProxy("ALMotion", IP, 9559)
        # motion = ALProxy("ALMotion")
        motionProxy.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
        print err


useSen = 0
useSen1 = 0

Greetings()

textSpeakProxy.say("Hello! I am Frank! Can I go with you?")

Follow()

motionProxy.setMoveArmsEnabled(False, False)


while(1):
    x = motionProxy.getAngles(shoulderJoint, useSen)
    wrist = motionProxy.getAngles(wristJoint, useSen1)

    degree_x = 180 * x[0] / 3.14
    normal_x = (degree_x + 43.8222)/43.8222

    degree_wrist = 180 * wrist[0] / 3.14
    normal_wrist = (degree_wrist - 58.1297)/58.1297

    print(degree_wrist)

    if(degree_x > -43.8222) & (degree_x < 0):
        print("Speed: " + str(normal_x))
        motionProxy.move(normal_x, 0.0, 0.0)
    else:
        print("Robot has stopped")
        motionProxy.move(0.0, 0.0, 0.0)

        if(degree_wrist > 90):
            print("Robot turning left")
            motionProxy.move(0.0, 0.0, normal_wrist)
        elif(degree_wrist < 0):
            print("Robot turning right")
            motionProxy.move(0.0, 0.0, normal_wrist)

    time.sleep(0.100)
