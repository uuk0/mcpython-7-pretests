import tools.build_configuration
import sys
import os
import shutil

local = os.path.dirname(__file__)


build_name = input("build name: ") if len(sys.argv) == 1 else sys.argv[1]


folder = local + "/builds/" + build_name
tools.build_configuration.DEFAULT_BUILD_INSTANCE.run(local, folder)
