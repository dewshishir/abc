% Import necessary libraries
:- use_module(library(readutil)).

% Predicate to count the number of words in a file
count_words_in_file(File, WordCount) :-
    open(File, read, Stream),             % Open the file for reading
    read_stream_to_codes(Stream, Codes),  % Read the content of the file as codes
    close(Stream),                        % Close the file stream
    atom_codes(Atom, Codes),              % Convert codes to an atom
    atomic_list_concat(Words, ' ', Atom), % Split atom into words by spaces
    exclude(=( '' ), Words, FilteredWords), % Remove any empty strings from list
    length(FilteredWords, WordCount).     % Count the words
