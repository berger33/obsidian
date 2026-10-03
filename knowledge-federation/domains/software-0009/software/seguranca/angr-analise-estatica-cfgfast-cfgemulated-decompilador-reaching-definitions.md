---
id: software.seguranca.tranche11.001056
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

# Análise Estática e Decompilação no `angr`: **`CFGFast` vs `CFGEmulated`**, Grafo de Dependências (**`DDG` / `ReachingDefinitions`**) e **`Decompiler`**

## Em uma frase
O `angr` não é apenas um motor de execução simbólica: o namespace **`proj.analyses`** contém uma suíte completa de **Análise Estática de Fluxo de Controle, Fluxo de Dados e Decompilação Programática** (que inclusive alimenta a interface gráfica oficial **`angr-management`**)!

## Por que importa
O alicerce de todas as análises estáticas é a construção do **Control Flow Graph (CFG)**: **(1) `cfg = proj.analyses.CFGFast()`** — reconstrói o grafo de fluxo de controle e identifica todas as funções do binário em segundos usando heurísticas estáticas, resolução de tabelas de salto (*jump tables*) e análise leve de fluxo de dados (sendo a escolha recomendada em 95% dos casos!); e **(2) `proj.analyses.CFGEmulated()`** — usa execução simbólica forçada para resolver saltos indiretos complexos.

## Como funciona
Uma vez construído o `CFGFast`, você pode rodar o **Decompilador em Python (`dec = proj.analyses.Decompiler(func, cfg=cfg.model)`)** para gerar código C estruturado de qualquer função, ou rodar **`proj.analyses.ReachingDefinitions`** para rastrear *taint analysis* estático (ex.: verificar se um parâmetro vindo da rede chega sem sanitização até o primeiro argumento de `system()`)!

## Exemplo
```python
import angr

# Construir o Control Flow Graph rapido (CFGFast) e decompilar programaticamente a funcao 'main' para codigo C em Python!
proj = angr.Project("/bin/true", auto_load_libs=False)
cfg = proj.analyses.CFGFast(normalize=True)

main_func = cfg.kb.functions.function(name="main") or cfg.kb.functions[proj.entry]
decomp = proj.analyses.Decompiler(main_func, cfg=cfg.model)
if decomp.codegen:
    print(decomp.codegen.text)
```

## Limites e trade-offs
Por que ter um **Decompilador C acessível em 5 linhas de Python (`decomp.codegen.text`)** dentro do `angr` é revolucionário para pesquisa de vulnerabilidades em escala (e integração com LLMs de auditoria de código)? Porque você pode iterar automaticamente sobre milhares de funções de dezenas de binários de firmware, decompilar apenas as funções que chamam sinks perigosos (`strcpy`, `popen`, `sprintf`, `ioctl`) e analisar o código C resultante em lote!

## Como verificar
Explore também `proj.analyses.BackwardSlice` e `proj.analyses.VariableRecoveryFast` na base de conhecimento `proj.kb`.

## Conexões
- [[angr-hooks-simprocedures-substituicao-funcoes-anti-debug-crypto]] — Veja também: Engenharia Reversa com **`@proj.hook`** e **`angr.SimProcedure`**: Neutralizando `ptrace` Anti-Debug, `sleep`, Loops Pesados e Funções Criptográficas.
- [[angr-mitigacao-explosao-estados-veritesting-dfs-length-limiter-symbion]] — Veja também: Como Mitigar a **Explosão de Estados (*State Explosion*)** no `angr`: Técnicas de Exploração **`Veritesting`**, **`DFS`**, **`LoopSeer`**, **`LengthLimiter`** e **`LAZY_SOLVES`**.
- [[angr-arquitetura-analise-binaria-execucao-simbolica-cle-pyvex-claripy]] — Referência cruzada direta com angr-arquitetura-analise-binaria-execucao-simbolica-cle-pyvex-claripy.
- [[pwndbg-integracao-decompiladores-decomp2dbg-ghidra-ida-binja]] — Referência cruzada direta com pwndbg-integracao-decompiladores-decomp2dbg-ghidra-ida-binja.

## Fontes
- [angr Official GitHub — Platform-Agnostic Binary Analysis & Symbolic Execution Framework](https://raw.githubusercontent.com/angr/angr/master/README.md) — repositório oficial do `angr` cobrindo carregamento de binários, lifting para IR, execução simbólica, hooks e decompilação; consultado em 2026-10-03.
- [angr Official Documentation — Quickstart, Architecture & Foundational Research (`SoK`, `Driller`, `Firmalice`)](https://docs.angr.io/en/latest/quickstart.html) — documentação oficial do `angr` detalhando os subsistemas `CLE`, `PyVEX`, `Claripy`, `SimState`, `SimulationManager` e análises estáticas/concólicas; consultado em 2026-10-03.
