#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <stdbool.h>
#include <fcntl.h>
#include <dirent.h>

#include "helper.h"

static void usage() {
  fputs("Usage: ./client file\n",stderr);
  exit(EXIT_FAILURE);
}


void send_file(int fd, int sockfd, const char *filename){
  if (write(sockfd, filename, strlen(filename)) < 1) ERROR(filename);
  fsync(sockfd);
  usleep(TIMEOUT);
  while(true) {
    char buf[BUF_LEN];
    int n = read(fd, buf, BUF_LEN);
    if(n == 0) break;
    
    if (write(sockfd, buf, n) <0) error(true, errno,"%s", filename);
  }
}


int open_server_connection( const char *ip, const int port) {
  int sockfd = socket(AF_INET, SOCK_STREAM, 0);
  if(sockfd < 0) ERROR("socket");
  

  struct sockaddr_in server_addr;  
  server_addr.sin_family = AF_INET;
  server_addr.sin_port =  htons(port);
  server_addr.sin_addr.s_addr = inet_addr(ip);

  if ( connect(sockfd, (struct sockaddr*)&server_addr,
               sizeof(server_addr)) == -1)  ERROR("connect");

  return sockfd;
}


int main(int args, char *argv[]){
  if(args != 2) usage();
  
  const char *ip = "127.0.0.1";
  //const char *ip = "192.168.2.108";
    

  int sockfd = open_server_connection(ip,SERVER_PORT);
  
  int fd = open(argv[1], O_RDONLY);
  if (fd <0) ERROR(argv[1]);
  
  send_file(fd, sockfd, argv[1]);

  close(fd);
  close(sockfd);
}
