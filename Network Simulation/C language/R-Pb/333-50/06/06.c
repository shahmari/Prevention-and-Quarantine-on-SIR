#include <stdio.h>
#include<stdbool.h>
#include <stdlib.h>
#include <time.h>

#define dim 333

void initial_condition(bool ***nodes, bool **edges, float Ps, float Pb, float I0);
int simulation(bool ***nodes, bool **edges, float Ps, float Pb, int ND, float betta, float gamma, int snode[ND+1], int inode[ND+1], int rnode[ND+1]);
int randnode(int res[2][2]);
int min(int num1, int num2);

int main()
{
////////////////////////////////////////////////////
  float I0=0.01;
  int ND=65;
  float betta=1;
  float gamma=0.2;
  int snode[ND+1]; int inode[ND+1]; int rnode[ND+1];
////////////////////////////////////////////////////
  srand(time(0));
////////////////////////////////////////////////////
  bool ***nodes = (bool ***)malloc(dim * sizeof(bool**));
  bool **edges = (bool **)malloc(dim*2 * sizeof(bool*));

  for (int i = 0; i < dim; i++) {
    nodes[i] = (bool **)malloc(dim * sizeof(bool*));
    for (int j = 0; j < dim; j++)
      nodes[i][j] = (bool *)malloc(2 * sizeof(bool));
  }
  for (int i = 0; i < dim*2; i++)
    edges[i] = (bool *)malloc(dim * sizeof(bool));
////////////////////////////////////////////////////
  float Ps=0.6; int n; float Pb; int m;
  FILE *f = fopen("Ps06.csv", "w");
  for (Pb=0,m=0;Pb<0.99; Pb+=0.01 , m++){
    for (int i=0; i<50; i++){
			initial_condition(nodes, edges, Ps, Pb, I0);
      int data = simulation(nodes, edges, Ps, Pb, ND, betta, gamma, snode, inode, rnode);
      fprintf(f,"%d, ",data);
      printf("\rProcessing %d %% Completed and %d %% of the Total Computing Proceed ",i,m);
    }
    fprintf(f,"\n");
  }
  fclose(f);
  printf("\nit's Wednesday my dudes");
  return 0;
}
////////////////////////////////////////////////////
void initial_condition(bool ***nodes, bool **edges, float Ps, float Pb, float I0)
{
  for(int i = 0; i<dim;i++){
    for(int j = 0; j<dim; j++){
      nodes[i][j][0]=false;
      nodes[i][j][1]=false;
      }
    }

  for(int i = 0; i<2*dim;i++){
    for(int j = 0; j<dim; j++){
      edges[i][j]=false;
      }
    }

  for(int m = 0; m<dim*dim*I0;){
    int xrand = rand() % dim;
    int yrand = rand() % dim;
    if((nodes[xrand][yrand][1]==false) && (nodes[xrand][yrand][0]==false)){
      nodes[xrand][yrand][0]=true;
      ++m;
    }
  }

  for(int n = 0; n<dim*dim*Ps;){
    int xrand = rand() % dim;
    int yrand = rand() % dim;
    if((nodes[xrand][yrand][1]==false) && (nodes[xrand][yrand][0]==false)){
      nodes[xrand][yrand][1]=true;
      ++n;
    }
  }
  for(int p = 0; p<dim*dim*Pb;){
    int xrand = rand() % (2*dim);
    int yrand = rand() % dim;
    if(edges[xrand][yrand]==false){
      edges[xrand][yrand]=true;
      ++p;
    }
  }
}
////////////////////////////////////////////////////
int simulation(bool ***nodes, bool **edges, float Ps, float Pb, int ND, float betta, float gamma, int snode[ND+1], int inode[ND+1], int rnode[ND+1]){

  for(int nd_p=0; nd_p<=ND; nd_p++){

    for(int l=0; l<dim*dim; l++){
      int res[2][2];
      randnode(res);
      float rb = (float)rand()/(float)(RAND_MAX);
      if((nodes[res[0][0]][res[0][1]][0]==true) && (nodes[res[1][0]][res[1][1]][0]==false)){
        if((nodes[res[1][0]][res[1][1]][1]==false) && (betta>rb)
          && (edges[res[0][0]+res[1][0]][min(res[1][1],res[0][1])]==false)){
            nodes[res[1][0]][res[1][1]][0]=true;
        }
      }
////////////////////////////////////////////////////
      randnode(res);
      float rg = (float)rand()/(float)(RAND_MAX);
      if((nodes[res[0][0]][res[0][1]][0]==true) && (gamma>rb)){
        nodes[res[0][0]][res[0][1]][0]=false;
        nodes[res[0][0]][res[0][1]][1]=true;
      }
    }
  }
  ////////////////////////////////////////////////////////////////////
  int rnum=0;
  for(int i=0; i<dim; i++){
    for(int j=0; j<dim; j++){
      if((nodes[i][j][0]==false) && (nodes[i][j][1]==true)){rnum++;}
    }
  }
  ////////////////////////////////////////////////////////////////////
  return rnum;
}
////////////////////////////////////////////////////
int randnode(int res[2][2]){
  int x1=rand() % dim; int y1=rand() % dim; int r=rand() % 4;
  int adj[4][2]={{0,1},{1,0},{0,-1},{-1,0}};
  int x2=x1+adj[r][0]; int y2=y1+adj[r][1];
  if(x2==-1){x2=dim-1;}
  if(x2==dim){x2=0;}
  if(y2==-1){y2=dim-1;}
  if(y2==dim){y2=0;}
  res[0][0]=x1; res[0][1]=y1; res[1][0]=x2; res[1][1]=y2;
}
////////////////////////////////////////////////////
int min(int num1, int num2)
{
    return (num1 > num2 ) ? num2 : num1;
}
