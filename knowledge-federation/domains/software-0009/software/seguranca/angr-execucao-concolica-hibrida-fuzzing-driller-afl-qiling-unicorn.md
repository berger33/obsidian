---
id: software.seguranca.tranche11.001058
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

# Execução Concólica Híbrida e Fuzzing Assistido por Solver (**`Driller`**) & Engine Nativa **Unicorn (`angr.options.UNICORN`)**

## Em uma frase
O segundo artigo acadêmico citado na documentação oficial do `angr` (`quickstart.html`) é o famoso paper **`Driller: Augmenting Fuzzing Through Selective Symbolic Execution` (NDSS 2016)** da UCSB/Shellphish.

## Por que importa
Por que combinar **Fuzzing Baseado em Cobertura (AFL++)** com **Execução Simbólica Seletiva (`angr`)**? Porque um *fuzzer* é extremamente rápido (milhares de execuções por segundo) para explorar desvios simples (`if (x > 10)`), mas **fica completamente travado quando encontra uma checagem de "Número Mágico" ou Checksum de 32/64 bits (`if (input_int == 0x7f454c46)`)** — pois a chance de adivinhar 4 bytes exatos no sorteio aleatório é de $1$ em $4$ bilhões!

## Como funciona
Na arquitetura **Driller / Execução Concólica**, quando o fuzzer trava sem conseguir descobrir novos caminhos, ele entrega uma das entradas concretas atuais para o `angr`; o `angr` traça exatamente aquele caminho concreto (`Preconstrainer`), inverte matematicamente no **Z3** a condição do `if (input_int == 0x7f454c46)` que bloqueava o fuzzer, gera uma nova semente válida e a devolve para o fuzzer continuar!

## Exemplo
```python
import angr

# Acelerar a execucao de trechos concretos no angr habilitando o conjunto de opcoes nativas da engine Unicorn (angr.options.unicorn)
proj = angr.Project("/bin/true", auto_load_libs=False)
state = proj.factory.entry_state(add_options=angr.options.unicorn)
simgr = proj.factory.simulation_manager(state)
simgr.run()
print("Estados finalizados com aceleracao Unicorn:", len(simgr.deadended))
```

## Limites e trade-offs
Repare em **`add_options=angr.options.unicorn`** no código acima: sempre que um `SimState` executa instruções que operam apenas sobre dados concretos (como loops de inicialização ou descompactação), o `angr` transfere a execução daquele trecho para o emulador C/JIT **Unicorn Engine** em velocidade nativa e só volta para o interpretador simbólico VEX na primeira instrução que tocar em um byte simbólico!

## Como verificar
Essa combinação `Unicorn (para dados concretos) + PyVEX/Claripy (apenas para dados simbólicos)` acelera análises reais em mais de 10x a 50x.

## Conexões
- [[angr-mitigacao-explosao-estados-veritesting-dfs-length-limiter-symbion]] — Veja também: Como Mitigar a **Explosão de Estados (*State Explosion*)** no `angr`: Técnicas de Exploração **`Veritesting`**, **`DFS`**, **`LoopSeer`**, **`LengthLimiter`** e **`LAZY_SOLVES`**.
- [[angr-auditoria-firmware-iot-firmalice-authentication-bypass-backdoors]] — Veja também: Auditoria de Firmware IoT com `angr` (**`Firmalice`**): Detecção Automática de **Backdoors e Authentication Bypass** em Binários Embarcados.
- [[angr-arquitetura-analise-binaria-execucao-simbolica-cle-pyvex-claripy]] — Referência cruzada direta com angr-arquitetura-analise-binaria-execucao-simbolica-cle-pyvex-claripy.
- [[pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto]] — Referência cruzada direta com pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto.

## Fontes
- [angr Official GitHub — Platform-Agnostic Binary Analysis & Symbolic Execution Framework](https://raw.githubusercontent.com/angr/angr/master/README.md) — repositório oficial do `angr` cobrindo carregamento de binários, lifting para IR, execução simbólica, hooks e decompilação; consultado em 2026-10-03.
- [angr Official Documentation — Quickstart, Architecture & Foundational Research (`SoK`, `Driller`, `Firmalice`)](https://docs.angr.io/en/latest/quickstart.html) — documentação oficial do `angr` detalhando os subsistemas `CLE`, `PyVEX`, `Claripy`, `SimState`, `SimulationManager` e análises estáticas/concólicas; consultado em 2026-10-03.
