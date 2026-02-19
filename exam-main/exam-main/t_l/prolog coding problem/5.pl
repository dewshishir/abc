% Define a rule for addition
add_numbers(X, Y, Sum) :-
    Sum is X + Y.

% Example query:
% ?- add_numbers(5, 3, Result).
% Result = 8.
