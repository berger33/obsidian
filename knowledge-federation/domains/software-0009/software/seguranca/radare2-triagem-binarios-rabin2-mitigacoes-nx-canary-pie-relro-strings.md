---
id: software.seguranca.tranche07.000642
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

# Radare2 (`rabin2`): Triagem Estática de Executáveis, Auditoria de Mitigações de Compilador (**NX**, **Canary**, **PIE**, **RELRO**) e Extração de Símbolos/Strings

## Em uma frase
O utilitário **`rabin2`** (equivalente aos comandos da família **`i`** dentro do `r2`: `iI`, `iS`, `ii`, `iE`, `iz`, `izz`) extrai metadados estruturais de executáveis ELF, PE, Mach-O, COFF e DEX sem precisar abrir uma sessão interativa.

## Por que importa
Em auditorias de segurança de binários (como verificar se todos os daemons C/C++ de um appliance corporativo foram compilados com proteções modernas de memória) ou na triagem inicial de um malware, o `rabin2 -I` revela em milissegundos a arquitetura, subclasse e todas as flags de hardening.

## Como funciona
As flags principais do `rabin2` incluem: **`-I`** (informações do binário e mitigações: `canary`, `nx`, `pic`/`pie`, `relro`, `crypto`, `stripped`), **`-S`** (seções e permissões `rwx`, detectando seções anômalas graváveis e executáveis), **`-i`** (funções importadas da PLT/IAT), **`-E`** (símbolos exportados), **`-l`** (bibliotecas dinâmicas vinculadas), **`-z`** (strings na seção de dados) e **`-zz`** (strings no binário inteiro, inclusive seções de código/recursos).

## Exemplo
```bash
# Auditar em JSON (-j) as mitigacoes de seguranca de compilacao (canary, nx, pic, relro) e secoes de um binario ELF
rabin2 -Ij /usr/sbin/sshd | jq '.info | {arch, bits, os, canary, nx, pic, relro, stripped}'
rabin2 -Sj /usr/sbin/sshd | jq '.sections[] | select(.perm | contains("x")) | {name, size, perm, vaddr}'
```

## Limites e trade-offs
Em pipelines de CI/CD de projetos C/C++/Rust embarcados, adicione um passo com `rabin2 -Ij <binario> | jq -e '.info.nx == true and .info.pic == true and .info.canary == true and .info.relro == "full"'` para bloquear releases compilados sem `-fstack-protector-strong -fPIE -pie -Wl,-z,relro,-z,now`.

## Como verificar
Verifique nas seções retornadas por `rabin2 -S` se alguma seção possui permissão simultânea de escrita e execução (`w` e `x`) ou entropia próxima de `8.0` (indicativo de *packing*).

## Conexões
- [[radare2-arquitetura-framework-engenharia-reversa-cli-core-plugins]] — Veja também: Radare2 (`r2`): Arquitetura Unix-First de Engenharia Reversa, Comandos Hierárquicos, Filtro Interno `~` e Iterador `@`.
- [[radare2-analise-fluxo-controle-aaa-grafos-cfg-xrefs-decompiler-pdg]] — Veja também: Radare2 (`r2`): Análise de Código (`aaa`), Grafos de Fluxo de Controle (`agf` / `agfj`), Referências Cruzadas (`axt` / `axf`) e Descompilação (`pdg`).
- [[radare2-busca-padroes-rafind2-rahash2-entropia-secoes-empacotamento]] — Referência cruzada direta com radare2-busca-padroes-rafind2-rahash2-entropia-secoes-empacotamento.

## Fontes
- [Radare2 Official GitHub — Libre Reversing Framework for Unix Geeks](https://raw.githubusercontent.com/radareorg/radare2/master/README.md) — documentação oficial do Radare2 cobrindo comandos fundamentais, arquitetura de bibliotecas e ecossistema de plugins r2pm (r2ghidra, r2frida, r2yara, r2pipe); consultado em 2026-10-03.
- [Radare2 Official Manual Page — radare2(1) CLI & Reversible Debugger](https://raw.githubusercontent.com/radareorg/radare2/master/man/radare2.1) — manual oficial radare2(1) cobrindo flags de linha de comando, modo sandbox, scripts QuickJS e checkpoints de depuração reversível (dts+/dtsc/dtsr); consultado em 2026-10-03.
- [The Official Radare2 Book](https://book.rada.re/) — livro oficial do projeto Radare2 cobrindo rabin2, radiff2, rasm2, ESIL e r2pipe; consultado em 2026-10-03.
