---
id: software.seguranca.tranche07.000649
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

# Radare2: Depuração Reversível (*Time-Travel Checkpoints* `dts+`/`dtsc`/`dtsr`), Perfis de Execução **`rarun2`** e Integração **`r2frida`**

## Em uma frase
Conforme documentado no manual oficial `radare2(1)`, o depurador do `r2` (`r2 -d <binario>`, comandos da família **`d`**) inclui suporte nativo a **sessões de depuração reversíveis baseadas em Checkpoints (`dts+`, `dtsc`, `dtsr`)**, perfis de ambiente **`rarun2`** (`-r profile.rr2`) e integração com o Frida via **`r2frida`** (`r2 frida://...`).

## Por que importa
O comando **`dts+`** inicia a gravação reversível do estado da sessão de debug; **`dtsc [label]`** cria um checkpoint ramificável do estado atual da memória e registradores; e **`dtsr <id>`** restaura instantaneamente o processo para um checkpoint anterior, permitindo testar diferentes caminhos de execução sem reiniciar o programa do zero.

## Como funciona
Complementarmente, o utilitário **`rarun2`** configura o ambiente do processo depurado (redirecionamento de `stdin`/`stdout` para sockets ou arquivos, `chroot`, mudança de `uid`/`gid`, `aslr=no`, `preload` de bibliotecas e `timeout`), enquanto o plugin **`r2frida`** (`r2pm -Uci r2frida`) conecta o `r2` diretamente a processos ao vivo no Android/iOS/Linux/Windows usando os comandos `:i`, `:is`, `:dt` e `:di`.

## Exemplo
```ini
#!/usr/bin/rarun2
# Perfil rarun2 (debug_profile.rr2) desativando ASLR local e definindo timeout de seguranca para sessao de debug
program=/cases/samples/test_crackme
aslr=no
timeout=60
stdio=/dev/null
```

## Limites e trade-offs
Nunca inicie `r2 -d` (que executa o binário de verdade no kernel) em amostras desconhecidas fora de uma máquina virtual descartável e isolada; para análise sem execução real, use sempre a emulação **ESIL (`aei`/`aes`)** sem a flag `-d`.

## Como verificar
Teste iniciar uma sessão de debug com um binário benigno (`r2 -d /bin/ls`), crie um checkpoint com `dts+` / `dtsc inicio`, avance algumas instruções (`dso 5`) e restaure com `dtsr`.

## Conexões
- [[radare2-automacao-scripting-r2pipe-python-javascript-qjs]] — Veja também: Radare2 (`r2pipe` & QuickJS `-j`): Automação Programática de Engenharia Reversa em Python e JavaScript Nativo.
- [[radare2-integracao-yara-r2yara-r2sarif-projetos-auditoria]] — Veja também: Radare2: Geração de Regras YARA Baseadas em Opcodes (`r2yara` / `pcy`), Exportação **SARIF** (`r2sarif`) e Gestão de Projetos.
- [[radare2-arquitetura-framework-engenharia-reversa-cli-core-plugins]] — Referência cruzada direta com radare2-arquitetura-framework-engenharia-reversa-cli-core-plugins.
- [[radare2-emulacao-esil-desofuscacao-calculo-estado-sem-execucao]] — Referência cruzada direta com radare2-emulacao-esil-desofuscacao-calculo-estado-sem-execucao.
- [[frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos]] — Referência cruzada direta com frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos.

## Fontes
- [Radare2 Official GitHub — Libre Reversing Framework for Unix Geeks](https://raw.githubusercontent.com/radareorg/radare2/master/README.md) — documentação oficial do Radare2 cobrindo comandos fundamentais, arquitetura de bibliotecas e ecossistema de plugins r2pm (r2ghidra, r2frida, r2yara, r2pipe); consultado em 2026-10-03.
- [Radare2 Official Manual Page — radare2(1) CLI & Reversible Debugger](https://raw.githubusercontent.com/radareorg/radare2/master/man/radare2.1) — manual oficial radare2(1) cobrindo flags de linha de comando, modo sandbox, scripts QuickJS e checkpoints de depuração reversível (dts+/dtsc/dtsr); consultado em 2026-10-03.
- [The Official Radare2 Book](https://book.rada.re/) — livro oficial do projeto Radare2 cobrindo rabin2, radiff2, rasm2, ESIL e r2pipe; consultado em 2026-10-03.
