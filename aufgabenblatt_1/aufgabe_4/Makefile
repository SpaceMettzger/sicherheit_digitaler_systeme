CFLAGS += -O2  -W -Wall -Wextra -Werror 
DEBUG  += -ggdb2 -fsanitize=address -DDEBUG
all: client server 

debug: CFLAGS += $(DEBUG)
debug: all



server: CFLAGS +=-pthread
server: 


clean:
	$(RM) *~ server client 
