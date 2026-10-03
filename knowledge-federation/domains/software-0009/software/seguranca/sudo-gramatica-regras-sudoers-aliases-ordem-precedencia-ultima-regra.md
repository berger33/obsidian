---
id: software.seguranca.tranche07.000672
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
fontes: ["https://raw.githubusercontent.com/sudo-project/sudo/main/README.md", "https://www.sudo.ws/docs/man/sudoers.man/", "https://www.sudo.ws/docs/man/sudo_logsrvd.man/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Sudoers: Gramática de Especificação de Comandos, Aliases (`User_Alias`, `Runas_Alias`, `Host_Alias`, `Cmnd_Alias`) e a Regra **"Last Match Wins"**

## Em uma frase
Uma especificação de privilégio no `/etc/sudoers` segue a estrutura **`Quem Onde = (ComoQuem:QualGrupo) Tags: QuaisComandos`** (ex.: `%sre_db ALL = (postgres:postgres) /usr/bin/pg_ctl reload`), permitindo delegar comandos para rodar como contas de serviço específicas (`postgres`, `www-data`, `app`) sem jamais conceder `root`!

## Por que importa
Um detalhe crítico da avaliação do `sudoers` que causa graves falhas de segurança quando incompreendido é a ordem de precedência: **quando múltiplas regras casam com o usuário e comando, a ÚLTIMA regra correspondente no arquivo vence (*Last Match Wins*)**!

## Como funciona
Se um administrador escrever uma negação `!` no topo do arquivo e colocar uma regra mais genérica `ALL` (ou um `#includedir /etc/sudoers.d` no final do `/etc/sudoers`) abaixo dela, a regra posterior sobrescreverá a restrição anterior.

## Exemplo
```sudoers
# /etc/sudoers.d/20-postgres-ops — Delegar apenas como usuario 'postgres' (nunca root) com argumentos fixos
User_Alias   DBA_ONCALL = alice, bob
Host_Alias   PG_SERVERS = dbprod01, dbprod02
Cmnd_Alias   PG_RELOAD  = /usr/lib/postgresql/16/bin/pg_ctl reload -D /var/lib/postgresql/16/main

DBA_ONCALL   PG_SERVERS = (postgres : postgres) PG_RELOAD
```

## Limites e trade-offs
Evite usar o operador de negação **`!`** em listas de comandos (`ALL, !/bin/sh`) achando que isso impede escalação de privilégio: qualquer binário permitido por `ALL` (como `cp`, `chmod`, `find`, `vim`, `python3`) permite copiar `/bin/sh` para `/tmp/meu_shell` e executá-lo contornando a lista negra!

## Como verificar
Sempre inspecione os privilégios efetivos resultantes de uma conta de usuário executando **`sudo -l -U <usuario>`** e verificando a ordem final das regras listadas.

## Conexões
- [[sudo-arquitetura-plugins-sudoers-visudo-menor-privilegio]] — Veja também: Sudo (`sudo`): Arquitetura Modular de Plugins (`sudo.conf`, `sudoers.so`), Validação Sintática com **`visudo -c`** e Menor Privilégio.
- [[sudo-integridade-binarios-sha256-digest-pinning-scripts-administrativos]] — Veja também: Sudoers: Pinagem Criptográfica de Binários e Scripts com **SHA-224 / SHA-256 / SHA-384 / SHA-512 Digest** no `/etc/sudoers`.
- [[sudo-prevencao-gtfobins-noexec-sudoedit-restricao-argumentos-curingas]] — Referência cruzada direta com sudo-prevencao-gtfobins-noexec-sudoedit-restricao-argumentos-curingas.

## Fontes
- [Sudo Official Sudoers Manual — sudoers(5) Policy Plugin Reference](https://raw.githubusercontent.com/sudo-project/sudo/main/README.md) — manual oficial sudoers(5) cobrindo plugins sudo.conf, autenticação, Defaults use_pty/env_reset/secure_path, SHA-256 digests, NOEXEC, sudoedit e I/O logging; consultado em 2026-10-03.
- [Sudo Official GitHub — The Sudo Philosophy & Security Architecture](https://www.sudo.ws/docs/man/sudoers.man/) — repositório oficial do projeto Sudo e diretrizes de menor privilégio; consultado em 2026-10-03.
- [Sudo Official Manual — sudo_logsrvd(8) Centralized I/O & Event Log Server](https://www.sudo.ws/docs/man/sudo_logsrvd.man/) — documentação oficial do servidor centralizado de gravação de sessões sudo_logsrvd com TLS mútuo; consultado em 2026-10-03.
