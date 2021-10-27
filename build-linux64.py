import env
import os


def run(command: str) -> None:
    os.system(command)


# if os.path.exists("build/"):
#     print("cleaning existing build directory")
#     run("rm -r build/")

run("mkdir build/")
os.chdir("build")
print("getting jcef sources")
if env.jcef_version == "HEAD":
    run("git clone https://bitbucket.org/chromiumembedded/java-cef.git src")
else:
    # TODO: clone specific version??
    run(f"git clone {env.jcef_version}")
os.chdir("src")
run("mkdir jcef_build")
os.chdir("jcef_build")
print("generating cmake files")
run("cmake -G \"Unix Makefiles\" -DCMAKE_BUILD_TYPE=Release ..")
print("compiling")
run(f"make -j{os.cpu_count()}")
print("compiling java classes")
os.chdir("tools")
run("sh compile.sh linux64")
print("building release")
run("sh make_distrib.sh linux64")
