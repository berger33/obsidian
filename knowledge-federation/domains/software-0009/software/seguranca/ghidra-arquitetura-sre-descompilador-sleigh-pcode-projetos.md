---
id: software.seguranca.tranche07.000631
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

# NSA Ghidra: Arquitetura de Engenharia Reversa de Software (SRE), Linguagem **SLEIGH**, Representação Intermediária **P-Code** e Descompilador

## Em uma frase
**Ghidra** (`NationalSecurityAgency/ghidra`, Apache-2.0, desenvolvido pela Diretoria de Pesquisa da NSA) é a suíte open-source de Engenharia Reversa de Software (SRE) para análise estática, descompilação, montagem, visualização em grafos e automação sobre binários compilados (PE, ELF, Mach-O, DEX, Firmware Raw) em dezenas de arquiteturas (x86/x64, ARM/AArch64, MIPS, PowerPC, RISC-V, AVR, SuperH, Tricore).

## Por que importa
Diferente de desassembladores que possuem motores acoplados a apenas uma ou duas arquiteturas de CPU, o Ghidra traduz as instruções de máquina de **qualquer** processador especificado na linguagem declarativa **SLEIGH (`.slaspec`)** para uma única Representação Intermediária de transferência de registradores chamada **P-Code**.

## Como funciona
Como o motor do **Descompilador C++** do Ghidra (que reconstrói código C de alto nível com tipos de dados, loops `while`/`for` e estruturas `struct`) e os analisadores de fluxo de dados operam sobre o **P-Code** (e não sobre a instrução assembly bruta), qualquer nova arquitetura de microcontrolador ou firmware descrita em SLEIGH ganha descompilação para C automaticamente.

## Exemplo
```bash
# Iniciar o Ghidra em modo nativo CPython 3 usando o lancador oficial PyGhidra
/opt/ghidra/support/pyghidraRun
```

## Limites e trade-offs
Conforme alerta o `README.md` oficial do Ghidra, sempre execute o Ghidra dentro de uma máquina virtual de análise isolada ao abrir binários ou arquivos de projeto (`.gar` / `.gpr`) provenientes de fontes não-confiáveis, e mantenha a versão atualizada contra os *Security Advisories* oficiais.

## Como verificar
Verifique a instalação do JDK 21/25 64-bit requerido e confirme a abertura de um binário ELF/PE de teste no `CodeBrowser`.

## Conexões
- [[ghidra-representacao-intermediaria-pcode-analise-fluxo-dados-varnodes]] — Veja também: Ghidra: Análise de Fluxo de Dados (*Data-Flow / Taint Analysis*) sobre **P-Code** (`Varnode`, `PcodeOp`, *HighFunction* e *SSA Form*).
- [[ghidra-automacao-cli-analyzeheadless-importacao-scripts-lote]] — Referência cruzada direta com ghidra-automacao-cli-analyzeheadless-importacao-scripts-lote.
- [[radare2-arquitetura-framework-engenharia-reversa-cli-core-plugins]] — Referência cruzada direta com radare2-arquitetura-framework-engenharia-reversa-cli-core-plugins.

## Fontes
- [NSA Ghidra Official GitHub — Software Reverse Engineering Framework](https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/README.md) — documentação oficial do NSA Ghidra cobrindo arquitetura SRE, instalação, build e avisos de segurança; consultado em 2026-10-03.
- [NSA Ghidra Official PyGhidra Documentation — CPython 3 Integration](https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/Ghidra/Features/PyGhidra/README.md) — documentação oficial do módulo PyGhidra para execução de scripts Ghidra nativos em CPython 3 e modo headless; consultado em 2026-10-03.
- [NSA Ghidra Official Security Advisories](https://github.com/NationalSecurityAgency/ghidra/security/advisories) — avisos oficiais de segurança e recomendações de isolamento do projeto Ghidra; consultado em 2026-10-03.
