#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <stdbool.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <pthread.h>
#include <libgen.h>

#include "helper.h"

void write_file(int sockfd){
  char buf[BUF_LEN];

  int n = read(sockfd, buf, BUF_LEN-1);
  if(n<0) ERROR("read");
  buf[n] = '\0'; 
  char *bn = basename(buf);
  int fd = open(bn, O_CREAT | O_WRONLY | O_EXCL, 0664);
  
  if(fd<0) WARN(buf);
  while (true) {
    n = read(sockfd, buf, BUF_LEN);
    if (n <= 0) break;
    if (write(fd,buf,n) != n) ERROR("write");
  }
  close(fd);
}


void* client_handler(void *sockfd) {
  int *socket = sockfd;
  write_file(*socket);
          
  close(*socket);
  free(sockfd);
  return NULL;
}

int open_server_socket(const char *ip, int port) {
  int sockfd = socket(AF_INET, SOCK_STREAM, 0);
  if(sockfd < 0) ERROR("socket");
  
  struct sockaddr_in server_addr;
  bzero(&server_addr, sizeof(server_addr)); 
  server_addr.sin_family = AF_INET;
  server_addr.sin_port = htons(port);
  server_addr.sin_addr.s_addr = inet_addr(ip);

  if ( bind(sockfd, (struct sockaddr*) &server_addr, sizeof(struct sockaddr_in)) != 0)
    ERROR("bind");

  if(listen(sockfd, 10) != 0) ERROR("listen");
  return sockfd;
}



int main(){
  const char *ip = "127.0.0.1";

  int sockfd = open_server_socket(ip, SERVER_PORT);

#ifndef DEBUG
  if( daemon(true, true) == -1) ERROR("daemon");
#endif
  
  pthread_t t;
  struct sockaddr_in new_addr;
  while(true) { 
    socklen_t  addr_size = sizeof(new_addr);
    int *sockp = malloc(sizeof(int));
    *sockp = accept(sockfd, (struct sockaddr*) &new_addr, &addr_size);
    
    if (pthread_create(&t, NULL, client_handler, sockp)) WARN("pthread_create");
    pthread_detach(t);
  }  

}
