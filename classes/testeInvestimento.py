from classes import ContaInvestimento

conta = ContaInvestimento(1000.0, 10)
print(f"Saldo inicial: R$ {conta.saldo:.2f}")
conta.adicionarJuros()
conta.adicionarJuros()
conta.adicionarJuros()
conta.adicionarJuros()
conta.adicionarJuros()
print("Após 5 rodadas de juros...")
print(f"Saldo resultante: R$ {conta.saldo:.2f}")
