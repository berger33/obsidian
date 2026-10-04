---
id: software.seguranca.tranche11.001055
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

# Engenharia Reversa com **`@proj.hook`** e **`angr.SimProcedure`**: Neutralizando `ptrace` Anti-Debug, `sleep`, Loops Pesados e Funções Criptográficas

## Em uma frase
Em binários do mundo real e malwares, se você rodar a execução simbólica cegamente desde o `main`, três obstáculos vão travar a análise: **(1) Armadilhas Anti-Debug** (como `ptrace(PTRACE_TRACEME, ...)` ou checagens de tempo `rdtsc`/`sleep(3600)`);

## Por que importa
**(2) Funções de Hash/Criptografia unidirecionais** (como `SHA256`, `MD5` ou `AES`, que um SMT solver como o Z3 não consegue inverter matematicamente); e **(3) Funções complexas de bibliotecas estáticas ou C++**!

## Como funciona
Para contornar esses obstáculos cirurgicamente, o `angr` oferece dois mecanismos de interceptação: **`@proj.hook(endereco, length=N)`** (substitui `N` bytes de instruções em um endereço específico por uma função Python `def meu_hook(state):`, podendo inclusive pular uma chamada `call` inteira!) e **`proj.hook_symbol('nome_funcao', MeuSimProcedure())`** (substitui qualquer função pelo seu nome ou endereço usando a classe **`angr.SimProcedure`**, que lida automaticamente com a convenção de chamada, argumentos e valor de retorno da arquitetura!)!

## Exemplo
```python
import angr
import claripy

proj = angr.Project("/bin/true", auto_load_libs=False)


# Criar um SimProcedure que substitui ptrace() ou uma funcao de verificacao customizada retornando sempre 0 (sucesso)
class BypassPtrace(angr.SimProcedure):
    def run(self, request, pid, addr, data):
        return claripy.BVV(0, self.arch.bits)


proj.hook_symbol("ptrace", BypassPtrace())
```

## Limites e trade-offs
Quando você está analisando um binário *stripped* (sem tabela de símbolos, comum em firmwares IoT e malwares compilados estaticamente), o `angr` pode aplicar assinaturas **FLIRT** ou você pode ligar seus `SimProcedures` diretamente ao endereço da função descoberta no Ghidra via **`proj.hook(0x4012a0, angr.SIM_PROCEDURES['libc']['strcmp']())`**!

## Como verificar
Use `@proj.hook(addr, length=5)` com corpo vazio (`pass`) quando quiser apenas transformar uma instrução `call check_debugger` (5 bytes no x86_64) em um `NOP` instantâneo sem modificar o arquivo binário em disco!

## Conexões
- [[angr-execucao-simbolica-simstate-simulation-manager-explore-find-avoid]] — Veja também: Execução Simbólica com **`SimState`** e **`SimulationManager` (`simgr.explore`)**: Navegando até Estados Alvo (`find`) e Podando Caminhos Inválidos (`avoid`).
- [[angr-analise-estatica-cfgfast-cfgemulated-decompilador-reaching-definitions]] — Veja também: Análise Estática e Decompilação no `angr`: **`CFGFast` vs `CFGEmulated`**, Grafo de Dependências (**`DDG` / `ReachingDefinitions`**) e **`Decompiler`**.
- [[angr-arquitetura-analise-binaria-execucao-simbolica-cle-pyvex-claripy]] — Referência cruzada direta com angr-arquitetura-analise-binaria-execucao-simbolica-cle-pyvex-claripy.
- [[frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos]] — Referência cruzada direta com frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos.

## Fontes
- [angr Official GitHub — Platform-Agnostic Binary Analysis & Symbolic Execution Framework](https://raw.githubusercontent.com/angr/angr/master/README.md) — repositório oficial do `angr` cobrindo carregamento de binários, lifting para IR, execução simbólica, hooks e decompilação; consultado em 2026-10-03.
- [angr Official Documentation — Quickstart, Architecture & Foundational Research (`SoK`, `Driller`, `Firmalice`)](https://docs.angr.io/en/latest/quickstart.html) — documentação oficial do `angr` detalhando os subsistemas `CLE`, `PyVEX`, `Claripy`, `SimState`, `SimulationManager` e análises estáticas/concólicas; consultado em 2026-10-03.
