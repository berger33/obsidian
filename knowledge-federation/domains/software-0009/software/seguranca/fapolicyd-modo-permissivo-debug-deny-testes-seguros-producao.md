---
id: software.seguranca.tranche15.001436
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

# Testando Políticas sem Risco de Lockout no fapolicyd: Modo **`--permissive`**, Diagnóstico **`--debug-deny`** e Interpretação dos Eventos de Negação

## Em uma frase
Como avisa o próprio autor do `fapolicyd` no `README.md`: *"When testing new policy, it is highly recommended to use the permissive mode to make sure nothing bad happens. It really is not too hard to deadlock your system."* Se você escrever uma regra errada que bloqueie o carregamento da `libc.so.6` ou do `/usr/bin/bash` em modo ativo (`permissive = 0`), nenhum processo novo subirá na máquina!

## Por que importa
Qual é o procedimento seguro de 3 passos documentado no `README.md` para testar e homologar regras do **`fapolicyd`** sem jamais travar o servidor?

## Como funciona
Passo 1: Pare o serviço systemd (`systemctl stop fapolicyd`) e inicie o daemon manualmente em um terminal `root` com **`/usr/sbin/fapolicyd --permissive --debug-deny`**! A flag **`--permissive`** faz com que o `fapolicyd` avalie 100% das regras mas responda sempre `ALLOW` ao kernel (impedindo qualquer travamento!), enquanto **`--debug-deny`** filtra a saída na tela para imprimir **exclusivamente os eventos que teriam sido bloqueados (`dec=deny` / `dec=deny_audit`)**! Passo 2: Em outro terminal, execute a carga de trabalho completa da sua aplicação, scripts de cron, deploys e agentes de monitoramento. Passo 3: Analise cada linha impressa no `--debug-deny`: se todas as ferramentas legítimas rodaram sem gerar nenhum `dec=deny_audit` e os seus testes de execução em `/tmp` e `/home` geraram `dec=deny_audit`, você está pronto para rodar em modo enforcing (`permissive = 0`)!

## Exemplo
```bash
# Executar o fapolicyd em primeiro plano em modo Permissivo filtrando apenas decisoes de bloqueio (--debug-deny) para homologar regras com risco zero
systemctl stop fapolicyd
/usr/sbin/fapolicyd --permissive --debug-deny
```

## Limites e trade-offs
Vamos decodificar cada campo de uma linha gerada pelo `--debug-deny`, como **`rule:9 dec=deny_audit perm=execute auid=1001 pid=14137 exe=/usr/bin/bash : file=/home/joe/my-ls ftype=application/x-executable trust=0`**: **`rule:9`** é o número da regra em `fapolicyd-cli --list` que tomou a decisão; **`auid=1001`** é o ID do usuário real que fez login via SSH (mesmo que ele tenha usado `sudo su -`!); **`exe=/usr/bin/bash`** é o processo pai; e **`file=/home/joe/my-ls ... trust=0`** é o binário não confiável bloqueado!

## Como verificar
Para testar em isolamento apenas um ponto de montagem específico sem monitorar o resto do sistema operacional, use a flag **`fapolicyd --debug --mounts=/tmp/meu-mounts-teste`** conforme documentado na seção *Override Mounts While Debugging*!

## Conexões
- [[fapolicyd-verificacao-integridade-sha256-size-ima-anti-tampering]] — Veja também: Modos de Verificação de Integridade (**`integrity = none | size | ima | sha256`**) no `/etc/fapolicyd/fapolicyd.conf`: Impedindo Substituição de Binários Confiáveis!.
- [[fapolicyd-bloqueio-interpretadores-python-shell-ld-so-evasao]] — Veja também: Blindando Interpretadores (**Python, Perl, Ruby, PHP, Lua, Node.js e Bash**) e Bloqueando Evasões `ld.so` / `/dev/shm` no fapolicyd.
- [[fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb]] — Referência cruzada direta com fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb.
- [[fapolicyd-politicas-known-libs-restrictive-fagenrules-rules-d]] — Referência cruzada direta com fapolicyd-politicas-known-libs-restrictive-fagenrules-rules-d.

## Fontes
- [Official `fapolicyd` GitHub Repository (`linux-application-whitelisting/fapolicyd`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/README.md) — repositório oficial do File Access Policy Daemon cobrindo interceptação de execução via `fanotify`, linguagem de regras `allow`/`deny_audit`, `fapolicyd-cli` e banco de confiança; consultado em 2026-10-03.
- [Official `fapolicyd.conf` Configuration Specification (`init/fapolicyd.conf`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/init/fapolicyd.conf) — especificação oficial de configuração do `/etc/fapolicyd/fapolicyd.conf` detalhando `permissive`, `trust = rpmdb,file`, `integrity = none|size|ima|sha256`, `watch_fs` e caches LRU; consultado em 2026-10-03.
