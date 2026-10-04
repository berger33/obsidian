---
id: software.seguranca.tranche15.001438
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

# Tuning de Performance do **`/etc/fapolicyd/fapolicyd.conf`**: Sistemas de Arquivos Monitorados (`watch_fs`), `ignore_mounts`, Tamanho de Fila `q_size` e Cache Hit Ratio

## Em uma frase
Como dimensionar os parâmetros de performance do **`/etc/fapolicyd/fapolicyd.conf`** (`q_size`, `subj_cache_size`, `obj_cache_size`, `watch_fs`, `ignore_mounts`, `allow_filesystem_mark`) em servidores de alta carga ou hosts que compilam código/rodam muitos processos sem esgotar a fila do `fanotify`?

## Por que importa
Consultando o arquivo oficial `init/fapolicyd.conf`, quatro ajustes evitam gargalos: **(1) `watch_fs = ext2,ext3,ext4,tmpfs,xfs,vfat,iso9660,btrfs`** — define quais tipos de sistemas de arquivos são monitorados; **(2) `ignore_mounts = /caminho/mount1,/caminho/mount2`** — permite excluir pontos de montagem específicos de dados puros (onde a montagem já usa `noexec` no `/etc/fstab`!) para não gerar eventos `fanotify` desnecessários; **(3) `q_size = 800`** — o tamanho da fila interna de eventos (aumente para `1600` ou `3200` em servidores com picos intensos de criação de processos); e **(4) `subj_cache_size` e `obj_cache_size`**!

## Como funciona
Quando o serviço `fapolicyd` é parado ou periodicamente (`do_stat_report = 1`), ele grava o relatório detalhado de estatísticas em **`/var/log/fapolicyd-access.log`**: verifique ali se a taxa de **`Object cache hits`** está acima de 95% e se há `evictions` excessivas!

## Exemplo
```bash
# Inspecionar as configuracoes de fila, caches e sistemas de arquivos monitorados em /etc/fapolicyd/fapolicyd.conf e checar o relatorio de estatisticas
grep -E "^(q_size|subj_cache_size|obj_cache_size|watch_fs|integrity|trust)" /etc/fapolicyd/fapolicyd.conf
head -n 30 /var/log/fapolicyd-access.log || true
```

## Limites e trade-offs
Atenção ao uso do `fapolicyd` em hosts que rodam **Containers (Docker / Podman / Kubernetes)**: como os containers usam camadas `overlayfs` (`overlay`), por padrão `overlay` **não** está listado em `watch_fs` no `fapolicyd.conf` porque os arquivos dentro da imagem do container não constam no `rpmdb` do host! Para proteger workloads containerizados em runtime, proteja o host com `fapolicyd` e use **KubeArmor / Tetragon / Tracee** (ou **Keylime + IMA**) para os containers!

## Como verificar
Mantenha também `nice_val = 14` (ou menor se o servidor tiver CPU 100% saturada) para garantir que a thread de decisão do `fapolicyd` seja escalonada prontamente pelo Kernel.

## Conexões
- [[fapolicyd-bloqueio-interpretadores-python-shell-ld-so-evasao]] — Veja também: Blindando Interpretadores (**Python, Perl, Ruby, PHP, Lua, Node.js e Bash**) e Bloqueando Evasões `ld.so` / `/dev/shm` no fapolicyd.
- [[fapolicyd-auditoria-auditd-fanotify-syslog-format-correlacao-siem]] — Veja também: Correlação de Bloqueios do fapolicyd com **`auditd` (`FANOTIFY`)** e Customização do **`syslog_format`** para Detecção Imediata no SIEM.
- [[fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb]] — Referência cruzada direta com fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb.
- [[fapolicyd-verificacao-integridade-sha256-size-ima-anti-tampering]] — Referência cruzada direta com fapolicyd-verificacao-integridade-sha256-size-ima-anti-tampering.

## Fontes
- [Official `fapolicyd` GitHub Repository (`linux-application-whitelisting/fapolicyd`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/README.md) — repositório oficial do File Access Policy Daemon cobrindo interceptação de execução via `fanotify`, linguagem de regras `allow`/`deny_audit`, `fapolicyd-cli` e banco de confiança; consultado em 2026-10-03.
- [Official `fapolicyd.conf` Configuration Specification (`init/fapolicyd.conf`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/init/fapolicyd.conf) — especificação oficial de configuração do `/etc/fapolicyd/fapolicyd.conf` detalhando `permissive`, `trust = rpmdb,file`, `integrity = none|size|ima|sha256`, `watch_fs` e caches LRU; consultado em 2026-10-03.
