---
id: software.seguranca.tranche05.000469
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/linux-audit/audit-userspace/master/README.md", "https://raw.githubusercontent.com/linux-audit/audit-userspace/master/rules/README-rules", "https://github.com/linux-audit/audit-userspace/tree/master/rules"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Linux Audit (`auditd`): Streaming em Tempo Real com Plugins `audisp` (`/etc/audit/plugins.d/`, `af_unix` e `audisp-remote` TLS/Kerberos)

## Em uma frase
Além de gravar no disco local, o `auditd` incorpora o multiplexador de eventos **`audisp`**, que distribui cada evento de auditoria em tempo real para plugins configurados em `/etc/audit/plugins.d/` (como `af_unix.conf`, `au-remote.conf` e `syslog.conf`).

## Por que importa
Se um atacante comprometer o `root` de um servidor sem modo imutável `-e 2` e apagar `/var/log/audit/audit.log`, os eventos já transmitidos em tempo real pelo `audisp` para um servidor central de logs ou coletor EDR permanecem preservados fora do alcance do invasor.

## Como funciona
O plugin `af_unix` expõe um socket UNIX local (`/var/run/audispd_events` com permissão `0640`) consumido por agentes locais de segurança (como Wazuh, Osquery ou Laurel), enquanto o plugin `audisp-remote` transmite os registros diretamente pela rede para um agregador central `auditd` usando autenticação mútua Kerrb5/GSSAPI ou TLS.

## Exemplo
```ini
# /etc/audit/plugins.d/af_unix.conf — Habilitar socket UNIX em tempo real para coletores locais de SIEM/EDR
active = yes
direction = out
path = builtin_af_unix
type = builtin
args = 0640 /var/run/audispd_events string
format = string
```

## Limites e trade-offs
Se a fila interna de plugins (`q_depth` em `/etc/audit/auditd.conf`) for subdimensionada e o plugin receptor travar, o `auditd` emitirá erros de *overflow* (`overflow_action`); dimensione `q_depth = 4096` em servidores com alto volume de eventos.

## Como verificar
Verifique com `sudo auditctl -s` e nos logs do `auditd` que o plugin configurado em `/etc/audit/plugins.d/` foi iniciado sem avisos de fila cheia.

## Conexões
- [[auditd-investigacao-forense-ausearch-aureport-auid-correlacao]] — Veja também: Linux Audit (`auditd`): Investigação Forense e Resposta a Incidentes com `ausearch` (`-i`, `-k`, `-ua`, `--session`) e `aureport`.
- [[auditd-rastreamento-containers-audit-container-id-namespaces]] — Veja também: Linux Audit (`auditd`): Monitoramento de Hosts de Containers, sockets de Runtime (`/run/containerd`, `/var/run/docker.sock`) e Isolamento de `auditd`.
- [[auditd-arquitetura-linux-audit-kernel-auditctl-augenrules]] — Referência cruzada direta com auditd-arquitetura-linux-audit-kernel-auditctl-augenrules.
- [[auditd-protecao-disco-particao-dedicada-space-left-action-halt]] — Referência cruzada direta com auditd-protecao-disco-particao-dedicada-space-left-action-halt.

## Fontes
- [Linux Audit Userspace Official GitHub — Architecture & Daemon Considerations](https://raw.githubusercontent.com/linux-audit/audit-userspace/master/README.md) — documentação oficial do Linux Audit System (auditd, auditctl, augenrules, audisp e RefuseManualStop); consultado em 2026-10-03.
- [Linux Audit Official Rules — README-rules & augenrules Ordering](https://raw.githubusercontent.com/linux-audit/audit-userspace/master/rules/README-rules) — especificação oficial da organização de regras 10–99 em /etc/audit/rules.d/ e 31-privileged.rules; consultado em 2026-10-03.
- [Linux Audit Rules Repository — STIG, PCI-DSS & Base Rules](https://github.com/linux-audit/audit-userspace/tree/master/rules) — catálogo oficial de regras de auditoria para Common Criteria, DISA STIG e PCI-DSS; consultado em 2026-10-03.
