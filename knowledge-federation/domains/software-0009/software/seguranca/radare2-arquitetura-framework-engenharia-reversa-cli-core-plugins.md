---
id: software.seguranca.tranche07.000641
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
fontes: ["https://raw.githubusercontent.com/radareorg/radare2/master/README.md", "https://raw.githubusercontent.com/radareorg/radare2/master/man/radare2.1", "https://book.rada.re/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Radare2 (`r2`): Arquitetura Unix-First de Engenharia Reversa, Comandos Hierárquicos, Filtro Interno `~` e Iterador `@`

## Em uma frase
**Radare2 (`r2`)** (`radareorg/radare2`, LGPLv3) é o framework livre de análise binária, engenharia reversa, edição hexadecimal, desmontagem e depuração projetado sob a filosofia Unix: composto por bibliotecas C modulares (`r_core`, `r_bin`, `r_anal`, `r_asm`, `r_esil`, `r_io`, `r_debug`) e utilitários de linha de comando (`r2`, `rabin2`, `radiff2`, `rafind2`, `rahash2`, `rasm2`, `rax2`, `rarun2`).

## Por que importa
Funciona instantaneamente via SSH em servidores headless, containers mínimos ou estações de análise forense, analisando dezenas de arquiteturas (x86/x64, ARM/AArch64, MIPS, PowerPC, RISC-V, eBPF/sBPF, WebAssembly, Dalvik, JVM) e sistemas operacionais.

## Como funciona
A gramática de comandos do `r2` é uma árvore mnemônica concisa onde cada letra refina a ação (ex.: `a` = *analyze*, `af` = *analyze functions*, `afl` = *analyze functions list*, `aflj` = sufixo **`j`** que formata a saída de **qualquer** comando como **JSON estruturado**), combinada com o operador de localização temporária **`@ <endereco/flag>`** e o grep/tabela interno **`~<filtro>`**.

## Exemplo
```bash
# Executar o r2 em modo batch (-q -c) analisando o binario (-A) e exportando a lista de funcoes em JSON (aflj)
r2 -q -A -c "aflj" /bin/ls | jq '.[0:3] | map({name: .name, offset: .offset, size: .size, nbbs: .nbbs})'
```

## Limites e trade-offs
Ao analisar amostras suspeitas em scripts automatizados, passe sempre **`-e cfg.sandbox=true`** (ou a flag **`-S`** documentada no manual `radare2(1)`) e **`-N`** (não carrega scripts de inicialização `~/.radare2rc`) para garantir execução determinística e confinada.

## Como verificar
Use `?<comando>?` (ex.: `af?` ou `pd?`) dentro do prompt do `r2` para consultar a ajuda interativa imediata de qualquer subcomando.

## Conexões
- [[radare2-triagem-binarios-rabin2-mitigacoes-nx-canary-pie-relro-strings]] — Veja também: Radare2 (`rabin2`): Triagem Estática de Executáveis, Auditoria de Mitigações de Compilador (**NX**, **Canary**, **PIE**, **RELRO**) e Extração de Símbolos/Strings.
- [[radare2-analise-fluxo-controle-aaa-grafos-cfg-xrefs-decompiler-pdg]] — Referência cruzada direta com radare2-analise-fluxo-controle-aaa-grafos-cfg-xrefs-decompiler-pdg.
- [[ghidra-arquitetura-sre-descompilador-sleigh-pcode-projetos]] — Referência cruzada direta com ghidra-arquitetura-sre-descompilador-sleigh-pcode-projetos.

## Fontes
- [Radare2 Official GitHub — Libre Reversing Framework for Unix Geeks](https://raw.githubusercontent.com/radareorg/radare2/master/README.md) — documentação oficial do Radare2 cobrindo comandos fundamentais, arquitetura de bibliotecas e ecossistema de plugins r2pm (r2ghidra, r2frida, r2yara, r2pipe); consultado em 2026-10-03.
- [Radare2 Official Manual Page — radare2(1) CLI & Reversible Debugger](https://raw.githubusercontent.com/radareorg/radare2/master/man/radare2.1) — manual oficial radare2(1) cobrindo flags de linha de comando, modo sandbox, scripts QuickJS e checkpoints de depuração reversível (dts+/dtsc/dtsr); consultado em 2026-10-03.
- [The Official Radare2 Book](https://book.rada.re/) — livro oficial do projeto Radare2 cobrindo rabin2, radiff2, rasm2, ESIL e r2pipe; consultado em 2026-10-03.
