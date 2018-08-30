# Borg backup role - Molecule testing

Requirements:


Ansible 2.4 or higher
Molecule 2.17.0 or higher

Docker host (local or remote through shell environment)

## Available tests

All scenarios run the same tests by default defined in generic_tests

### all

Verify the borg-binary is present

### client

Verifies if all the required parameters are present on the client to perform a backup. It verifies an already existing backup has run and if it has succeeded.

### server

Verifies if all server-related configurations are in place and if the backup is working from a server perspective.


## Available test-scenarios

### clients

This tests spins up supported platforms and verifies the basic functionality of both server and client with the generic_tests.

```
borgbackup_appendonly:
borgbackup_servers:
borgbackup_include:
borgbackup_passphrase:
```

### commands

Verify if both pre and post commands are configured at backup time and are run.

```
borgbackup_pre_commands:
borgbackup_post_commands:
```

### folders

Verify if both inclusion and exclusion of folders is working as expected

```
borgbackup_include:
borgbackup_exclude:
```

### lamp

Verify a basic lamp setup meaning making sure /var/www/ and automysqlbackup is configured properly and backed up.
As an extra preparation, apache2 and automysqlbackup are installed for verification.


```
backup_pre_commands: needs to be extended with automysqlbackup
borgbackup_include: need to contain both /var/www and /var/lib/automysqlbackup
```

### multiple

Testing whether backing up to multiple targets works properly.

```
borgbackup_servers:
```

### mgt

Testing whether the management-station functionality works

```
borgbackup_management:
borgbackup_management_user:
borgbackup_management_sshkey:
```

### restore


