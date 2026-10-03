---
id: software.seguranca.tranche11.001057
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

# Como Mitigar a **Explosão de Estados (*State Explosion*)** no `angr`: Técnicas de Exploração **`Veritesting`**, **`DFS`**, **`LoopSeer`**, **`LengthLimiter`** e **`LAZY_SOLVES`**

## Em uma frase
O maior desafio teórico e prático da Execução Simbólica é a **Explosão de Caminhos (*Path / State Explosion*)**: como o padrão do `SimulationManager` é explorar todos os caminhos em largura (*Breadth-First Search*), um simples loop de 64 iterações com um `if` simbólico dentro pode gerar $2^{64}$ estados e esgotar toda a memória RAM do servidor!

## Por que importa
Para domar a explosão de estados em programas reais, o `angr` oferece **Técnicas de Exploração Pluggáveis (`simgr.use_technique(...)`)** e opções de estado (`angr.options`): **(1) `angr.exploration_techniques.Veritesting()`** — implementa o algoritmo da CMU que alterna automaticamente entre execução simbólica dinâmica (DSE) e execução simbólica estática (SSE, fundindo estados que divergem e reconvergem rapidamente em blocos `if/else` simples!); **(2) `angr.exploration_techniques.DFS()`** — explora em profundidade mantendo apenas 1 caminho ativo por vez em memória;

## Como funciona
**(3) `angr.exploration_techniques.LoopSeer(cfg=cfg, bound=5)`** — limita quantas vezes um estado pode girar no mesmo loop!; e **(4) `angr.options.LAZY_SOLVES` + `ZERO_FILL_UNCONSTRAINED_MEMORY`**!

## Exemplo
```python
import angr

proj = angr.Project("/bin/true", auto_load_libs=False)
state = proj.factory.entry_state(
    add_options={
        angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY,
        angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS,
    }
)
simgr = proj.factory.simulation_manager(state)

# Ativar Veritesting (fusao estatica de ramificacoes simples) e DFS para controlar o consumo de memoria RAM
simgr.use_technique(angr.exploration_techniques.Veritesting())
simgr.use_technique(angr.exploration_techniques.DFS())
print("Tecnicas ativas no SimulationManager:", simgr._techniques)
```

## Limites e trade-offs
Dica obrigatória de higiene no `angr`: adicione sempre **`angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY`** e **`angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS`** ao criar um estado inicial! Isso elimina os avisos `WARNING | angr.storage.memory_mixins... | Filling memory/register with unconstrained symbolic bytes` e evita criar variáveis simbólicas desnecessárias para registradores não inicializados.

## Como verificar
Outra técnica avançada é o **`Symbion`**: ele executa o programa concretamente em um debugger real (**GDB / Pwndbg** ou **QEMU**) até a função que você quer analisar, tira um snapshot concreto do estado da memória e transfere apenas aquele ponto para o `angr`!

## Conexões
- [[angr-analise-estatica-cfgfast-cfgemulated-decompilador-reaching-definitions]] — Veja também: Análise Estática e Decompilação no `angr`: **`CFGFast` vs `CFGEmulated`**, Grafo de Dependências (**`DDG` / `ReachingDefinitions`**) e **`Decompiler`**.
- [[angr-execucao-concolica-hibrida-fuzzing-driller-afl-qiling-unicorn]] — Veja também: Execução Concólica Híbrida e Fuzzing Assistido por Solver (**`Driller`**) & Engine Nativa **Unicorn (`angr.options.UNICORN`)**.
- [[angr-arquitetura-analise-binaria-execucao-simbolica-cle-pyvex-claripy]] — Referência cruzada direta com angr-arquitetura-analise-binaria-execucao-simbolica-cle-pyvex-claripy.
- [[angr-execucao-simbolica-simstate-simulation-manager-explore-find-avoid]] — Referência cruzada direta com angr-execucao-simbolica-simstate-simulation-manager-explore-find-avoid.
- [[pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto]] — Referência cruzada direta com pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto.

## Fontes
- [angr Official GitHub — Platform-Agnostic Binary Analysis & Symbolic Execution Framework](https://raw.githubusercontent.com/angr/angr/master/README.md) — repositório oficial do `angr` cobrindo carregamento de binários, lifting para IR, execução simbólica, hooks e decompilação; consultado em 2026-10-03.
- [angr Official Documentation — Quickstart, Architecture & Foundational Research (`SoK`, `Driller`, `Firmalice`)](https://docs.angr.io/en/latest/quickstart.html) — documentação oficial do `angr` detalhando os subsistemas `CLE`, `PyVEX`, `Claripy`, `SimState`, `SimulationManager` e análises estáticas/concólicas; consultado em 2026-10-03.
