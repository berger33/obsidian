---
id: software.seguranca.tranche07.000634
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/README.md", "https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/Ghidra/Features/PyGhidra/README.md", "https://github.com/NationalSecurityAgency/ghidra/security/advisories"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Ghidra: Desenvolvimento de Scripts em **Python 3 Nativo (`PyGhidra`)** e Uso da **`FlatProgramAPI`**

## Em uma frase
O módulo oficial **`PyGhidra`** (`Ghidra/Features/PyGhidra`, iniciado com `./support/pyghidraRun` ou usado como biblioteca Python standalone `import pyghidra`) substitui o antigo interpretador Jython 2.7 por um **interpretador CPython 3 nativo** integrado à JVM via JPype.

## Por que importa
Permite usar dentro dos scripts de engenharia reversa do Ghidra todo o ecossistema moderno de Python 3 (`cryptography`, `pycryptodome`, `unicorn`, `capstone`, `z3-solver`, `yara-python`, `networkx`, `pandas`) para decifrar strings de malware ou resolver restrições simbólicas.

## Como funciona
A API do Ghidra disponibiliza no escopo global dos scripts tanto o objeto `currentProgram` (`ProgramDB` completo) quanto os métodos simplificados da **`FlatProgramAPI`** (`getFunctionAt`, `getReferencesTo`, `getBytes`, `setBytes`, `createBookmark`, `setPlateComment`, `decompileFunction`).

## Exemplo
```python
# Script PyGhidra (CPython 3) que localiza todas as referencias cruzadas (XREFs) para APIs criticas de injecao
target_apis = ["VirtualAllocEx", "WriteProcessMemory", "CreateRemoteThread", "NtMapViewOfSection"]
sym_table = currentProgram.getSymbolTable()

for api_name in target_apis:
    for sym in sym_table.getSymbols(api_name):
        for ref in getReferencesTo(sym.getAddress()):
            caller = getFunctionContaining(ref.getFromAddress())
            caller_name = caller.getName() if caller else "unknown"
            print(f"[XREF] {api_name} chamado em {ref.getFromAddress()} dentro de {caller_name}")
```

## Limites e trade-offs
Ao usar o `pyghidra` diretamente como biblioteca a partir de um script Python externo (`pyghidra.start()` e `with pyghidra.open_program(binary_path) as flat_api:`), você pode integrar a descompilação do Ghidra diretamente dentro de pipelines automatizados de triagem.

## Como verificar
Execute o script via `pyghidraRun` e confirme a listagem exata dos endereços e funções chamadoras.

## Conexões
- [[ghidra-automacao-cli-analyzeheadless-importacao-scripts-lote]] — Veja também: Ghidra: Automação em Linha de Comando e Pipelines CI/DFIR com **`analyzeHeadless`** (`-import`, `-preScript`, `-postScript` e `-readOnly`).
- [[ghidra-reconstrucao-tipos-structs-classes-cpp-rtti-vtables-pdb-dwarf]] — Veja também: Ghidra: Reconstrução de Estruturas C (`Data Type Manager`), Classes C++ (`RTTI` / `vtable`), *Parse C Source* e Símbolos **PDB / DWARF**.
- [[ghidra-arquitetura-sre-descompilador-sleigh-pcode-projetos]] — Referência cruzada direta com ghidra-arquitetura-sre-descompilador-sleigh-pcode-projetos.
- [[radare2-automacao-scripting-r2pipe-python-javascript-qjs]] — Referência cruzada direta com radare2-automacao-scripting-r2pipe-python-javascript-qjs.

## Fontes
- [NSA Ghidra Official GitHub — Software Reverse Engineering Framework](https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/README.md) — documentação oficial do NSA Ghidra cobrindo arquitetura SRE, instalação, build e avisos de segurança; consultado em 2026-10-03.
- [NSA Ghidra Official PyGhidra Documentation — CPython 3 Integration](https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/Ghidra/Features/PyGhidra/README.md) — documentação oficial do módulo PyGhidra para execução de scripts Ghidra nativos em CPython 3 e modo headless; consultado em 2026-10-03.
- [NSA Ghidra Official Security Advisories](https://github.com/NationalSecurityAgency/ghidra/security/advisories) — avisos oficiais de segurança e recomendações de isolamento do projeto Ghidra; consultado em 2026-10-03.
