CC=gcc
CFLAGS += -W -Wall -Wextra # -Werror			#Pflicht
CFLAGS += -pedantic -fPIC   						#Optional
CFLAGS += -ggdb3 -DDEBUG -fno-stack-protector #-fsanitize=address

a1_1: 
	$(CC) -o a1_1 $(CFLAGS) a1_1.c 

clean:
	$(RM) a1_1
