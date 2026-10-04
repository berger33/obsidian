---
id: software.seguranca.tranche07.000640
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

# Ghidra: **Ghidra Debugger** — Depuração Dinâmica Híbrida (`gdb`, `lldb`, Windows `dbgeng`) e *Time-Travel / Trace Recording*

## Em uma frase
O módulo **Ghidra Debugger** une a análise estática do `CodeBrowser`/Descompilador com a execução dinâmica ao vivo (conectando-se a **GDB** local/remoto `gdbserver`, **LLDB**, **Windows `dbgeng.dll` / WinDbg** ou emulador P-Code/QEMU) através de um banco de dados temporal chamado **Trace**.

## Por que importa
Durante a depuração dinâmica tradicional, se o analista passar direto pela instrução crítica ou quiser saber qual era o valor de um registrador 200 instruções atrás, ele precisa reiniciar o processo; no Ghidra Debugger, o **Trace** grava os estados de memória, registradores, módulos e threads indexados por *snapshots* temporais.

## Como funciona
A sincronização bidirecional entre a janela **Static Listing / Decompiler** e a janela **Dynamic Listing** traduz automaticamente os endereços com **ASLR** do processo em execução para os offsets estáticos do projeto Ghidra, permitindo clicar em uma variável no código C descompilado e ver seu conteúdo ao vivo na memória RAM.

## Exemplo
```bash
# Iniciar gdbserver em uma VM isolada de analise Linux para conexao remota do Ghidra Debugger via SSH/TCP
gdbserver --once 127.0.0.1:2345 /cases/samples/linux_elf_sample
```

## Limites e trade-offs
Jamais conecte o Ghidra Debugger da sua estação de trabalho diretamente a uma amostra de malware rodando fora de um ambiente virtualizado isolado; use sempre uma VM descartável sem acesso à LAN corporativa.

## Como verificar
Verifique na janela *Modules* do Ghidra Debugger o mapeamento automático do binário principal entre o endereço base dinâmico (ASLR) e o programa estático aberto.

## Conexões
- [[ghidra-colaboracao-ghidraserver-version-tracking-patch-diffing]] — Veja também: Ghidra: Engenharia Reversa Colaborativa com **GhidraServer** e Análise de Patches (*Patch Diffing*) com **Version Tracking (`VT`)**.
- [[ghidra-arquitetura-sre-descompilador-sleigh-pcode-projetos]] — Referência cruzada direta com ghidra-arquitetura-sre-descompilador-sleigh-pcode-projetos.
- [[ghidra-emulacao-pcode-emulatorhelper-desofuscacao-strings-malware]] — Referência cruzada direta com ghidra-emulacao-pcode-emulatorhelper-desofuscacao-strings-malware.
- [[frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos]] — Referência cruzada direta com frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos.

## Fontes
- [NSA Ghidra Official GitHub — Software Reverse Engineering Framework](https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/README.md) — documentação oficial do NSA Ghidra cobrindo arquitetura SRE, instalação, build e avisos de segurança; consultado em 2026-10-03.
- [NSA Ghidra Official PyGhidra Documentation — CPython 3 Integration](https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/Ghidra/Features/PyGhidra/README.md) — documentação oficial do módulo PyGhidra para execução de scripts Ghidra nativos em CPython 3 e modo headless; consultado em 2026-10-03.
- [NSA Ghidra Official Security Advisories](https://github.com/NationalSecurityAgency/ghidra/security/advisories) — avisos oficiais de segurança e recomendações de isolamento do projeto Ghidra; consultado em 2026-10-03.
