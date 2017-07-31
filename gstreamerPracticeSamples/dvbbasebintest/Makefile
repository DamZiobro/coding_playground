#
# Makefile
#

all:
	@echo "Building dvbbasebintest..."
	gcc dvbbasebin.c -o dvbbasebin `pkg-config --cflags --libs gstreamer-1.0`
	@echo "Building finished."

alt: 
	@echo "Building alternative version..."
	gcc main.c -o dvbbasebin `pkg-config --cflags --libs gstreamer-1.0`
	@echo "Building finished."


run: 
	GST_DEBUG=*:2 ./dvbbasebin

memcheck: 
	@echo "Memory testing..."
	GST_DEBUG=*:2 memorycheck ./dvbbasebin 120
	@echo "Memory testing finished"

