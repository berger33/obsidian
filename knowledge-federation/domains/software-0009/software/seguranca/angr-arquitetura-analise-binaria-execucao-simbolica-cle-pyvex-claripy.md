---
id: software.seguranca.tranche11.001051
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

# **`angr` (`angr/angr`)**: Arquitetura da Suíte de Análise Binária Multi-Arquitetura (**`CLE`, `archinfo`, `PyVEX`, `Claripy/Z3`, `SimEngine` e `Analyses`**)

## Em uma frase
Criado pelos pesquisadores do **Computer Security Lab da UC Santa Barbara (UCSB)**, **SEFCOM da Arizona State University (ASU)** e pela equipe de CTF **Shellphish** (`angr/angr`, licença BSD-2-Clause, escrito em Python 3 / C / Rust), o **`angr`** é o mais completo framework open-source de **Análise Binária Estática, Execução Simbólica Dinâmica (*Concolic Analysis*) e Decompilação Multi-Arquitetura**.

## Por que importa
Como o `angr` consegue analisar binários de `x86`, `x86_64`, `ARM`, `AArch64`, `MIPS`, `PPC`, `RISC-V` e `JVM/Soot` com a mesma API Python? Porque sua arquitetura é dividida em 5 sub-bibliotecas modulares: **(1) `CLE` (*CLE Loads Everything*)** — carrega executáveis ELF, PE, Mach-O, CGC e blobs Raw de firmware em um espaço de endereçamento virtual; **(2) `archinfo`** — define registradores, convenções de chamada e endianness de cada CPU; **(3) `PyVEX` (e P-Code)** — traduz (*lifts*) o código de máquina nativo de qualquer arquitetura para uma **Representação Intermediária (IR VEX)** única; **(4) `Claripy`** — constrói Árvores de Sintaxe Abstrata (ASTs) de variáveis simbólicas (*Bitvectors*) e resolve restrições matemáticas via **Microsoft Z3 SMT Solver**; e **(5) `SimState` & `SimulationManager`** — executam e ramificam os caminhos do programa!

## Como funciona
O ponto de entrada universal no `angr` é **`proj = angr.Project('/caminho/binario', auto_load_libs=False)`**!

## Exemplo
```python
import angr

# Carregar um binario ELF no angr sem carregar bibliotecas compartilhadas externas (auto_load_libs=False) para evitar explosao de estados
proj = angr.Project("/bin/true", auto_load_libs=False)
print(f"Arquitetura: {proj.arch.name}, Entry Point: {hex(proj.entry)}, Main: {hex(proj.loader.main_object.min_addr)}")
```

## Limites e trade-offs
Por que quase sempre passamos **`auto_load_libs=False`** ao criar um `angr.Project` para execução simbólica? Porque se o `CLE` carregar a `libc.so.6` inteira e o `angr` entrar simbolicamente dentro do código real de `printf` ou `malloc` da glibc, o número de ramificações (`if/else`) explode exponencialmente (*State Explosion*)! Com `auto_load_libs=False`, o `angr` substitui automaticamente funções padrão da `libc` por resumos simbólicos rápidos em Python chamados **`SimProcedures`**!

## Como verificar
Explore os atributos `proj.arch`, `proj.loader` e `proj.analyses` em uma sessão interativa do `ipython`.

## Conexões
- [[angr-carregador-binarios-cle-shared-libraries-firmware-blobs-base-addr]] — Veja também: O Carregador **`CLE` (*CLE Loads Everything*)** do `angr`: Espaço de Endereçamento, Posição Independente (`PIE`), Bibliotecas Compartilhadas e **Firmware Raw (`Blob`)**.
- [[angr-execucao-simbolica-simstate-simulation-manager-explore-find-avoid]] — Referência cruzada direta com angr-execucao-simbolica-simstate-simulation-manager-explore-find-avoid.
- [[ropper-busca-semantica-pyvex-z3-solver-restricoes-registradores]] — Referência cruzada direta com ropper-busca-semantica-pyvex-z3-solver-restricoes-registradores.

## Fontes
- [angr Official GitHub — Platform-Agnostic Binary Analysis & Symbolic Execution Framework](https://raw.githubusercontent.com/angr/angr/master/README.md) — repositório oficial do `angr` cobrindo carregamento de binários, lifting para IR, execução simbólica, hooks e decompilação; consultado em 2026-10-03.
- [angr Official Documentation — Quickstart, Architecture & Foundational Research (`SoK`, `Driller`, `Firmalice`)](https://docs.angr.io/en/latest/quickstart.html) — documentação oficial do `angr` detalhando os subsistemas `CLE`, `PyVEX`, `Claripy`, `SimState`, `SimulationManager` e análises estáticas/concólicas; consultado em 2026-10-03.
