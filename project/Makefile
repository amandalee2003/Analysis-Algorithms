#PYTHON = python3

# Source file
#SRC = MWST.py

# Executable name
#EXEC = MWST

# Default target
#all: $(EXEC)

# Rule to create an executable script
#$(EXEC): $(SRC)
#	echo "$(PYTHON) $(SRC)" > $(EXEC)
#	chmod +x $(EXEC)

# Clean up
#clean:
#	rm -f $(EXEC)


#target:
#	chmod u+x MWST.py
#
#

SRC = MWST.py
EXEC = MWST
all: $(EXEC)

$(EXEC): $(SRC)
	echo '#!/bin/sh' > $(EXEC)
	echo 'python3 $(SRC) "$$@"' >> $(EXEC)
	chmod +x $(EXEC)
clean:
	rm -f $(EXEC)
