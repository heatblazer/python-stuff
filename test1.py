import sys
from PyQt4.QtCore import *
from PyQt4.QtXml import *

DBG = True


class XmlParser:
    def __init__(self):
        self.m_tags = dict()

    def loadFile(self, fname):
        f = QFile(fname)
        res = f.open(QIODevice.ReadOnly)
        if res > 0:
            reader = QXmlStreamReader(f.readAll())
            f.close()
            if reader.hasError():
                return False
            else:
                while not reader.atEnd():
                    reader.readNext()
                    if reader.isStartElement():
                        attribs = reader.attributes()
                        self.m_tags[reader.name()] = list()
                        for i in range(0, attribs.count()):
                            it = attribs.at(i)
                            v = it.value()
                            k = reader.name()
                            self.m_tags[k].append(v)
        else:
            return False


def main():
    xml = XmlParser()
    if len(sys.argv) <= 1:
        print ("provide xml file")
        return False
    else:
        xml.loadFile(sys.argv[1])


if __name__ == "__main__":
    main()
