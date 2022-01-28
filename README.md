# EulerProjectDotNet
 
![Project Euler Profile Image](https://projecteuler.net/profile/Plankt0n.png)

Mit Python gelöste Probleme des Project Euler.

* [Largest product in a grid](https://projecteuler.net/problem=11)
* [Large sum](https://projecteuler.net/problem=13)
* [Power digit sum](https://projecteuler.net/problem=16)
* [Counting Sundays](https://projecteuler.net/problem=19)
* [Factorial digit sum](https://projecteuler.net/problem=20)


# Sudoku Solver
Realisierung eines Backtracking-Algorythmus zum lösen von Sudokus.
Dieser funktioniert so, dass er die erste frei Zelle sucht, dort eine Zahl einsetzt und diese prüft. Ist sie gültig, verletzt als keine der Sudoku-Regeln, wird die nächste freie Zelle gesucht. Es werden wieder von 1 beginnend die Zahlen eingesetzt und geprüft. Wird die Zahl 9 erreicht und keine ist gültig, geht der Algorythmus eine Zelle zurück und erhöht diese soweit, bis eine neue gültige Zahl eingesetzt wurde.