#visualization_tools.py
'''
Functions for creating visualization_msgs.
'''

__docformat__ = "restructuredtext en"

import roslib; roslib.load_manifest('pr2_python')
from visualization_msgs.msg import Marker, MarkerArray
from arm_navigation_msgs.msg import RobotState
import copy
import rospy
import pr2_python.trajectory_tools as tt

def marker_at(pose_stamped, ns='', mid=0, mtype=Marker.SPHERE, sx=0.05, sy=0.05, sz=0.05, r=0.0, g=0.0, b=1.0, 
              a=0.8):
    '''
    Returns a single marker at a pose.

    See the visualization_msgs.msg.Marker documentation for more details on any of these fields.

    **Args:**
    
        **pose_stamped (geometry_msgs.msg.PoseStamped):** Pose for marker

        *ns (string):* namespace

        *mid (int):* ID
        
        *mtype (int):* Shape type

        *sx (double):* Scale in x

        *sy (double):* Scale in y

        *sz (double):* scale in z

        *r (double):* Red (scale 0 to 1)

        *g (double):* Green (scale 0 to 1)

        *b (double):* Blue (scale 0 to 1)

        *a (double):* Alpha (scale 0 to 1)

    **Returns:**
        visualization_msgs.msg.Marker at pose_stamped
    '''
    marker = Marker()
    marker.header = copy.deepcopy(pose_stamped.header)
    marker.ns = ns
    marker.id = mid
    marker.type = mtype
    marker.action = marker.ADD
    marker.pose = copy.deepcopy(pose_stamped.pose)
    marker.scale.x = sx
    marker.scale.y = sy
    marker.scale.z = sz
    marker.color.r = r
    marker.color.g = g
    marker.color.b = b
    marker.color.a = a
    return marker

def marker_at_point(point_stamped, ns='', mid=0, mtype=Marker.SPHERE, sx=0.05, sy=0.05, sz=0.05, r=0.0, g=0.0, 
                    b=1.0, a=0.8):
    '''
    Returns a single marker at a point.

    Orientation is always (0, 0, 0, 1).  See the visualization_msgs.msg.Marker documentation for more details on 
    any of these fields.

    **Args:**
    
        **point_stamped (geometry_msgs.msg.PointStamped):** Point for marker

        *ns (string):* namespace

        *mid (int):* ID
        
        *mtype (int):* Shape type

        *sx (double):* Scale in x

        *sy (double):* Scale in y

        *sz (double):* scale in z

        *r (double):* Red (scale 0 to 1)

        *g (double):* Green (scale 0 to 1)

        *b (double):* Blue (scale 0 to 1)

        *a (double):* Alpha (scale 0 to 1)

    **Returns:**
        visualization_msgs.msg.Marker at point_stamped
    '''

    marker = Marker()
    marker.header = copy.deepcopy(point_stamped.header)
    marker.ns = ns
    marker.id = mid
    marker.type = mtype
    marker.action = marker.ADD
    marker.pose.position = copy.deepcopy(point_stamped.point)
    marker.pose.orientation.w = 1.0
    marker.scale.x = sx
    marker.scale.y = sy
    marker.scale.z = sz
    marker.color.r = r
    marker.color.g = g
    marker.color.b = b
    marker.color.a = a
    return marker


def hsv_to_rgb(h, s, v):
    '''
    Converts from HSV to RGB

    **Args:**
    
        **h (double):** Hue

        **s (double):** Saturation

        **v (double):** Value

    **Returns:**
       The (r, g, b) values corresponding to this HSV color.
    '''
    hp = h/60.0
    c = v*s
    x = c*(1 - abs(hp % 2 - 1))
    if hp < 1:
        return (c, x, 0)
    if hp < 2:
        return (x, c, 0)
    if hp < 3:
        return (0, c, x)
    if hp < 4:
        return (0, x, c)
    if hp < 5:
        return (x, 0, c)
    return (c, 0, x)