TEMPLATE = lib
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += \
    simplemodule.c

HEADERS +=


INCLUDEPATH += I/usr/include/python
LIBS += -L/usr/lib64/python2.7 -lpython2.7
