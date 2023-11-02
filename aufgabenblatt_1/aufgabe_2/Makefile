CC=gcc
CFLAGS += -W -Wall -Wextra -Werror			#Pflicht
CFLAGS += -pedantic -fPIC   						#Optional
CFLAGS += -ggdb3 -DDEBUG -fno-stack-protector #-fsanitize=address

a2_1: 
	$(CC) -o a2_1 $(CFLAGS) a2_1.c 

clean:
	$(RM) a2_1
