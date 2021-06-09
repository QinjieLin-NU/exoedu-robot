import pybullet as p
import time
import pybullet_data
import pybullet_envs


p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")
exo_robot = p.loadURDF("urdf/exoedu_assemble.urdf",[0,0,0.5],globalScaling=0.01)

gravId = p.addUserDebugParameter("gravity",-10,10,0)
p.setPhysicsEngineParameter(numSolverIterations=100)
p.changeDynamics(exo_robot,-1,linearDamping=0, angularDamping=0)
jointAngles=[0.0]
activeJoint=0
jointIds = []
paramIds = []
for j in range (p.getNumJoints(exo_robot)):
    p.changeDynamics(exo_robot,j,linearDamping=0, angularDamping=0)
    info = p.getJointInfo(exo_robot,j)
    jointName = info[1]
    jointType = info[2]
    if (jointType==p.JOINT_PRISMATIC or jointType==p.JOINT_REVOLUTE):
        jointIds.append(j)
        paramIds.append(p.addUserDebugParameter(jointName.decode("utf-8"),-4,4,jointAngles[activeJoint]))
        p.resetJointState(exo_robot, j, jointAngles[activeJoint])
        activeJoint+=1


p.setRealTimeSimulation(1)
while(1):
    p.getCameraImage(320,200)
    info = p.getJointInfo(exo_robot,0)
    p.setGravity(0,0,p.readUserDebugParameter(gravId))
    
    for i in range(len(paramIds)):
        c = paramIds[i]
        targetPos = p.readUserDebugParameter(c)
        p.setJointMotorControl2(exo_robot,jointIds[i],p.POSITION_CONTROL,targetPos, force=100.)
        p.setTimeStep(0.1)
