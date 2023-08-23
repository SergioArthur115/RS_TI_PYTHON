from Disciplina import Disciplina

mat = Disciplina("Matemática", [6.3, 9.5])
print(f"Disciplina: {mat.nome}")
print(f"Notas: {mat.notas}")
print(f"Média: {mat.calcularMedia():.1f}")
print(f"Situação: {mat.exibirSituacao()}\n")

port = Disciplina("Português", [3.4, 5.2])
print(f"Disciplina: {port.nome}")
print(f"Notas: {port.notas}")
print(f"Média: {port.calcularMedia():.1f}")
print(f"Situação: {port.exibirSituacao()}\n")

fis = Disciplina("Fisíca", [1.0, 3.0])
print(f"Disciplina: {fis.nome}")
print(f"Notas: {fis.notas}")
print(f"Média: {fis.calcularMedia():.1f}")
print(f"Situação: {fis.exibirSituacao()}")