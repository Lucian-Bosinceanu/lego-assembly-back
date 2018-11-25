# Application flow

Here we put information about the flow of the application. An example would be:

In this application, the flow is the following:

- read the file from input
    - if the file content is valid, continue
    - else show an error and stop
- generate a structure using the given file, which is a graph
    - if the graph is valid then continue
    - else regenerate the structure
- convert the graph to a dictionary format
- write the given dictionary to a predefined file (or a file given as input)
    - if the file doesn't exist, create it
    - if we don't have permissions, show an error and stop

Also, include diagrams, use case scenarios, and so on.