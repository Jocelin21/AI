triangle(A, B, C) :-
    A + B + C =:= 180,
    ( A =:= 90; B =:= 90; C =:= 90),
    writeln('One of the angle is 90, so this is a right triangle').
triangle(A, B, C) :-
    A + B + C =\= 180,
    writeln('Total angle is not 180, so this is not a triangle'),!, fail.
triangle(_,_,_) :-
    writeln('None of the angle is 90, so this is not a right triangle'), fail.

