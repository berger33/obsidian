---
id: software.seguranca.tranche11.001053
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/angr/angr/master/README.md", "https://docs.angr.io/en/latest/quickstart.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Álgebra Simbólica no `angr` com **`claripy`**: Bitvectors Simbólicos (**`BVS`** vs **`BVV`**), Árvores AST e Resolução de Restrições com **Z3 (`state.solver`)**

## Em uma frase
Qual é a diferença fundamental entre executar um programa normalmente na CPU e executá-lo simbolicamente no `angr`? Na CPU real, o registrador `rax` ou um buffer de entrada contém um valor concreto fixo (ex.: `0x41414141`); no `angr`, eles podem conter uma **Variável Matemática Simbólica (`BitVector Symbolic — BVS`)** gerenciada pela biblioteca **`claripy`**!

## Por que importa
No `claripy`, você manipula dois tipos principais de Bitvectors: **(1) `claripy.BVV(valor, bits)` (*BitVector Value*)** — representa um número concreto com largura em bits exata (ex.: `claripy.BVV(0xdeadbeef, 32)`); e **(2) `claripy.BVS("nome", bits)` (*BitVector Symbolic*)** — representa uma incógnita de `N` bits (ex.: `flag = claripy.BVS("flag", 8 * 16)` para uma senha de 16 bytes!).

## Como funciona
Quando o binário faz operações aritméticas ou bit-a-bit (`+`, `^`, `<<`, `*`) sobre `flag`, o `angr` constrói automaticamente uma **Árvore de Sintaxe Abstrata (AST)** da expressão; e quando o programa chega a um desvio condicional (`if (hash(flag) == 0x1337)`), o **`state.solver` (Z3)** resolve o sistema de equações (`state.solver.eval(flag, cast_to=bytes)`) para descobrir qual entrada satisfaz a condição!

## Exemplo
```python
import claripy

# Criar um Bitvector Simbolico de 4 bytes (32 bits) com Claripy e usar o Solver Z3 para descobrir a entrada que satisfaz uma equacao XOR/ADD
 solver = claripy.Solver()
x = claripy.BVS("chave_secreta", 32)

# Adicionar restricoes: cada byte deve ser ASCII imprimivel (0x20..0x7e) e ((x ^ 0x1337beef) + 0x10203040) == 0x628b0043
for byte in x.chop(8):
    solver.add(byte >= 0x20, byte <= 0x7E)
solver.add(((x ^ 0x1337BEEF) + 0x10203040) == 0x628B0043)

solucao = solver.eval(x, 1)[0].to_bytes(4, "big")
print("Solucao encontrada pelo Claripy/Z3:", solucao)
```

## Limites e trade-offs
Repare no método **`x.chop(8)`** do exemplo acima: ele fatia um Bitvector simbólico de `N` bits em uma lista de Bitvectors de `8` bits (1 byte cada), permitindo adicionar facilmente restrições por caractere (como exigir que a entrada gerada contenha apenas caracteres ASCII alfanuméricos ou comece com o prefixo `CTF{`)!

## Como verificar
Em um `SimState` do `angr`, o solver está sempre acessível em `state.solver` (com métodos `state.solver.add(...)`, `state.solver.satisfiable()`, `state.solver.eval(ast, cast_to=bytes)`).

## Conexões
- [[angr-carregador-binarios-cle-shared-libraries-firmware-blobs-base-addr]] — Veja também: O Carregador **`CLE` (*CLE Loads Everything*)** do `angr`: Espaço de Endereçamento, Posição Independente (`PIE`), Bibliotecas Compartilhadas e **Firmware Raw (`Blob`)**.
- [[angr-execucao-simbolica-simstate-simulation-manager-explore-find-avoid]] — Veja também: Execução Simbólica com **`SimState`** e **`SimulationManager` (`simgr.explore`)**: Navegando até Estados Alvo (`find`) e Podando Caminhos Inválidos (`avoid`).
- [[angr-arquitetura-analise-binaria-execucao-simbolica-cle-pyvex-claripy]] — Referência cruzada direta com angr-arquitetura-analise-binaria-execucao-simbolica-cle-pyvex-claripy.
- [[ropper-busca-semantica-pyvex-z3-solver-restricoes-registradores]] — Referência cruzada direta com ropper-busca-semantica-pyvex-z3-solver-restricoes-registradores.

## Fontes
- [angr Official GitHub — Platform-Agnostic Binary Analysis & Symbolic Execution Framework](https://raw.githubusercontent.com/angr/angr/master/README.md) — repositório oficial do `angr` cobrindo carregamento de binários, lifting para IR, execução simbólica, hooks e decompilação; consultado em 2026-10-03.
- [angr Official Documentation — Quickstart, Architecture & Foundational Research (`SoK`, `Driller`, `Firmalice`)](https://docs.angr.io/en/latest/quickstart.html) — documentação oficial do `angr` detalhando os subsistemas `CLE`, `PyVEX`, `Claripy`, `SimState`, `SimulationManager` e análises estáticas/concólicas; consultado em 2026-10-03.
