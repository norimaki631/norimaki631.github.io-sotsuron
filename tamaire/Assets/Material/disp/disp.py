# coding: utf-8
########## ヘッダ ##########
#%YAML 1.1
#%TAG !u! tag:unity3d.com,2011:
#--- !u!91 &9100000
#AnimatorController:
#  m_ObjectHideFlags: 0
#  m_PrefabParentObject: {fileID: 0}
#  m_PrefabInternal: {fileID: 0}
#  m_Name: disp
#  serializedVersion: 5
#  m_AnimatorParameters:
#  - m_Name: point
#    m_Type: 3
#    m_DefaultFloat: 0
#    m_DefaultInt: 0
#    m_DefaultBool: 0
#    m_Controller: {fileID: 0}
#  m_AnimatorLayers:
#  - serializedVersion: 5
#    m_Name: Base Layer
#    m_StateMachine: {fileID: 1107881186541672538}
#    m_Mask: {fileID: 0}
#    m_Motions: []
#    m_Behaviours: []
#    m_BlendingMode: 0
#    m_SyncedLayerIndex: -1
#    m_DefaultWeight: 0
#    m_IKPass: 0
#    m_SyncedLayerAffectsTiming: 0
#    m_Controller: {fileID: 9100000}
########## ステート ##########
#--- !u!1102 &1102482230009221382(後ろ3桁変更)
#AnimatorState:
#  serializedVersion: 5
#  m_ObjectHideFlags: 1
#  m_PrefabParentObject: {fileID: 0}
#  m_PrefabInternal: {fileID: 0}
#  m_Name: 1
#  m_Speed: 0
#  m_CycleOffset: 0.0105(オフセット値変更)
#  m_Transitions: []
#  m_StateMachineBehaviours: []
#  m_Position: {x: 0, y: 0, z: 0}
#  m_IKOnFeet: 0
#  m_WriteDefaultValues: 1
#  m_Mirror: 0
#  m_SpeedParameterActive: 0
#  m_MirrorParameterActive: 0
#  m_CycleOffsetParameterActive: 0
#  m_TimeParameterActive: 0
#  m_Motion: {fileID: 7400000, guid: 25125a3eb71847f40b1a3104bb13a523, type: 2}
#  m_Tag: 
#  m_SpeedParameter: 
#  m_MirrorParameter: 
#  m_CycleOffsetParameter: point
#  m_TimeParameter: point
########## トランジション ##########
#--- !u!1101 &1101666695064115174(後ろ3桁変更)
#AnimatorStateTransition:
#  m_ObjectHideFlags: 1
#  m_PrefabParentObject: {fileID: 0}
#  m_PrefabInternal: {fileID: 0}
#  m_Name: point
#  m_Conditions:
#  - m_ConditionMode: 6
#    m_ConditionEvent: point
#    m_EventTreshold: 1(1~999)
#  m_DstStateMachine: {fileID: 0}
#  m_DstState: {fileID: 1102482230009221382}(ステートに合わせる)
#  m_Solo: 0
#  m_Mute: 0
#  m_IsExit: 0
#  serializedVersion: 3
#  m_TransitionDuration: 0
#  m_TransitionOffset: 0
#  m_ExitTime: 0
#  m_HasExitTime: 0
#  m_HasFixedDuration: 1
#  m_InterruptionSource: 0
#  m_OrderedInterruption: 1
#  m_CanTransitionToSelf: 1
########## 総合 ##########
#--- !u!1102 &1102595633841359602
#AnimatorState:
#  serializedVersion: 5
#  m_ObjectHideFlags: 1
#  m_PrefabParentObject: {fileID: 0}
#  m_PrefabInternal: {fileID: 0}
#  m_Name: state
#  m_Speed: 1
#  m_CycleOffset: 0
#  m_Transitions: []
#  m_StateMachineBehaviours: []
#  m_Position: {x: 0, y: 0, z: 0}
#  m_IKOnFeet: 0
#  m_WriteDefaultValues: 1
#  m_Mirror: 0
#  m_SpeedParameterActive: 0
#  m_MirrorParameterActive: 0
#  m_CycleOffsetParameterActive: 0
#  m_TimeParameterActive: 0
#  m_Motion: {fileID: 0}
#  m_Tag: 
#  m_SpeedParameter: 
#  m_MirrorParameter: 
#  m_CycleOffsetParameter: point
#  m_TimeParameter: point
#--- !u!1107 &1107881186541672538
#AnimatorStateMachine:
#  serializedVersion: 5
#  m_ObjectHideFlags: 1
#  m_PrefabParentObject: {fileID: 0}
#  m_PrefabInternal: {fileID: 0}
#  m_Name: Base Layer
#  m_ChildStates:
#  - serializedVersion: 1
#    m_State: {fileID: 1102595633841359602}(ステート)
#    m_Position: {x: 240, y: 72, z: 0}
#  - serializedVersion: 1
#    m_State: {fileID: 1102482230009221382}(ステート)
#    m_Position: {x: 240, y: 276, z: 0}
#  - serializedVersion: 1
#    m_State: {fileID: 1102521934202659926}(ステート)
#    m_Position: {x: 504, y: 192, z: 0}
#  m_ChildStateMachines: []
#  m_AnyStateTransitions:
#  - {fileID: 1101930281369557914}
#  - {fileID: 1101232657785165244}
#  - {fileID: 1101320290193629784}
#  m_AnyStateTransitions: []
#  m_EntryTransitions: []
#  m_StateMachineTransitions: {}
#  m_StateMachineBehaviours: []
#  m_AnyStatePosition: {x: 50, y: 20, z: 0}
#  m_EntryPosition: {x: 50, y: 120, z: 0}
#  m_ExitPosition: {x: 800, y: 120, z: 0}
#  m_ParentStateMachinePosition: {x: 800, y: 20, z: 0}
#  m_DefaultState: {fileID: 1102595633841359602}


########## コード ##########

t0='''\
%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!91 &9100000
AnimatorController:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {fileID: 0}
  m_PrefabInternal: {fileID: 0}
  m_Name: disp
  serializedVersion: 5
  m_AnimatorParameters:
  - m_Name: point
    m_Type: 3
    m_DefaultFloat: 0
    m_DefaultInt: 0
    m_DefaultBool: 0
    m_Controller: {fileID: 0}
  m_AnimatorLayers:
  - serializedVersion: 5
    m_Name: Base Layer
    m_StateMachine: {fileID: 1107881186541672538}
    m_Mask: {fileID: 0}
    m_Motions: []
    m_Behaviours: []
    m_BlendingMode: 0
    m_SyncedLayerIndex: -1
    m_DefaultWeight: 0
    m_IKPass: 0
    m_SyncedLayerAffectsTiming: 0
    m_Controller: {fileID: 9100000}\
'''

t10='''\
--- !u!1102 &1102482230000000\
'''
t102='''\
1102482230000000\
'''
t11='''\
AnimatorState:
  serializedVersion: 5
  m_ObjectHideFlags: 1
  m_PrefabParentObject: {fileID: 0}
  m_PrefabInternal: {fileID: 0}
  m_Name: gen
  m_Speed: 0
  m_CycleOffset: \
'''
t12='''\
  m_Transitions: []
  m_StateMachineBehaviours: []
  m_Position: {x: 0, y: 0, z: 0}
  m_IKOnFeet: 0
  m_WriteDefaultValues: 1
  m_Mirror: 0
  m_SpeedParameterActive: 0
  m_MirrorParameterActive: 0
  m_CycleOffsetParameterActive: 0
  m_TimeParameterActive: 0
  m_Motion: {fileID: 7400000, guid: 25125a3eb71847f40b1a3104bb13a523, type: 2}
  m_Tag: 
  m_SpeedParameter: 
  m_MirrorParameter: 
  m_CycleOffsetParameter: point
  m_TimeParameter: point\
'''

t20='''\
--- !u!1101 &1101666695000000\
'''
t202='''\
1101666695000000\
'''
t21='''\
AnimatorStateTransition:
  m_ObjectHideFlags: 1
  m_PrefabParentObject: {fileID: 0}
  m_PrefabInternal: {fileID: 0}
  m_Name: point
  m_Conditions:
  - m_ConditionMode: 6
    m_ConditionEvent: point
    m_EventTreshold: \
'''
t22='''\
  m_DstStateMachine: {fileID: 0}
  m_DstState: {fileID: \
'''
t23='''\
}
  m_Solo: 0
  m_Mute: 0
  m_IsExit: 0
  serializedVersion: 3
  m_TransitionDuration: 0
  m_TransitionOffset: 0
  m_ExitTime: 0
  m_HasExitTime: 0
  m_HasFixedDuration: 1
  m_InterruptionSource: 0
  m_OrderedInterruption: 1
  m_CanTransitionToSelf: 1\
'''
tfileID='''\
  - {fileID: \
'''
tfileIDE='''\
}\
'''
t33='''\
--- !u!1107 &1107881186541672538
AnimatorStateMachine:
  serializedVersion: 5
  m_ObjectHideFlags: 1
  m_PrefabParentObject: {fileID: 0}
  m_PrefabInternal: {fileID: 0}
  m_Name: Base Layer
  m_ChildStates:
  - serializedVersion: 1\
'''
t34='''\
  - serializedVersion: 1
    m_State: {fileID: \
'''
t35='''\
}
    m_Position: {x: 240, y: 72, z: 0}\
'''
t36='''\
  m_ChildStateMachines: []
  m_AnyStateTransitions:\
'''
t37='''\
  m_EntryTransitions: []
  m_StateMachineTransitions: {}
  m_StateMachineBehaviours: []
  m_AnyStatePosition: {x: 50, y: 20, z: 0}
  m_EntryPosition: {x: 50, y: 120, z: 0}
  m_ExitPosition: {x: 800, y: 120, z: 0}
  m_ParentStateMachinePosition: {x: 800, y: 20, z: 0}
  m_DefaultState: {fileID: 1102482230000000000}
'''

############ code ##########
num = 1000
print(t0)
#トランジション
for i in range(num):
	s = '{:0=3}'.format(i)
	print(t20 + s)	#ID
	print(t21 + str(i))	#しきい値
	print(t22 + t102 + s + t23)	#移動先
#ステート
for i in range(num):
	s = '{:0=3}'.format(i)
	print(t10 + s)
	print(t11 + str(i/num))
	print(t12)
#総合
print(t33)
for i in range(num):
	s = '{:0=3}'.format(i)
	print(t34 + t102 + s + t35)
print(t36)
for i in range(num):
	s = '{:0=3}'.format(i)
	print(tfileID + t202 + s + tfileIDE)
print(t37)