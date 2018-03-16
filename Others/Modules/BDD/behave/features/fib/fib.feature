Feature:Calc Fib
    In order to introduce Behave
    We calc fib as example
  Scenario Outline: Calc fib number
     Given we have the number <number>
      when we calc the fib
      then we get the fib number <fib_number>
      Examples: Some Numbers
        | number    | fib_number |
        | 1         | 1          |
        | 2         | 2          |
        | 10        | 55         |