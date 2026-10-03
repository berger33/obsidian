---
id: software.seguranca.tranche11.001054
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

# Execução Simbólica com **`SimState`** e **`SimulationManager` (`simgr.explore`)**: Navegando até Estados Alvo (`find`) e Podando Caminhos Inválidos (`avoid`)

## Em uma frase
Como automatizar a descoberta de uma entrada (via `stdin`, `argv` ou memória) que faz um binário alcançar uma função específica (como uma rotina de autenticação bem-sucedida ou um ponto vulnerável de *buffer overflow*) sem cair nos ramos de erro?

## Por que importa
O fluxo no `angr` segue três passos: **(1)** Criar um estado inicial com **`state = proj.factory.entry_state(...)`** (ou `blank_state(addr=...)` / `call_state(addr, arg1, ...)` para começar direto no meio de uma função!); **(2)** Criar um gerenciador de simulação com **`simgr = proj.factory.simulation_manager(state)`**; e **(3)** Executar **`simgr.explore(find=..., avoid=...)`**!

## Como funciona
À medida que o `SimulationManager` avança bloco a bloco (`simgr.step()`), os estados são organizados em listas chamadas **`stashes`**: `simgr.active` (caminhos sendo explorados), `simgr.found` (caminhos que atingiram a condição `find`), `simgr.avoid` (caminhos podados por `avoid`), `simgr.deadended` (caminhos que terminaram `exit()`) e `simgr.unconstrained` (caminhos onde o ponteiro de instrução `rip`/`pc` se tornou simbólico — indicando um **Control-Flow Hijack / Buffer Overflow**!)!

## Exemplo
```python
import angr

# Template padrao de exploracao simbolica com SimulationManager buscando um endereco/saida alvo e podando caminhos de falha
proj = angr.Project("/bin/false", auto_load_libs=False)
state = proj.factory.entry_state()
simgr = proj.factory.simulation_manager(state)

# find e avoid aceitam tanto enderecos (int/list) quanto funcoes lambda que inspecionam o stdout do estado (state.posix.dumps(1))!
simgr.explore(
    find=lambda s: b"Access Granted" in s.posix.dumps(1),
    avoid=lambda s: b"Invalid" in s.posix.dumps(1),
)

if simgr.found:
    win_state = simgr.found[0]
    print("Entrada para stdin:", win_state.posix.dumps(0))
```

## Limites e trade-offs
Olhe que poder expressivo: passar `find=lambda s: b"Access Granted" in s.posix.dumps(1)` dispensa até mesmo ter que procurar no disassembler o endereço hexadecimal do bloco `if/else` de sucesso — o `angr` monitora o descritor de arquivo `1` (`stdout` simulado no POSIX) de cada estado e para assim que encontra um caminho que imprime a string desejada!

## Como verificar
E para caça automática de vulnerabilidades de corrupção de memória (AEG — *Automatic Exploit Generation*), passe `save_unconstrained=True` no `simulation_manager`: qualquer estado que cair em `simgr.unconstrained` significa que a entrada simbólica conseguiu sobrescrever o endereço de retorno (`RIP`/`PC`)!

## Conexões
- [[angr-motor-solver-claripy-bitvectors-bvs-bvv-restricoes-z3]] — Veja também: Álgebra Simbólica no `angr` com **`claripy`**: Bitvectors Simbólicos (**`BVS`** vs **`BVV`**), Árvores AST e Resolução de Restrições com **Z3 (`state.solver`)**.
- [[angr-hooks-simprocedures-substituicao-funcoes-anti-debug-crypto]] — Veja também: Engenharia Reversa com **`@proj.hook`** e **`angr.SimProcedure`**: Neutralizando `ptrace` Anti-Debug, `sleep`, Loops Pesados e Funções Criptográficas.
- [[angr-arquitetura-analise-binaria-execucao-simbolica-cle-pyvex-claripy]] — Referência cruzada direta com angr-arquitetura-analise-binaria-execucao-simbolica-cle-pyvex-claripy.

## Fontes
- [angr Official GitHub — Platform-Agnostic Binary Analysis & Symbolic Execution Framework](https://raw.githubusercontent.com/angr/angr/master/README.md) — repositório oficial do `angr` cobrindo carregamento de binários, lifting para IR, execução simbólica, hooks e decompilação; consultado em 2026-10-03.
- [angr Official Documentation — Quickstart, Architecture & Foundational Research (`SoK`, `Driller`, `Firmalice`)](https://docs.angr.io/en/latest/quickstart.html) — documentação oficial do `angr` detalhando os subsistemas `CLE`, `PyVEX`, `Claripy`, `SimState`, `SimulationManager` e análises estáticas/concólicas; consultado em 2026-10-03.
