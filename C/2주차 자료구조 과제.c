#include <stdio.h>

struct result_type {
   unsigned int student_number; 
   char name[100];
   int grading[4];
}; 

void insert_student(struct result_type x, struct result_type* std_array, int i) {
  std_array[i] = x;
  return;
}

void print_infos(struct result_type* std_array, int n){
   for(int i=0; i<n; i++){
      struct result_type info = std_array[i];
      printf("%d %s %d %d %d %d %d", 
      info.student_number, 
      info.name, 
      info.grading[0],
      info.grading[1],
      info.grading[2],
      info.grading[3],
      info.grading[0] + info.grading[1] + info.grading[2] + info.grading[3]);
   }   
   return;
}

void main() {
   struct result_type std_array[4];
   
   
}
