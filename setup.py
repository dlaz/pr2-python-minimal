## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['pr2_python'],
    package_dir={'': 'src'},
    requires=[], # TODO
    scripts=['scripts/move_to_look.py', 'scripts/print_base_pose.py', 'scripts/print_joint_states.py', 'scripts/print_transform.py'],
)

setup(**setup_args)