---
id: software.seguranca.tranche15.001431
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

# Arquitetura do **fapolicyd (`linux-application-whitelisting/fapolicyd` — *File Access Policy Daemon*)**: **Application Whitelisting** no Linux via Kernel **`fanotify`** e Banco **`LMDB`**

## Em uma frase
Imagine que um atacante explore uma vulnerabilidade de Upload de Arquivo ou Injeção de Comando em uma aplicação web no seu servidor Linux, baixe um implante/ransomware em `/tmp/payload.elf` (ou um script Python/Bash malicioso em `/var/tmp/reverse.py`) e tente executá-lo. Mesmo que o arquivo tenha permissão `chmod +x` e o contexto SELinux de `/tmp` permita execução por padrão, **como bloquear no Kernel Linux a execução de todo e qualquer binário, biblioteca `.so` ou script que não pertença aos pacotes oficiais instalados no sistema**?

## Por que importa
Com o **`fapolicyd` (*File Access Policy Daemon*)**, o daemon oficial de **Application Whitelisting (Allowlisting)** do ecossistema Linux (padrão em perfis DISA STIG, OSPP e ANSSI no RHEL, Fedora, AlmaLinux, Rocky Linux, Debian e Ubuntu)!

## Como funciona
Como ele funciona em tempo real? O `fapolicyd` registra marcas de interceptação síncrona na API **`fanotify` do Kernel Linux (`FAN_OPEN_EXEC_PERM` e `FAN_OPEN_PERM`, Kernel >= 4.20)**: toda vez que qualquer processo tenta executar um binário ou abrir uma biblioteca compartilhada/script nos sistemas de arquivos monitorados (`watch_fs`), **o Kernel congela a chamada `execve`/`open` por alguns microssegundos e pergunta ao `fapolicyd` se o arquivo é confiável (`ALLOW` ou `DENY`)**, consultando um banco de dados ultrarrápido **`LMDB`** alimentado automaticamente pelo gerenciador de pacotes (**`rpmdb`** / **`debdb`**) e pelos arquivos em **`/etc/fapolicyd/trust.d/`**!

## Exemplo
```bash
# Listar a politica compilada ativa do fapolicyd e inspecionar as estatisticas em tempo real do cache de decisoes e do banco de confianca LMDB
fapolicyd-cli --list
cat /var/run/fapolicyd/fapolicyd.state || true
```

## Limites e trade-offs
Veja como o banco de confiança **`trust = rpmdb,file`** (no `/etc/fapolicyd/fapolicyd.conf`) elimina 99% do trabalho manual de manutenção de uma *Whitelist*: sempre que o administrador instala ou atualiza um pacote oficial via **`dnf` / `rpm`** (integrado via plugin `fapolicyd-dnf-plugin`!), os novos caminhos, tamanhos em bytes e hashes **`SHA-256`** dos binários e bibliotecas do pacote são sincronizados automaticamente no banco LMDB do `fapolicyd`!

## Como verificar
Para não sofrer latência repetindo consultas ao LMDB a cada comando executado, o `fapolicyd` mantém em RAM um cache LRU de sujeitos (`subj_cache_size = 4099`) e de objetos (`obj_cache_size = 8191`), respondendo à maioria das decisões em frações de microssegundo!

## Conexões
- [[fapolicyd-politicas-known-libs-restrictive-fagenrules-rules-d]] — Veja também: Políticas Modulares em **`/etc/fapolicyd/rules.d/`**, Compilador **`fagenrules`** e Diferença entre os Perfis **`known-libs`** e **`restrictive`** no fapolicyd.
- [[fapolicyd-verificacao-integridade-sha256-size-ima-anti-tampering]] — Referência cruzada direta com fapolicyd-verificacao-integridade-sha256-size-ima-anti-tampering.
- [[keylime-monitoramento-integridade-runtime-linux-ima-allowlists-polices]] — Referência cruzada direta com keylime-monitoramento-integridade-runtime-linux-ima-allowlists-polices.

## Fontes
- [Official `fapolicyd` GitHub Repository (`linux-application-whitelisting/fapolicyd`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/README.md) — repositório oficial do File Access Policy Daemon cobrindo interceptação de execução via `fanotify`, linguagem de regras `allow`/`deny_audit`, `fapolicyd-cli` e banco de confiança; consultado em 2026-10-03.
- [Official `fapolicyd.conf` Configuration Specification (`init/fapolicyd.conf`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/init/fapolicyd.conf) — especificação oficial de configuração do `/etc/fapolicyd/fapolicyd.conf` detalhando `permissive`, `trust = rpmdb,file`, `integrity = none|size|ima|sha256`, `watch_fs` e caches LRU; consultado em 2026-10-03.
