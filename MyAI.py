# ======================================================================
# FILE:        MyAI.py
#
# AUTHOR:      Abdullah Younis
#
# DESCRIPTION: This file contains your agent class, which you will
#              implement. You are responsible for implementing the
#              'getAction' function and any helper methods you feel you
#              need.
#
# NOTES:       - If you are having trouble understanding how the shell
#                works, look at the other parts of the code, as well as
#                the documentation.
#
#              - You are only allowed to make changes to this portion of
#                the code. Any changes to other portions of the code will
#                be lost when the tournament runs your code.
# ======================================================================

from Agent import Agent

class MyAI ( Agent ):

    position = (0,0)
    map = {}
    visited  = set();
    action_Buff = [];  # when action buffer is not empty, excute action without check states
      # N = 4 in this case


    def __init__ ( self ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        
        pass
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

    def getAction( self, stench, breeze, glitter, bump, scream ):
        # ======================================================================
        # YOUR CODE BEGINS
        # =================================================== ===================
        # 0,none 1,breeze, 2.stench 3.glitter 4.scream 5.bump 6.breeze and stench
        if(breeze and stench):
            self.mark(6);
        elif(breeze):
            self.mark(1);
            if(breeze == (0,0)):
                return Agent.Action.CLIMB;
        elif(stench):
            self.mark(2);
        elif(glitter):
            return Agent.Action.GRAB;
        elif(scream):
            self.mark(4);
        elif(bump):
            self.mark(5);
        else:
            self.mark(0);

        return Agent.Action.CLIMB
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================
    
    # ======================================================================
    # YOUR CODE BEGINS
    # ======================================================================
    def in_bound(self,i):
        if(i>=0):
            return 1;
        return 0;



    def mark(self,sensor):
        self.visited.add(self.position);
        x = self.position[0]
        y = self.position[1]



        self.map[(x,y)] = 1;

        if (x+1,y) not in self.map.keys():
            self.map[(x+1,y)] = 0;
        self.mark_coordinate(x+1,y,sensor);

        if(x,y+1) not in self.map.keys():
            self.map[(x,y+1)] = 0;
        self.mark_coordinate(x,y+1,sensor);

        if (x-1,y) not in self.map.keys():
            self.map[(x-1,y)] = 0;
        self.mark_coordinate(x-1,y,sensor);


        if (x,y-1) not in self.map.keys():
            self.map[(x,y-1)] = 0;
        self.mark_coordinate(x,y-1,sensor);


        return;


    def mark_coordinate(self,x,y,sensor):
        if (self.in_bound(x) and self.in_bound(y) and  ((x, y) not in self.visited) and self.map[(x, y)] != 1 and self.map[(x, y)] != 4 and self.map[(x, y)] != 5):  # Mark grid should not be visited nor confirmed
            if (sensor == 0):
                self.map[(x, y)] = 1;
            elif sensor == 1:
                self.map[(x, y)] = 2;
            elif sensor == 2:
                self.map[(x, y)] = 3;
            elif sensor == 3:
                for k in map:
                    if (map[k] == 3):
                        map[k] = 1;
            elif sensor == 6 :
                self.map[(x,y)] = 6;




    # ======================================================================
    # YOUR CODE ENDS
    # ======================================================================