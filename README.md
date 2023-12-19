# **AsciiScript: An ASCII-Based Esoteric Coding Language**

AsciiScript is a nascent esoteric programming language that is being built on top of Python Programming Language which is currently under development. It embraces the simplicity and immediacy of ASCII characters, crafting them into a unique code canvas. If you're drawn to the unconventional and enjoy pushing the boundaries of programming, AsciiScript awaits.

**Key Features**
-
- Like any other language it has **Variable** Declaration.
- Loops? Nah! This has **Repetition**.
- Remember those traverse functions from Linked lists made in C language? Yeah! AsciiScript has **Traversing**
- Multiple data types? WHO USES THOSE! Use **NUM** instead.
- Never tried to remember any ASCII? Well, now you have to use **only ASCII** to write something on the screen.

**How to write in *AsciiScript***
-
*Syntax:*
`[Ascii code for a letter1] [Ascii code for a letter2] [Ascii code for a letter3] ....`
- Example 1: `65 67 85` The Output: `ACU`
- Example 2: `45 57 90` The Output: `-9Z`

**How to declare a *variable***
-
*Syntax:*
`{NUM[variable_name]=[value]}`
- Example 1: `{NUMi=9}`
- Example 2: `{NUMI=90}`

**How to use *Traversing***
-
*Syntax:*
`([Starting Ascii Value]->[Ending Ascii Value])`
- Example 1: `(77->87)` The Output: `MNOPQRSTUVW`
- Example 2: `(65->78)` The Output: `ABCDEFGHIJKLMN`

**How to use *Repetition***
-
### Repetition only works with Traversing
*Syntax:*
`([Starting Ascii Value]->[Ending Ascii Value])*[the amount of times you want to traverse]`
- Example 1: `(77->87)*3` The Output: `MNOPQRSTUVWMNOPQRSTUVWMNOPQRSTUVW`
- Example 2: `(65->78)*5` The Output: `ABCDEFGHIJKLMNABCDEFGHIJKLMNABCDEFGHIJKLMNABCDEFGHIJKLMNABCDEFGHIJKLMN`

**Rules**
- 
- Variables can only be single characters long and can only be **a -> z** or **A -> Z**.
- You may write without a newline, but I prefer writing with newline(s) included.
- While using *Traverse* the starting ASCII code must be bigger than the ending ASCII code.
- Values of the variables can be altered later in the code.
- *More Rules may be added in the future.*

**Sample Code of AsciiScript**
-
    {NUMi=9}
    {NUMi=10}

    45 57 90

    (65->98)

    (76->89)*3
The Output:
    ```-9ZABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abLMNOPQRSTUVWXYLMNOPQRSTUVWXYLMNOPQRSTUVWXY```

**Current Status**
-
AsciiScript is in its early stages of development. The syntax and semantics are actively evolving, and new features are being explored. This repository serves as a living document, tracking the language's progress and inviting collaboration.

**Getting Started**
-
- Download Python if you don't have it already.
- Clone this Repo
- Run the `interpreter.py` file
- When it asks you for the filename, give the path to the AsciiScript file you have created while maintaining the provided rules.
- It will generate the output
