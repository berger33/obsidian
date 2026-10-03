---
id: software.seguranca.tranche07.000632
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

# Ghidra: Análise de Fluxo de Dados (*Data-Flow / Taint Analysis*) sobre **P-Code** (`Varnode`, `PcodeOp`, *HighFunction* e *SSA Form*)

## Em uma frase
O motor de descompilação do Ghidra eleva o **P-Code** bruto para a forma **SSA (*Static Single Assignment*)** através da árvore `HighFunction`, onde cada variável ou registrador em um ponto específico da função é representado como um **`Varnode`** conectado por operações **`PcodeOp`** (`COPY`, `LOAD`, `STORE`, `CALL`, `CALLIND`, `INT_ADD`, `PTRSUB`, `MULTIEQUAL`).

## Por que importa
Para encontrar vulnerabilidades de corrupção de memória (como um tamanho controlado pelo atacante vindo de `recv()` ou `getenv()` que chega ao terceiro argumento `size` de `memcpy(dst, src, size)` sem validação de limite), rastrear instruções assembly manualmente em 5.000 funções é impraticável; percorrer o grafo SSA de `Varnode.getDef()` no P-Code automatiza essa caça com precisão independente da arquitetura.

## Como funciona
No P-Code em forma SSA, todo `Varnode` tem no máximo uma única operação definidora (`vnode.getDef()`), o que permite caminhar para trás (*backward slicing*) desde o sumidouro perigoso (`memcpy` / `system` / `sprintf`) até a fonte de entrada.

## Exemplo
```python
# Script PyGhidra que inspeciona o P-Code de alto nivel (SSA) das chamadas para identificar a origem dos argumentos
from ghidra.app.decompiler import DecompInterface

ifc = DecompInterface()
ifc.openProgram(currentProgram)
for func in currentProgram.getFunctionManager().getFunctions(True):
    res = ifc.decompileFunction(func, 30, monitor)
    high_func = res.getHighFunction()
    if high_func:
        for op in high_func.getPcodeOps():
            if op.getOpcode() == op.CALL:
                print(func.getName(), op.getSeqnum().getTarget())
```

## Limites e trade-offs
Habilite a visualização do P-Code diretamente na janela de listagem (`Listing`) do Ghidra clicando em *Edit the Listing Fields -> PCode* para depurar como cada instrução assembly é traduzida.

## Como verificar
Execute o script acima no `Script Manager` do Ghidra sobre um binário de teste e verifique a listagem de todas as instruções `CALL` no nível de P-Code.

## Conexões
- [[ghidra-arquitetura-sre-descompilador-sleigh-pcode-projetos]] — Veja também: NSA Ghidra: Arquitetura de Engenharia Reversa de Software (SRE), Linguagem **SLEIGH**, Representação Intermediária **P-Code** e Descompilador.
- [[ghidra-automacao-cli-analyzeheadless-importacao-scripts-lote]] — Veja também: Ghidra: Automação em Linha de Comando e Pipelines CI/DFIR com **`analyzeHeadless`** (`-import`, `-preScript`, `-postScript` e `-readOnly`).
- [[ghidra-scripting-pyghidra-cpython3-flatprogramapi-automacao]] — Referência cruzada direta com ghidra-scripting-pyghidra-cpython3-flatprogramapi-automacao.

## Fontes
- [NSA Ghidra Official GitHub — Software Reverse Engineering Framework](https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/README.md) — documentação oficial do NSA Ghidra cobrindo arquitetura SRE, instalação, build e avisos de segurança; consultado em 2026-10-03.
- [NSA Ghidra Official PyGhidra Documentation — CPython 3 Integration](https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/Ghidra/Features/PyGhidra/README.md) — documentação oficial do módulo PyGhidra para execução de scripts Ghidra nativos em CPython 3 e modo headless; consultado em 2026-10-03.
- [NSA Ghidra Official Security Advisories](https://github.com/NationalSecurityAgency/ghidra/security/advisories) — avisos oficiais de segurança e recomendações de isolamento do projeto Ghidra; consultado em 2026-10-03.
