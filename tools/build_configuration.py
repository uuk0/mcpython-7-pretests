from . import BuildPipe


DEFAULT_BUILD_INSTANCE = BuildPipe.ProjectBuildManager()

DEFAULT_BUILD_INSTANCE.add_preparation_stage(BuildPipe.BlackCodeFormattingPreparation())

# Filter the file tree
DEFAULT_BUILD_INSTANCE.add_stage(
    BuildPipe.FileFilterTask(
        lambda file: not (
            ".git" in file
            or ".idea" in file
            or "__pycache__" in file
            or "builds" in file
        )
    )
)

DEFAULT_BUILD_INSTANCE.add_stage(BuildPipe.DumpTask("source.zip", as_zip=True))

DEFAULT_BUILD_INSTANCE.add_stage(
    BuildPipe.FilePrefixRenameTask("licences/", "")
)  # export every file from the licences/ folder to the home folder
DEFAULT_BUILD_INSTANCE.add_stage(BuildPipe.DumpTask("dev.zip", as_zip=True))
DEFAULT_BUILD_INSTANCE.add_stage(
    BuildPipe.BuildSplitStage(
        BuildPipe.PyMinifierTask(),
        BuildPipe.JsonMinifierTask(),
        BuildPipe.FileFilterTask(
            lambda file: not (
                file.startswith("tools/mdk")
                or (file.startswith("doc") and "changelog.txt" not in file)
            )
        ),
        BuildPipe.FilePrefixRenameTask("doc/", ""),
        BuildPipe.FilePrefixRenameTask("tools/", ""),
        BuildPipe.DumpTask("end_user.zip", as_zip=True),
        BuildPipe.NuitkaBuild(
            [
                "--standalone",
                "--assume-yes-for-downloads",
                "--follow-imports",
                "--output-dir={output_dir}/nuitka_output",
                #  "--lto",
                "--show-modules",
                "--onefile",
                "--windows-product-name=mcpython",
                "--windows-company-name=mcpython",
                "--windows-product-version=0.1.0",
            ],
            look_for_output="{output_dir}/nuitka_output/launch.dist/launch.exe",
        ),
    )
)
