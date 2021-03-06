
%%----- Cell Locations -----

c(0, 0). c(0, 1). c(0, 2). c(0, 3). 
c(1, 0).          c(1, 2). c(1, 3). 
         c(2, 1). c(2, 2). c(2, 3). 
c(3, 0). c(3, 1).           

%%----- Pokemon Locations -----

         p(0, 1).                   p(0, 3).          
                  start(1, 2).                   
         end(2, 1).                   
p(2, 3).                                     

%%----------- Query -----------

%% agent(2, 1, 3, P, 0, S).

%%----------- Agent -----------

agent(1, 0, 0, [], 9, s0).

possible(down, X, Y):-
    X1 is X + 1,
    c(X1, Y).
possible(up, X, Y):-
	X1 is X - 1,
	c(X1, Y).
possible(right, X, Y):-
    Y1 is Y + 1,
    c(X, Y1).
possible(left, X, Y):-
    Y1 is Y - 1,
    c(X, Y1).
possible(catch, X, Y):-
    p(X, Y).
agent(X1, Y1, P1, Ploc1, H1, result(A, S)):-
	(agent(X, Y, P, Ploc, H, S), possible(A, X, Y), (
		(A = down,  X1 is X + 1, Y1 is Y, P1 is P, Ploc1 = Ploc, hatch(H, H1));
		(A = up,    X1 is X - 1, Y1 is Y, P1 is P, Ploc1 = Ploc, hatch(H, H1));
		(A = right, Y1 is Y + 1, X1 is X, P1 is P, Ploc1 = Ploc, hatch(H, H1));
		(A = left,  Y1 is Y - 1, X1 is X, P1 is P, Ploc1 = Ploc, hatch(H, H1));
		(A = catch, P1 is P + 1, X1 is X, Y1 is Y, H1 is H,
								\+member((X, Y), Ploc), Ploc1 = [(X, Y)|Ploc])
	)).

hatch(0, 0).
hatch(H, H1):-
	H1 is H - 1.

