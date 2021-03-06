#   Copyright (C) 2019  Davide De Tommaso
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>

import yarp
import sys
sys.path.append('../../')

from pyicub.api.iCubHelper import iCub, ROBOT_TYPE

yarp.Network.init()

icub = iCub(ROBOT_TYPE.ICUB, logtype="DEBUG")
icub.gaze.lookAt3DPoint(-1.0, -0.5, 1.0, waitMotionDone=True)
icub.gaze.lookAt3DPoint(-1.0, -0.2, 0.5, waitMotionDone=True)
icub.gaze.lookAt3DPoint(-1.0, 0.2, 0.1, waitMotionDone=True)
