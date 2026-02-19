% Base case: The sum of an empty list is 0.
sum_list([], 0).

% Recursive case: Separate the head and the tail of the list, add the head to the sum of the tail.
sum_list([Head|Tail], Sum) :-
    sum_list(Tail, TailSum),       % Recursively sum the tail of the list
    Sum is Head + TailSum.          % Add the head to the sum of the tail
