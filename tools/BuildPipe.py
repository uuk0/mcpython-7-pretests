import os
import shutil
import subprocess
import sys
import tempfile
import typing
import zipfile
from abc import ABC

import json

HOME = os.path.dirname(__file__)


class ProjectView:
    """
    Helper class for in-memory file manipulation
    todo: export to common place / library
    """

    def __init__(self):
        self.path_lookup = {}
        self.path_cache = {}
        self.modified_files = set()

    def with_directory_source(
        self,
        directory: str,
        filter_files: typing.Callable[[str], bool] = lambda _: True,
    ):
        """
        Adds the files from a directory to the project view
        :param directory: the directory to load from
        :param filter_files: a filter function; useful when only special files should be included
        """
        for root, dirs, files in os.walk(directory):
            for file in files:
                whole_file = os.path.join(root, file).replace("\\", "/")
                f = os.path.relpath(whole_file, directory).replace("\\", "/")
                if filter_files(whole_file):
                    self.path_lookup[f] = whole_file
                    self.modified_files.add(f)
        return self

    def copy(self) -> "ProjectView":
        """
        Copies the ProjectView class; Writing to the files not loaded into memory are still changed in the view
        """
        instance = ProjectView()
        instance.path_lookup = self.path_lookup.copy()
        instance.path_cache = self.path_cache.copy()
        instance.modified_files = self.modified_files.copy()
        return instance

    def read(self, file: str, cache=False) -> bytes:
        """
        Reads a relative file
        :param file: the relative file
        :param cache: if the read data should be cached; useful when planning to access it multiple times in the near
            future
        :return: the data
        """
        if file in self.path_cache:
            return self.path_cache[file]

        with open(self.path_lookup[file], mode="rb") as f:
            data = f.read()

        if cache:
            self.path_cache[file] = data

        return data

    def write(self, file: str, data: bytes):
        """
        Writes data into the local cache, overriding existing data, and overriding the original file data previously
            accessable via read()
        :param file: the file
        :param data: the data to write
        """
        assert isinstance(data, bytes)
        self.path_cache[file] = data
        self.modified_files.add(file)

    def dump_into_directory(
        self,
        directory: str,
        file_filter: typing.Callable[[str], bool] = lambda _: True,
    ):
        """
        Writes all affected files into the given directory (all files accessed by with_directory_source
            and write()-en to)
        :param directory: the directory to write to
        :param file_filter: a filter for the files
        """
        for file in self.modified_files:
            if not file_filter(file):
                continue

            if file in self.path_cache:
                with open(os.path.join(directory, file), mode="wb") as f:
                    f.write(self.path_cache[file])
            elif file in self.path_lookup:
                shutil.copyfile(self.path_lookup[file], os.path.join(directory, file))
            else:
                print("skipping file", file, "as the file is not found")

    def dump_into_zipfile(
        self, file: str, file_filter: typing.Callable[[str], bool] = lambda _: True
    ):
        """
        Writes all affected files into the given zipfile (all files accessed by with_directory_source
            and write()-en to)
        :param file: the file to write into
        :param file_filter: a filter for the files
        """
        with zipfile.ZipFile(file, mode="w") as zip_file:
            for file in self.modified_files:
                if not file_filter(file):
                    continue

                if file in self.path_cache:
                    with zip_file.open(file, mode="w") as f:
                        f.write(self.path_cache[file])
                elif file in self.path_lookup:
                    zip_file.write(self.path_lookup[file], file)
                else:
                    print("skipping file", file, "as the file is not found")

    def filter_in_place(self, file_filter: typing.Callable[[str], bool]):
        self.modified_files = set(filter(file_filter, self.modified_files))

    def merge(self, other: "ProjectView"):
        for file in other.modified_files:
            if file in other.path_cache:
                self.path_cache[file] = other.path_cache[file]
            elif file in other.path_lookup:
                self.path_lookup[file] = other.path_lookup[file]
            else:
                print("skipping file", file, "as the file is not found")
                continue
            self.modified_files.add(file)

    def print_stats(self):
        print(self.modified_files)

    def clear(self):
        self.modified_files.clear()
        self.path_cache.clear()
        self.path_lookup.clear()


class AbstractBuildStage(ABC):
    """
    Base class for a stage in the build system
    """

    def execute_on(self, view: ProjectView, build_output_dir: str, build_manager):
        raise NotImplementedError


class AbstractProjectPreparation(ABC):
    """
    Base class for a preparation stage; A stage affecting files, and not consuming a ProjectView.
    The ProjectView is created based on the results of this transformer
    """

    def execute_in(self, directory: str, build_manager):
        raise NotImplementedError


class ProjectBuildManager:
    """
    The manager, storing how to build certain things
    """

    def __init__(self):
        self.preparation_stages: typing.List[AbstractProjectPreparation] = []
        self.stages: typing.List[AbstractBuildStage] = []
        self.build_name = None
        self.version_id = None

    def add_preparation_stage(self, stage: AbstractProjectPreparation):
        """
        Adds such preparation stage to the internal list
        :param stage: the stage
        """

        self.preparation_stages.append(stage)
        return self

    def add_stage(self, stage: AbstractBuildStage):
        """
        Adds a normal stage into the internal list
        :param stage: the stage to add
        """

        self.stages.append(stage)
        return self

    def run(
        self,
        directory: str,
        build_output_dir: str,
        project_view_consumer: typing.Callable[[ProjectView], None] = None,
    ):
        """
        Runs the build configuration onto the given directory and outputs the data at the given directory
        :param directory: the directory to use as a source
        :param build_output_dir: the directory to output to
        :param project_view_consumer: a consumer for the project view, for additonal changes
        """

        if not os.path.isdir(build_output_dir):
            os.makedirs(build_output_dir)

        for preparation in self.preparation_stages:
            print("running preparation {}".format(preparation))
            preparation.execute_in(directory, self)

        view = ProjectView().with_directory_source(directory)

        if callable(project_view_consumer):
            project_view_consumer(view)

        for stage in self.stages:
            print("running stage {}".format(stage))
            try:
                stage.execute_on(view, build_output_dir, self)
            except:
                view.print_stats()
                raise

        return view


class BlackCodeFormattingPreparation(AbstractProjectPreparation):
    def execute_in(self, directory: str, build_manager):
        subprocess.call([sys.executable, "-m", "black", directory])


class PyMinifierTask(AbstractBuildStage):
    def __init__(self, special_config=None):
        if special_config is None:
            special_config = {}
        self.special_config = special_config

    def execute_on(self, view: ProjectView, build_output_dir: str, build_manager):
        try:
            import python_minifier
        except ImportError:
            subprocess.Popen(
                [sys.executable, "-m", "pip", "install", "python-minifier"]
            )
            import python_minifier

        for file in view.modified_files:
            if file.endswith(".py"):
                if file not in self.special_config:
                    view.write(
                        file,
                        python_minifier.minify(
                            view.read(file).decode("utf-8"),
                            preserve_locals=["NAME"],
                            remove_literal_statements=True,
                        ).encode("utf-8"),
                    )
                else:
                    view.write(
                        file,
                        python_minifier.minify(
                            view.read(file).decode("utf-8"), **self.special_config[file]
                        ).encode("utf-8"),
                    )


class JsonMinifierTask(AbstractBuildStage):
    def execute_on(self, view: ProjectView, build_output_dir: str, build_manager):
        for file in view.modified_files:
            if file.endswith(".json"):
                view.write(
                    file,
                    json.dumps(
                        json.loads(view.read(file).decode("utf-8"))
                    ).encode("utf-8"),
                )


class BuildSplitStage(AbstractBuildStage):
    """
    A stage for splitting the current build chain into a sub-chain not modifying the base chain
    """

    def __init__(self, *parts: AbstractBuildStage, merge_back=False):
        self.parts = parts
        self.merge_back = merge_back

    def execute_on(self, view: ProjectView, build_output_dir: str, build_manager):
        view = view.copy() if not self.merge_back else view
        for part in self.parts:
            print("running stage {}".format(part))
            part.execute_on(view, build_output_dir, None)


class BuildSplitUsingManagerAndTMPCache(AbstractBuildStage):
    """
    Similar to BuildSplitStage, but takes a whole ProjectBuildManager.
    Data is written to a temporary directory
    """

    def __init__(self, manager: ProjectBuildManager, merge_back=False):
        self.manager = manager
        self.merge_back = merge_back

    def execute_on(self, view: ProjectView, build_output_dir: str, build_manager):
        directory = tempfile.TemporaryDirectory()
        view.dump_into_directory(directory.name)
        view2 = self.manager.run(directory.name, build_output_dir)

        if self.merge_back:
            view.merge(view2)

        directory.cleanup()


class DumpTask(AbstractBuildStage):
    """
    Task for dumping the whole file tree
    as_zip defines if the data should be written to a zip file or not
    file_filter is passed to the dump function
    """

    def __init__(
        self,
        file_or_dir_name: str,
        as_zip=True,
        file_filter: typing.Callable[[str], bool] = lambda _: True,
    ):
        self.file_or_dir_name = file_or_dir_name
        self.as_zip = as_zip
        self.file_filter = file_filter

    def execute_on(self, view: ProjectView, build_output_dir: str, build_manager):
        if self.as_zip:
            view.dump_into_zipfile(
                os.path.join(build_output_dir, self.file_or_dir_name).replace(
                    "\\", "/"
                ),
                file_filter=self.file_filter,
            )
        else:
            view.dump_into_directory(
                os.path.join(build_output_dir, self.file_or_dir_name).replace(
                    "\\", "/"
                ),
                file_filter=self.file_filter,
            )


class FileFilterTask(AbstractBuildStage):
    """
    Helper for filtering the project view by file name
    """

    def __init__(self, file_filter: typing.Callable[[str], bool]):
        self.file_filter = file_filter

    def execute_on(self, view: ProjectView, build_output_dir: str, build_manager):
        view.filter_in_place(self.file_filter)


class FileRenameTask(AbstractBuildStage):
    """
    Helper for renaming certain files in the tree
    """

    def __init__(self, rename: typing.Callable[[str], str]):
        self.rename = rename

    def execute_on(self, view: ProjectView, build_output_dir: str, build_manager):
        for file in view.modified_files:
            new_file = self.rename(file)
            if new_file != file:
                view.modified_files.remove(file)
                view.modified_files.add(new_file)
                if file in view.path_cache:
                    view.path_cache[new_file] = view.path_cache.pop(file)

                if file in view.path_lookup:
                    view.path_lookup[new_file] = view.path_lookup.pop(file)


class FilePrefixRenameTask(FileRenameTask):
    def __init__(self, renames_from, renames_to):
        self.renames_from = renames_from
        self.renames_to = renames_to
        super().__init__(self.rename_task)

    def rename_task(self, file: str) -> str:
        if file.startswith(self.renames_from):
            return self.renames_to + file.removeprefix(self.renames_from)
        return file

    def __repr__(self):
        return "FilePrefixRenameTask(from='{}',to='{}')".format(
            self.renames_from, self.renames_to
        )


PY_FILE_FILTER = FileFilterTask(lambda file: file.endswith(".py"))


class NuitkaBuild(AbstractBuildStage):
    def __init__(
        self,
        launch_args=None,
        executable_name: str = "result.exe",
        look_for_output="{tmp}/launch.exe",
    ):
        self.look_for_output = look_for_output
        self.executable_name = executable_name
        if launch_args is None:
            launch_args = []
        self.launch_args = launch_args

    def execute_on(self, view: ProjectView, build_output_dir: str, build_manager):
        args = [arg.format(output_dir=build_output_dir) for arg in self.launch_args]

        tmp = tempfile.TemporaryDirectory()
        view.dump_into_directory(tmp.name)

        subprocess.call(
            [sys.executable, "-m", "nuitka"] + args + [tmp.name + "/launch.py"]
        )

        shutil.copyfile(
            self.look_for_output.format(tmp=tmp.name, output_dir=build_output_dir),
            build_output_dir + "/" + self.executable_name,
        )

