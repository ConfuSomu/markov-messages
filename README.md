Markov chains from messages
----

This project's objective is to allow users to generate Markov chains from messages that are sourced from different messaging platforms. Current supported platforms are the proprietary Discord instant messager. I have plans to add support for the ActivityPub format.

You first need to generate a file containing messages (like a file named `messages`) from all desired sources then you can run `markov.py` to have a random message generated. To create a messages file (or append to one if it already exists), run one of the `export-*` scripts. Please follow the usage that's printed when running the script without any arguments.

Separating the scripts that generate the messages file from the files that generate the messages allows adding message sources and other generation algorithms with ease. None of the files are expected to be run standalone, though they can be; they can be easily `import`ed into other Python scripts for more complex uses.

The main `markov.py` file generates messages by using the text present in the specified messages file and of the specified length in number of words.

## Example usage of `markov.py`
```
$ python3 markov.py messages 3
Namespace a Pi
$ python3 markov.py messages 3
Donné vendredi? cat
$ python3 markov.py messages 5
Design made an NTFS filesystem?
```
As shown, the second argument passed to the script controls the length of the generated message. The first argument controls the source file that's used for messages.
