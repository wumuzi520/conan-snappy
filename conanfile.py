#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class GflagsConan(ConanFile):
    name = "snappy"
    version = "1.1.7"
    description = "The snappy package contains a C++ library that implements commandline flags processing. "
    url = "https://github.com/wumuzi520/conan-snappy"
    license = 'BSD 3-clause'
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt", "FindSnappy.cmake"]
    source_subfolder = "source_subfolder"
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"

    def source(self):
        source_url = "https://github.com/google/snappy"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version))
        os.rename("%s-%s" % (self.name, self.version), self.source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("FindSnappy.cmake", ".", ".")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
