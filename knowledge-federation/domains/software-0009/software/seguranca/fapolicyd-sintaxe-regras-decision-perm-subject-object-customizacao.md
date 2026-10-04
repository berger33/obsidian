---
id: software.seguranca.tranche15.001433
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/README.md", "https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/init/fapolicyd.conf"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# A Receita de Escrita de Regras no fapolicyd: **`decision perm subject : object`**, Tipos MIME (`ftype`), `trust=1` e `deny_audit`

## Em uma frase
Qual é a gramática exata de uma regra do **`fapolicyd`** e como escrever uma regra customizada em `/etc/fapolicyd/rules.d/` (por exemplo, para permitir que apenas membros do grupo `wheel` executem uma ferramenta administrativa sensível ou permitir que uma conta de serviço execute um binário específico)?

## Por que importa
Conforme o `README.md` oficial, toda regra do `fapolicyd` segue a receita de 4 colunas separadas por dois-pontos (`:`): **`decision permission subject : object`**!

## Como funciona
Veja o significado de cada coluna: **(1) `decision`**: `allow`, `deny`, `allow_audit`, **`deny_audit`** (nega e envia um evento `FANOTIFY` para o subsistema **Linux Audit `auditd`**!), `allow_syslog` ou `deny_syslog`; **(2) `permission`**: `perm=execute`, `perm=open` ou `perm=any`; **(3) `subject` (Quem está fazendo a ação — antes do `:`)**: `all`, `auid=1000`, `uid=nginx`, `gid=wheel`, `exe=/usr/bin/python3`, `comm=bash` ou `trust=1`; e **(4) `object` (Qual arquivo está sendo acessado — depois do `:`)**: `all`, `path=/usr/bin/ping`, `dir=/opt/app/`, `ftype=application/x-executable`, `ftype=application/x-sharedlib` ou `trust=1`!

## Exemplo
```text
# Exemplo de unidade de regra em /etc/fapolicyd/rules.d/65-restricao-admin-tools.rules: permite tcpdump apenas para o grupo wheel e nega com auditoria aos demais
allow perm=any gid=wheel : trust=1 path=/usr/sbin/tcpdump
deny_audit perm=execute all : path=/usr/sbin/tcpdump
```

## Limites e trade-offs
Como descobrir exatamente qual **`ftype` (MIME type)** o `fapolicyd` enxerga para um determinado arquivo (por exemplo, diferenciar `application/x-executable`, `application/x-sharedlib`, `text/x-python` ou `text/x-shellscript`) antes de escrever uma regra? Executando o comando nativo **`fapolicyd-cli --ftype /caminho/do/arquivo`**!

## Como verificar
Cuidado importante documentado no `README.md`: quando você usar nomes de usuário ou de grupo como string nas regras (ex.: `gid=wheel` ou `uid=appuser`), esses usuários e grupos **devem estar resolvidos localmente no `/etc/passwd` e `/etc/group`** no momento da inicialização do `fapolicyd` (ou use o `uid`/`gid` numérico se a conta vier exclusivamente de um diretório de rede tardio).

## Conexões
- [[fapolicyd-politicas-known-libs-restrictive-fagenrules-rules-d]] — Veja também: Políticas Modulares em **`/etc/fapolicyd/rules.d/`**, Compilador **`fagenrules`** e Diferença entre os Perfis **`known-libs`** e **`restrictive`** no fapolicyd.
- [[fapolicyd-gerenciamento-trust-database-fapolicyd-cli-file-add-trust-d]] — Veja também: Gerenciando o **Banco de Confiança (`trust.d/`)** com **`fapolicyd-cli`**: Autorizando Binários Customizados, Agentes de Terceiros e Aplicações em `/opt`.
- [[fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb]] — Referência cruzada direta com fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb.

## Fontes
- [Official `fapolicyd` GitHub Repository (`linux-application-whitelisting/fapolicyd`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/README.md) — repositório oficial do File Access Policy Daemon cobrindo interceptação de execução via `fanotify`, linguagem de regras `allow`/`deny_audit`, `fapolicyd-cli` e banco de confiança; consultado em 2026-10-03.
- [Official `fapolicyd.conf` Configuration Specification (`init/fapolicyd.conf`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/init/fapolicyd.conf) — especificação oficial de configuração do `/etc/fapolicyd/fapolicyd.conf` detalhando `permissive`, `trust = rpmdb,file`, `integrity = none|size|ima|sha256`, `watch_fs` e caches LRU; consultado em 2026-10-03.
