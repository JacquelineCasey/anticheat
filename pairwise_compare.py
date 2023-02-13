# Compares a specific file across submissions in a directory.

import click

import itertools
import os
import subprocess


@click.command()
@click.option('--usernames-file', '--usernames', '-u',
    default='.anticheat/usernames.txt',
    help='List of usernames to compare. Defaults to .anticheat/usernames.txt')
@click.option('--compare-file', '--file', '-f',
    required=True,
    help='File to compare across repositories')
@click.option('--assignment', '-a',
    required=True,
    help='Github classroom assignment name')
def pairwise_compare(usernames_file, compare_file, assignment):
    if not os.path.isfile(usernames_file):
        print(f'Error: Could not find usernames file {usernames_file}. Aborting.')
        return

    with open(usernames_file, 'r') as file:
        usernames = [line.strip() for line in file.readlines()]

    for username in usernames:
        if not os.path.isdir(f'{assignment}-{username}') or \
        not os.path.isfile(f'{assignment}-{username}/{compare_file}'):
            print(f'Note: Could not find submission {assignment}-{username}/{compare_file}')
            usernames.remove(username)

    results = []
    for (user_a, user_b) in itertools.combinations(usernames, 2):
        p = subprocess.Popen(['diff', f'{assignment}-{user_a}/{compare_file}', f'{assignment}-{user_b}/{compare_file}'],
            stdout=subprocess.PIPE, 
            text=True
        )
        return_code = p.wait()
        assert return_code >= 0  # negative means errors for diff.

        diff_output, _ = p.communicate()  # Rudimentary measure of similarity
        results.append((user_a, user_b, len(diff_output.splitlines())))


    results.sort(key=lambda tup: tup[2])

    print('\n'.join([str(r) for r in results[:100]]))



if __name__=='__main__':
    pairwise_compare()
