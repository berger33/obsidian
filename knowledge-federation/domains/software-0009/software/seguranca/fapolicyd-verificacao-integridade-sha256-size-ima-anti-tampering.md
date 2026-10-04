---
id: software.seguranca.tranche15.001435
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

# Modos de Verificação de Integridade (**`integrity = none | size | ima | sha256`**) no `/etc/fapolicyd/fapolicyd.conf`: Impedindo Substituição de Binários Confiáveis!

## Em uma frase
Preste muita atenção a este detalhe crítico do arquivo **`/etc/fapolicyd/fapolicyd.conf`**: por padrão de instalação, a opção **`integrity`** vem configurada como **`integrity = none`**! O que acontece se `integrity = none` for mantido e um atacante com privilégio de escrita substituir o conteúdo de um script ou binário confiável (como `/usr/bin/meu-script-backup.sh`) por comandos maliciosos?

## Por que importa
Com `integrity = none`, o `fapolicyd` verifica apenas se o **caminho (`/usr/bin/meu-script-backup.sh`)** consta no banco LMDB — ele não confere se o conteúdo do arquivo foi alterado depois da instalação!

## Como funciona
Para impedir que um invasor trojanize binários ou scripts já existentes na whitelist, você deve mudar no `/etc/fapolicyd/fapolicyd.conf` para **`integrity = sha256`** (ou `integrity = ima` se o sistema usar Linux IMA)! Com **`integrity = sha256`**, no instante em que um arquivo é aberto para execução pela primeira vez, o `fapolicyd` calcula o hash **`SHA-256` real do arquivo no disco** e o compara com o `SHA-256` gravado no banco LMDB (`rpmdb` + `trust.d`): **se um único bit do arquivo tiver sido modificado, `trust` vira `0` na hora e a execução é bloqueada (`DENY`)**!

## Exemplo
```ini
# Habilitar verificacao criptografica de integridade SHA-256 em tempo real no /etc/fapolicyd/fapolicyd.conf e exigir hashes SHA-256 no RPM
permissive = 0
trust = rpmdb,file
integrity = sha256
rpm_sha256_only = 1
syslog_format = rule,dec,perm,auid,pid,exe,:,path,ftype,trust
```

## Limites e trade-offs
E por que isso não deixa o servidor lento se calcular `SHA-256` consome CPU? Graças ao **Object Cache (`obj_cache_size = 8191`)** do `fapolicyd`! O hash `SHA-256` é calculado apenas na **primeira vez** que o binário ou biblioteca entra no cache de objetos; nas milhares de execuções seguintes, o veredito já está validado em memória RAM!

## Como verificar
Executando **`fapolicyd-cli --check-trustdb`**, você visualiza imediatamente no terminal qualquer arquivo do sistema cujo tamanho ou hash `SHA-256` atual no disco divirja do `rpmdb` ou do `trust.d`!

## Conexões
- [[fapolicyd-gerenciamento-trust-database-fapolicyd-cli-file-add-trust-d]] — Veja também: Gerenciando o **Banco de Confiança (`trust.d/`)** com **`fapolicyd-cli`**: Autorizando Binários Customizados, Agentes de Terceiros e Aplicações em `/opt`.
- [[fapolicyd-modo-permissivo-debug-deny-testes-seguros-producao]] — Veja também: Testando Políticas sem Risco de Lockout no fapolicyd: Modo **`--permissive`**, Diagnóstico **`--debug-deny`** e Interpretação dos Eventos de Negação.
- [[fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb]] — Referência cruzada direta com fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb.
- [[keylime-monitoramento-integridade-runtime-linux-ima-allowlists-polices]] — Referência cruzada direta com keylime-monitoramento-integridade-runtime-linux-ima-allowlists-polices.

## Fontes
- [Official `fapolicyd` GitHub Repository (`linux-application-whitelisting/fapolicyd`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/README.md) — repositório oficial do File Access Policy Daemon cobrindo interceptação de execução via `fanotify`, linguagem de regras `allow`/`deny_audit`, `fapolicyd-cli` e banco de confiança; consultado em 2026-10-03.
- [Official `fapolicyd.conf` Configuration Specification (`init/fapolicyd.conf`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/init/fapolicyd.conf) — especificação oficial de configuração do `/etc/fapolicyd/fapolicyd.conf` detalhando `permissive`, `trust = rpmdb,file`, `integrity = none|size|ima|sha256`, `watch_fs` e caches LRU; consultado em 2026-10-03.
