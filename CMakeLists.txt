cmake_minimum_required(VERSION 2.8.3)
project(pr2_python)

find_package(catkin REQUIRED COMPONENTS nav_msgs pr2_mechanism_msgs std_srvs actionlib sensor_msgs rospy visualization_msgs move_base_msgs geometry_msgs pr2_controllers_msgs)
catkin_python_setup()

catkin_package(
    DEPENDS  # TODO
    CATKIN_DEPENDS nav_msgs pr2_mechanism_msgs std_srvs actionlib sensor_msgs rospy visualization_msgs move_base_msgs geometry_msgs pr2_controllers_msgs
    INCLUDE_DIRS # TODO include
    LIBRARIES # TODO
)

include_directories( ${Boost_INCLUDE_DIR} ${catkin_INCLUDE_DIRS})

install(PROGRAMS scripts/print_joint_states.py scripts/print_transform.py scripts/print_base_pose.py scripts/move_to_look.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

# if (CATKIN_ENABLE_TESTING)
#     catkin_add_nosetests(nosetests/tests.py) # this test doesn't do anything useful
# endif()