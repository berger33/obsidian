---
id: software.seguranca.tranche11.001060
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

# Caça a Corrupção de Memória e **Exploit Generation (`save_unconstrained=True` & `angrop`)**: Encontrando e Explorando **Stack Buffer Overflows** com `angr`

## Em uma frase
Como usar o `angr` para encontrar automaticamente uma vulnerabilidade de **Stack Buffer Overflow** em um binário C/C++ e gerar o payload exato que assume o controle do ponteiro de instrução (`RIP`/`EIP`/`PC`)?

## Por que importa
Quando uma função vulnerável (como `gets`, `strcpy`, `sprintf` ou um `read(0, buf, 512)` sobre um buffer local de 64 bytes) permite sobrescrever o endereço de retorno salvo na pilha, ao executar a instrução `ret`, a CPU carrega os bytes simbólicos da sua entrada diretamente para dentro do registrador **`state.regs.rip` (`state.regs.pc`)**!

## Como funciona
Ao configurar o `SimulationManager` com **`simgr = proj.factory.simulation_manager(state, save_unconstrained=True)`**, assim que o `angr` detecta que o `pc` do estado contém bits simbólicos não-restritos, ele move esse estado para a lista **`simgr.unconstrained`**! A partir daí, basta adicionar a restrição **`unconstrained_state.solver.add(unconstrained_state.regs.pc == endereco_alvo)`** e avaliar `dumps(0)` para que o Z3 calcule o offset exato de padding + todas as transformações nos bytes até apontar o `RIP` para `endereco_alvo`!

## Exemplo
```python
import angr

# Configurar o SimulationManager com save_unconstrained=True para capturar estados onde o ponteiro de instrucao (PC/RIP) se torna simbolico
proj = angr.Project("/bin/true", auto_load_libs=False)
state = proj.factory.entry_state(
    add_options={
        angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY,
        angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS,
    }
)
simgr = proj.factory.simulation_manager(state, save_unconstrained=True)

# Em um binario vulneravel a buffer overflow, simgr.unconstrained recebera o estado no momento do 'ret' corrompido:
print("Monitoramento de estados unconstrained ativo:", simgr.unconstrained)
```

## Limites e trade-offs
Além disso, o ecossistema oficial do `angr` inclui o pacote complementar **`angrop` (`angr/angrop`)**, que adiciona `proj.analyses.ROP()` sobre o motor simbólico do `angr` para encontrar gadgets e sintetizar cadeias ROP completas automaticamente usando resolução de restrições SMT!

## Como verificar
Compare a abordagem simbólica do `angrop` / `Ropper --semantic` com o debug dinâmico no **Pwndbg** para validar cada etapa do payload.

## Conexões
- [[angr-auditoria-firmware-iot-firmalice-authentication-bypass-backdoors]] — Veja também: Auditoria de Firmware IoT com `angr` (**`Firmalice`**): Detecção Automática de **Backdoors e Authentication Bypass** em Binários Embarcados.
- [[angr-arquitetura-analise-binaria-execucao-simbolica-cle-pyvex-claripy]] — Referência cruzada direta com angr-arquitetura-analise-binaria-execucao-simbolica-cle-pyvex-claripy.
- [[angr-execucao-simbolica-simstate-simulation-manager-explore-find-avoid]] — Referência cruzada direta com angr-execucao-simbolica-simstate-simulation-manager-explore-find-avoid.
- [[ropper-geracao-automatica-rop-chains-execve-mprotect-ret2libc]] — Referência cruzada direta com ropper-geracao-automatica-rop-chains-execve-mprotect-ret2libc.

## Fontes
- [angr Official GitHub — Platform-Agnostic Binary Analysis & Symbolic Execution Framework](https://raw.githubusercontent.com/angr/angr/master/README.md) — repositório oficial do `angr` cobrindo carregamento de binários, lifting para IR, execução simbólica, hooks e decompilação; consultado em 2026-10-03.
- [angr Official Documentation — Quickstart, Architecture & Foundational Research (`SoK`, `Driller`, `Firmalice`)](https://docs.angr.io/en/latest/quickstart.html) — documentação oficial do `angr` detalhando os subsistemas `CLE`, `PyVEX`, `Claripy`, `SimState`, `SimulationManager` e análises estáticas/concólicas; consultado em 2026-10-03.
