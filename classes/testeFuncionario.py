from classes import Funcionario

func1 = Funcionario("João da Silva", 2350.0)
func2 = Funcionario("Maria das Dores", 5000.0)

print(f"Salário de {func1.nome}: R$ {func1.salario:.2f}")
print(f"Aumento de 20%: R$ {func1.aumentarSalario(20):.2f}")

print(f"\nSalário de {func2.nome}: R$ {func2.salario:.2f}")
print(f"Aumento de 50%: R$ {func2.aumentarSalario(50):.2f}")
