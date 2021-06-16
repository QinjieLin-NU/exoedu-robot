import pybullet as p
import time
import pybullet_data
import pybullet_envs

class ExoRobot:
    def __init__(self) :
        p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.loadURDF("plane.urdf")
        # self.exo_robot = p.loadURDF("urdf/exoedu_assemble.urdf",[0,0,0.5],globalScaling=0.01)
        self.exo_robot = p.loadURDF("urdf/exoedu_scale.urdf",[0,0,0.5],globalScaling=1)

        p.setPhysicsEngineParameter(numSolverIterations=100)
        p.changeDynamics(self.exo_robot,-1,linearDamping=0, angularDamping=0)
        init_jointAngles=[0.0]
        activeJoint=0
        self.jointIds = []
        self.paramIds = []

        #add Debug parameter
        self.gravId = p.addUserDebugParameter("gravity",-10,10,0)
        for j in range (p.getNumJoints(self.exo_robot)):
            p.changeDynamics(self.exo_robot,j,linearDamping=0, angularDamping=0)
            info = p.getJointInfo(self.exo_robot,j)
            jointName = info[1]
            jointType = info[2]
            if (jointType==p.JOINT_PRISMATIC or jointType==p.JOINT_REVOLUTE):
                self.jointIds.append(j)
                self.paramIds.append(p.addUserDebugParameter(jointName.decode("utf-8"),-4,4,init_jointAngles[activeJoint]))
                p.resetJointState(self.exo_robot, j, init_jointAngles[activeJoint])
                activeJoint+=1

        p.setRealTimeSimulation(1)


    def step(self,joint_angle) :
        p.setJointMotorControl2(self.exo_robot,self.jointIds[0],p.POSITION_CONTROL,joint_angle, force=500.)
        p.setTimeStep(0.01)
        return
    
    def executeDebuger(self) :
        while(1):
            p.getCameraImage(320,200)
            info = p.getJointInfo(self.exo_robot,0)
            p.setGravity(0,0,p.readUserDebugParameter(self.gravId))
            
            for i in range(len(self.paramIds)):
                c = self.paramIds[i]
                targetPos = p.readUserDebugParameter(c)
                p.setJointMotorControl2(self.exo_robot,self.jointIds[i],p.POSITION_CONTROL,targetPos, force=140.)
                p.setTimeStep(0.1)
        return
    
