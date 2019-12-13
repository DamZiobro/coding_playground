#! /bin/bash
#
# test_git.sh
# This script tests git commands and git graph.
# In order to have `git graph` command add this line to section [alias] for your $HOME/.gitconfig file:
#[alias]
#    graph  = log --graph --abbrev-commit --decorate --date=relative --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all

mkdir /tmp/testgit
cd /tmp/testgit
git init . 

cat a > test.txt 
git add . 
git commit -m "first commit" 
git graph

git checkout -b branch-1 # create branch 'branch-1' and switch to it
echo b >> text.txt 
git add . 
git commit -m "first commit to branch-1"
git graph

echo b >> text.txt 
git add . 
git commit -m "second commit to branch-1"
git graph

git checkout -b branch-2-from-branch-1
echo b >> text.txt 
git add . 
git commit -m "first commit to branch-2-from-branch-1"
git graph

echo b >> text.txt 
git add . 
git commit -m "second commit to branch-2-from-branch-1"
git graph

git checkout branch-1 #switch to already existing branch branch-1
echo b >> text2.txt 
git add . 
git commit -m "second commit to branch-2-from-branch-1"
git graph

echo b >> text2.txt 
git add . 
git commit -m "second commit to branch-2-from-branch-1"
git graph

git merge branch-2-from-branch-1
git graph

echo b >> text.txt 
git add . 
git commit -m "1st commit to master"
git graph

git checkout master #switch to already existing branch braster
echo b >> text3.txt 
git add . 
git commit -m "2nd commit to master"
git graph

echo b >> text3.txt 
git add . 
git commit -m "third commit to master"
git graph

git merge branch-1
git graph

