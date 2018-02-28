from conans import ConanFile, CMake, tools


class SnappyConan(ConanFile):
    name = "snappy"
    version = "1.1.7"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Snappy here>"
    settings = "os", "compiler", "build_type", "arch"
    requires = "gflags/2.2.1@ant/stable"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://gitee.com/wumuzi520/snappy.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="snappy")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/snappy %s' % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="snappy")
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*snappy.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["snappy"]
