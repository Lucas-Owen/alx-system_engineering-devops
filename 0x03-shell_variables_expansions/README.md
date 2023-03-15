# Shell, init files, variables and expansions

## Commands and topics
printenv  
set  
unset  
export  
alias  
unalias  
.  
source  
printf  

Expansions
Shell Arithmetic
Variables
Shell initialization files
The alias Command
Technical Writing

### 0-alias
A script that creates an alias.  
Name: `ls ` 
Value: `rm *`

### 1-hello_you
A script that prints `hello user`, where user is the current Linux user.

### 2-path
Add `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program.

### 3-paths
A script that counts the number of directories in the `PATH`.

### 4-global_variables
A script that lists environment variables.

### 5-local_variables
A script that lists all local variables and environment variables, and functions.

### 6-create_local_variable
Create a script that creates a new local variable.  
Name: `BEST`  
Value: `School`

### 7-create_global_variable
Create a script that creates a new global variable.  
Name: `BEST`  
Value: `School`

### 8-true_knowledge
A script that prints the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`, followed by a new line.

### 9-divide_and_rule
A script that prints the result of `POWER` divided by `DIVIDE`, followed by a new line.  
`POWER` and `DIVIDE` are environment variables

### 10-love_exponent_breath
A script that displays the result of `BREATH` to the power `LOVE`  
`BREATH` and `LOVE` are environment variables  
The script should display the result, followed by a new line

### 11-binary_to_decimal
A script that converts a number from base 2 to base 10.  
The number in base 2 is stored in the environment variable `BINARY`  
The script should display the number in base 10, followed by a new line

### 12-combinations
A script that prints all possible combinations of two letters, except `oo`.  
Letters are lower cases, from `a` to `z`  
One combination per line  
The output should be alpha ordered, starting with `aa`  
Do not print `oo`  
Your script file should contain maximum 64 characters

### 13-print_float
A script that prints a number with two decimal places, followed by a new line.  
The number will be stored in the environment variable `NUM`.

### 100-decimal_to_hexadecimal
A script that converts a number from base 10 to base 16.  
The number in base 10 is stored in the environment variable `DECIMAL`  
The script should display the number in base 16, followed by a new line

### 101-rot13
A script that encodes and decodes text using the rot13 encryption. Assume ASCII.  
```
julien@production-503e7013:~/shell/fun_with_the_shell$ cat quote
"Everyone is a proponent of strong encryption."
- Dorothy E. Denning
julien@production-503e7013:~/shell/fun_with_the_shell$ ./101-rot13 < quote
"Rirelbar vf n cebcbarag bs fgebat rapelcgvba."
- Qbebgul R. Qraavat
julien@production-503e7013:~/shell/fun_with_the_shell$
```

### 102-odd
A script that prints every odd line from the input, starting with the first line.

### 103-water_and_stir
A shell script that adds the two numbers stored in the environment variables `WATER` and `STIR` and prints the result.  
`WATER` is in base `water`  
`STIR` is in base `stir`.  
The result should be in base `bestchol`

## Quick Notes
### Shell Init files, variables and expansion  

#### Expansion - processes performed on text before carrying out the command
Arithmetic $((expression))  
expansion - {singlecharacter pattern} e.g {1..5} expands to 1 2 3 4 5  
expansion - $PARAMETER (empty string on typos)  
printenv - see a list of available variables  
Command substitution - $(command) or `command` e.g ls -l $(which cp)   
Quoting - the shell suppresses unwanted expansions. e.g removing extra spaces, returning empty strings with typos  
Double quotes-make all special characters lose meaning except $,\,`  
Single quotes-suppress all expansions  
Excaping characters - use backslash in double quotes, also to ignore new line in commands  
#### Init files  
/etc/profile : contains shell variables  
/etc/bashsrc : contains bash specific configurations  
.bash_profile : uses specific config  
.bash_login : contains specific settings loaded on login - read when .bash_profile is unavailable  
.profile  
.bashrc  
.bash_logout  

alias : used to set aliases for commands. Commands can be reset temporarily by backslashing  
	

