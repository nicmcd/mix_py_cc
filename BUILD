cc_library(
    name = "cc_Foo",
    srcs = ["Foo.cc"],
    hdrs = ["Foo.h"],
)

py_library(
    name = "py_Foo",
    srcs = ["Foo.py"],
    data = [":cc_Foo"],
)

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [":py_Foo"],
)
