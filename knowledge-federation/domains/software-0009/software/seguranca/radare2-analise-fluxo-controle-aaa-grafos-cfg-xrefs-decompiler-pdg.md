---
id: software.seguranca.tranche07.000643
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

# Radare2 (`r2`): Análise de Código (`aaa`), Grafos de Fluxo de Controle (`agf` / `agfj`), Referências Cruzadas (`axt` / `axf`) e Descompilação (`pdg`)

## Em uma frase
Dentro de uma sessão do `r2`, os comandos de análise **`aa`** (análise básica de símbolos e chamadas) e **`aaa`** (equivalente à flag `-A` na CLI: análise completa de funções, blocos básicos, *autonaming*, argumentos de pilha e tabelas de salto) constroem o modelo de fluxo de controle do programa.

## Por que importa
Após rodar `aaa`, o analista navega até qualquer função (`s main` ou `s sym.imp.system`), visualiza o disassembly colorido (`pdf`), renderiza o **Control-Flow Graph (CFG)** interativo diretamente no terminal (`agf` ou modo visual `VV`) e inspeciona todas as referências cruzadas que chegam (`axt`) ou saem (`axf`) de um endereço ou string.

## Como funciona
Integrado ao gerenciador de pacotes **`r2pm`**, o plugin oficial **`r2ghidra`** (`r2pm -Uci r2ghidra`) traz o motor nativo em C++ do descompilador do NSA Ghidra diretamente para dentro do `r2`, acessível pelo comando **`pdg`** (e `pdgj` para AST JSON), unindo a agilidade da CLI do `r2` com a descompilação de alto nível do Ghidra.

## Exemplo
```bash
# Localizar referencias cruzadas (axt) para funcoes ou strings e exportar o Control-Flow Graph (agfj) da funcao main
r2 -q -A -c "s main; agfj" /bin/ls | jq '.[0].blocks | length'
```

## Limites e trade-offs
Evite rodar `aaaa` (análise experimental exaustiva) cegamente em binários gigantes (> 50 MB) com milhares de funções estáticas; prefira `aa` seguido de análise direcionada nas regiões de interesse (`af @ <addr>`) para resposta instantânea.

## Como verificar
Instale ou verifique plugins instalados com `r2pm -l` e utilize `axt @ str.<nome>` para listar todas as funções que referenciam uma string específica.

## Conexões
- [[radare2-triagem-binarios-rabin2-mitigacoes-nx-canary-pie-relro-strings]] — Veja também: Radare2 (`rabin2`): Triagem Estática de Executáveis, Auditoria de Mitigações de Compilador (**NX**, **Canary**, **PIE**, **RELRO**) e Extração de Símbolos/Strings.
- [[radare2-emulacao-esil-desofuscacao-calculo-estado-sem-execucao]] — Veja também: Radare2: Emulação Segura com **ESIL (*Evaluable Strings Intermediate Language*)** (`aei`, `aeim`, `aes`, `aeso` e `emu.str=true`).
- [[radare2-arquitetura-framework-engenharia-reversa-cli-core-plugins]] — Referência cruzada direta com radare2-arquitetura-framework-engenharia-reversa-cli-core-plugins.
- [[ghidra-arquitetura-sre-descompilador-sleigh-pcode-projetos]] — Referência cruzada direta com ghidra-arquitetura-sre-descompilador-sleigh-pcode-projetos.

## Fontes
- [Radare2 Official GitHub — Libre Reversing Framework for Unix Geeks](https://raw.githubusercontent.com/radareorg/radare2/master/README.md) — documentação oficial do Radare2 cobrindo comandos fundamentais, arquitetura de bibliotecas e ecossistema de plugins r2pm (r2ghidra, r2frida, r2yara, r2pipe); consultado em 2026-10-03.
- [Radare2 Official Manual Page — radare2(1) CLI & Reversible Debugger](https://raw.githubusercontent.com/radareorg/radare2/master/man/radare2.1) — manual oficial radare2(1) cobrindo flags de linha de comando, modo sandbox, scripts QuickJS e checkpoints de depuração reversível (dts+/dtsc/dtsr); consultado em 2026-10-03.
- [The Official Radare2 Book](https://book.rada.re/) — livro oficial do projeto Radare2 cobrindo rabin2, radiff2, rasm2, ESIL e r2pipe; consultado em 2026-10-03.
