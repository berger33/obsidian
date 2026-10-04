---
id: software.seguranca.tranche11.001052
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

# O Carregador **`CLE` (*CLE Loads Everything*)** do `angr`: Espaço de Endereçamento, Posição Independente (`PIE`), Bibliotecas Compartilhadas e **Firmware Raw (`Blob`)**

## Em uma frase
Antes de executar qualquer análise sobre um binário, o módulo **`proj.loader` (`CLE`)** do `angr` faz o papel do carregador do sistema operacional (`ld.so` no Linux ou `ntdll.dll` no Windows): ele mapeia segmentos ELF/PE/Mach-O na memória virtual, resolve símbolos de importação/exportação e aplica relocações no GOT/IAT.

## Por que importa
Saber configurar o `CLE` em `angr.Project(..., main_opts={...})` evita dois erros muito comuns em engenharia reversa: **(1) Binários PIE (*Position-Independent Executable*)**: por padrão, o `CLE` mapeia binários ELF PIE de `64-bit` no endereço base **`0x400000`**; se você estiver comparando endereços com o **Ghidra** (que usa `0x100000` por padrão para PIE), passe **`main_opts={'base_addr': 0x100000}`** para que os endereços batam 100% entre o Ghidra e o seu script `angr`!

## Como funciona
E **(2) Imagens de Firmware Bare-Metal / Bootloaders / ROMs IoT (`backend='blob'`)**: quando o arquivo é um dump bruto de memória Flash sem cabeçalho ELF, passe `main_opts={'backend': 'blob', 'arch': 'ARMEL', 'base_addr': 0x08000000, 'entry_point': 0x08000101}`!

## Exemplo
```python
import angr

# Sincronizar o endereco base de um binario ELF PIE com o padrao do Ghidra (0x100000) e inspecionar objetos e simbolos carregados pelo CLE
proj = angr.Project(
    "/usr/bin/id",
    main_opts={"base_addr": 0x100000},
    auto_load_libs=False,
)
main_obj = proj.loader.main_object
print("Objetos:", proj.loader.all_objects)
print("Secoes:", [s.name for s in main_obj.sections])
```

## Limites e trade-offs
Observe a dica de ouro para dumps de firmware **ARM Thumb** no `CLE`: se o código no ponto de entrada do firmware usar o conjunto de instruções **Thumb (16/32 bits)**, lembre-se da convenção da arquitetura ARM de somar **`+1` (endereço ímpar, ex.: `0x08000101`)** no `entry_point` para que o `angr` / `PyVEX` saiba decodificar o bloco em modo Thumb!

## Como verificar
Use `proj.loader.find_symbol('main')` para obter o objeto `Symbol` e consultar `sym.rebased_addr` sem precisar procurar o endereço manualmente.

## Conexões
- [[angr-arquitetura-analise-binaria-execucao-simbolica-cle-pyvex-claripy]] — Veja também: **`angr` (`angr/angr`)**: Arquitetura da Suíte de Análise Binária Multi-Arquitetura (**`CLE`, `archinfo`, `PyVEX`, `Claripy/Z3`, `SimEngine` e `Analyses`**).
- [[angr-motor-solver-claripy-bitvectors-bvs-bvv-restricoes-z3]] — Veja também: Álgebra Simbólica no `angr` com **`claripy`**: Bitvectors Simbólicos (**`BVS`** vs **`BVV`**), Árvores AST e Resolução de Restrições com **Z3 (`state.solver`)**.
- [[ropper-console-interativo-multi-binarios-cache-raw-firmware]] — Referência cruzada direta com ropper-console-interativo-multi-binarios-cache-raw-firmware.

## Fontes
- [angr Official GitHub — Platform-Agnostic Binary Analysis & Symbolic Execution Framework](https://raw.githubusercontent.com/angr/angr/master/README.md) — repositório oficial do `angr` cobrindo carregamento de binários, lifting para IR, execução simbólica, hooks e decompilação; consultado em 2026-10-03.
- [angr Official Documentation — Quickstart, Architecture & Foundational Research (`SoK`, `Driller`, `Firmalice`)](https://docs.angr.io/en/latest/quickstart.html) — documentação oficial do `angr` detalhando os subsistemas `CLE`, `PyVEX`, `Claripy`, `SimState`, `SimulationManager` e análises estáticas/concólicas; consultado em 2026-10-03.
