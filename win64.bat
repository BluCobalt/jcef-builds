git clone https://bitbucket.org/chromiumembedded/java-cef.git src
cd src
mkdir jcef_build
cd jcef_build
cmake -G "Visual Studio 16 2019" -A x64 ..
msbuild jcef.sln
cd ..
cd tools
compile.bat win64
make_distrib.bat win64
