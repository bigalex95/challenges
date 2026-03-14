cmake_minimum_required(VERSION 3.22)
project(BaykarCVMapping LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# ── Dependencies ─────────────────────────────────────────────────────────────
find_package(Eigen3 3.3 REQUIRED NO_MODULE)
find_package(GTest REQUIRED)
find_package(nlohmann_json 3.2.0 REQUIRED)

# ── Library ──────────────────────────────────────────────────────────────────
add_library(depth_densifier_lib
    src/depth_densifier.cpp
)
target_include_directories(depth_densifier_lib PUBLIC
    ${PROJECT_SOURCE_DIR}/src
)
target_link_libraries(depth_densifier_lib PUBLIC
    Eigen3::Eigen
)

# ── Tests ────────────────────────────────────────────────────────────────────
enable_testing()

add_executable(depth_densifier_test
    test/depth_densifier_test.cpp
)
target_link_libraries(depth_densifier_test PRIVATE
    depth_densifier_lib
    GTest::gtest_main
)

include(GoogleTest)
gtest_discover_tests(depth_densifier_test)
