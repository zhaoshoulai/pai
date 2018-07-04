# Copyright (c) Microsoft Corporation
# All rights reserved.
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
# to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
# BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
import os
import unittest
import sys
sys.path.append("..")
from exporter.docker_inspect import parse_docker_inspect

class TestDockerInspect(unittest.TestCase):
    """
    Test docker_inspect.py
    """
    def setUp(self):
        try:
            os.chdir(os.path.abspath("test"))
        except:
            pass

    def tearDown(self):
        try:
            os.chdir(os.path.abspath(".."))
        except:
            pass

    def test_parse_docker_inspect(self):
        sample_path = "data/docker_inspect_sample.json"
        file = open(sample_path, "r") 
        dockerInspect = file.read()
        inspectInfo = parse_docker_inspect(dockerInspect)
        targetInspectInfo = {'labels': ['container_label_PAI_USER_NAME="openmindstudio"', 'container_label_GPU_ID="0,1,"', 'container_label_PAI_HOSTNAME="paigcr-a-gpu-1058"', 'container_label_PAI_JOB_NAME="trialslot_nnimain_d65bc5ac"', 'container_label_PAI_CURRENT_TASK_ROLE_NAME="tuner"'], 'env': ['container_env_PAI_TASK_INDEX="0"']}
        self.assertEqual(targetInspectInfo, inspectInfo)
        pass

if __name__ == '__main__':
    unittest.main()