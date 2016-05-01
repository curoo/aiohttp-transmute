import os
import subprocess


def main(build):
    build.packages.install("../transmute-core", develop=True)
    build.packages.install(".", develop=True)


def test(build):
    main(build)
    build.packages.install("jedi")
    build.packages.install("pytest")
    build.packages.install("pytest-cov")
    pytest = os.path.join(build.root, "bin", "py.test")
    subprocess.call([
        pytest, "--cov", "aiohttp_transmute",
        "aiohttp_transmute/tests",
        "--cov-report", "term-missing"
    ])


def distribute(build):
    """ distribute the uranium package """
    build.packages.install("wheel")
    build.executables.run([
        "python", "setup.py",
        "sdist", "bdist_wheel", "--universal", "upload"
    ])


def build_docs(build):
    build.packages.install("sphinx")
    return subprocess.call(
        ["make", "html"], cwd=os.path.join(build.root, "docs")
    )
