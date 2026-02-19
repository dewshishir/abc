% Knowledge Base (KB)
parent(alice, bob).
parent(bob, charlie).
parent(alice, dave).
male(bob).
female(alice).
% Check if a fact exists in the Knowledge Base
fact_exists(Fact) :-
    (   predicate_property(Fact, defined)
    ->  (   call(Fact)
        ->  write('The information exists in the Knowledge Base.'), nl
        ;   write('The information does NOT exist in the Knowledge Base.'), nl,
            fail
        )
    ;   write('The predicate is not defined in the Knowledge Base.'), nl,
        fail
    ).
