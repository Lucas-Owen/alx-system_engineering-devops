# Shell, permissions
## Commands covered
chmod  
sudo  
su  
chown  
chgrp  
id  
groups  
whoami  
adduser  
useradd  
addgroup  

## Files
### 0-iam_betty
Switches the current user to the user betty.
Use exactly 8 characters for the command (+1 character for the new line)

### 1-who_am_i
Prints the effective username of the current user.

### 2-groups
Prints all the groups the current user is part of.

### 3-new_owner
Changes the owner of the file hello to the user betty.

### 4-empty
Creates an empty file called hello.

### 5-execute
Adds execute permission to the owner of the file hello.
The file hello will be in the working directory

### 6-multiple_permissions
Adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
The file hello will be in the working directory

### 7-everybody
Adds execution permission to the owner, the group owner and the other users, to the file hello  
The file hello will be in the working directory  
No using commas for this script  

### 8-James_Bond
Sets the permission to the file hello as follows:  
-Owner: no permission at all  
-Group: no permission at all  
-Other users: all the permissions  
The file hello will be in the working directory  
No using commas for this script

### 9-John_Doe
Sets the mode of the file hello to this:  
```
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
```

### 10-mirror_permissions
Sets the mode of the file hello the same as olleh’s mode.  
The file hello will be in the working directory  
The file olleh will be in the working directory 

### 11-directories_permissions
Adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.

### 12-directory_permissions
Creates a directory called my_dir with permissions 751 in the working directory.

### 13-change_group
Changes the group owner to school for the file hello  
The file hello will be in the working directory  

### 100-change_owner_and_group
Changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.

### 101-symbolic_link_permissions
Changes the owner and the group owner of _hello to vincent and staff respectively.  
The file _hello is in the working directory  
The file _hello is a symbolic link  

### 102-if_only
Changes the owner of the file hello to betty only if it is owned by the user guillaume.  
The file hello will be in the working directory

### 103-Star_Wars
Plays the StarWars IV episode in the terminal.
