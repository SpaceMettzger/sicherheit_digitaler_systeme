CC=gcc
CFLAGS += -W -Wall -Wextra -Werror					#Pflicht
CFLAGS += -pedantic -fPIC #-fsanitize=address		#Optional
CFLAGS += -ggdb3 -DDEBUG -fno-stack-protector 		

a3: 
	$(CC) -o a3 $(CFLAGS) a3.c 

clean:
	$(RM) a3
