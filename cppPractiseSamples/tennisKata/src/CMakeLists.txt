cmake_minimum_required(VERSION 2.6)

# sources exclusive for main executables only
SET(SRC
    main.cpp
)

# sources of libraries shared between main and test executables
SET (LIBRARY_SRC
    Tennis.cpp  
    Player.cpp  
)


message ("     ---> Configuring libraries shared for main and test executables: ${PROJECT_NAME}")
SET(PROJECT_NAME_LIB "${PROJECT_NAME}Lib")
ADD_LIBRARY (${PROJECT_NAME_LIB} SHARED ${LIBRARY_SRC})
SET_TARGET_PROPERTIES(${PROJECT_NAME_LIB} PROPERTIES OUTPUT_NAME ${PROJECT_NAME})

message ("     ---> Configuring main executables: ${PROJECT_NAME}")
ADD_EXECUTABLE(${PROJECT_NAME} ${SRC})
TARGET_LINK_LIBRARIES (${PROJECT_NAME} ${PROJECT_NAME_LIB})

install(TARGETS ${PROJECT_NAME} ${PROJECT_NAME_LIB} RUNTIME DESTINATION bin LIBRARY DESTINATION lib)
