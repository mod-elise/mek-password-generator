# Planning document Think Employment secure password generator

This document details the planning for a secure password generator to be coded in one afternoon.

## The problem to be solved

When picking a password humans typically choose words or phrases they are familiar with and can remember.  They will reuse passwords using familiar patterns such as a loved one's name, dates and such.  Passwords based off dates or words are easy to crack using brute force methods.

This generator will make cryptographically strong passwords easy to generate, with flexibility in password rules (length, symbols, numbers, capital letters and such) and will make it easy to copy the results to the clipboard for use.

## Inputs

* Password length (6-20) (slider or text)
* Include Uppercase (checkbox)
* Include Numbers (checkbox)
* Include Special Characters (checkbox)
* Option to avoid ambiguous characters like (1,l) and (0,O)
* A Generate Button
* Copy To clipboard button

**Power user mode:  Maybe have an option to include something like an open text area to type in custom set like: u3n4s2 which might mean the password must contain three upper case letters, four numbers and two special characters**

## Outputs

A text field of some kind that displays a secure password like
b7!kP$2zQw

Maybe a strength indicator if this seems feasible?

## Extras

* a show/hide password toggle
* Passphrase generator as with xkcd's method: https://xkcd.com/936/
