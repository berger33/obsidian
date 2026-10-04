---
id: software.seguranca.tranche05.000470
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

# Linux Audit (`auditd`): Monitoramento de Hosts de Containers, sockets de Runtime (`/run/containerd`, `/var/run/docker.sock`) e Isolamento de `auditd`

## Em uma frase
Em nós que hospedam containers (Kubernetes, containerd, CRI-O, Docker), o `auditd` roda exclusivamente no sistema operacional do host (pois o subsistema de auditoria do kernel não é isolado por namespaces de usuário comuns) e monitora toda atividade originada dentro dos containers além do acesso aos sockets do runtime.

## Por que importa
Conforme documentado no README oficial do `audit-userspace`, tentar confinar o próprio `auditd.service` dentro de namespaces restritivos sugeridos cegamente pelo `systemd-analyze security` quebra o funcionamento das regras de auditoria e o acesso às bases de usuários do host.

## Como funciona
Nos nós de cluster, adicione regras `-w` específicas para monitorar o binário e os sockets do runtime (`/usr/bin/containerd`, `/usr/bin/runc`, `/run/containerd/containerd.sock`, `/etc/kubernetes/manifests`, `/var/lib/kubelet/config.yaml`) e utilize `log_format = ENRICHED` manteniendo o `auditd` no namespace raiz do host.

## Exemplo
```ini
# /etc/audit/rules.d/50-container-runtime.rules
-w /usr/bin/containerd -p x -k container_runtime_exec
-w /usr/bin/runc -p x -k container_runtime_exec
-w /run/containerd/containerd.sock -p rwxa -k containerd_socket_access
-w /etc/kubernetes/manifests -p wa -k k8s_static_pods_tamper
-w /var/lib/kubelet/config.yaml -p wa -k kubelet_config_tamper
```

## Limites e trade-offs
Monitorar `-w /var/lib/containerd -p rwxa` recursivamente em todo o diretório de camadas de overlay gerará milhões de eventos por segundo durante pulls e escritas de disco dos pods; monitore apenas os binários de runtime, sockets de controle e arquivos de configuração.

## Como verificar
Carregue `50-container-runtime.rules` com `sudo augenrules --load` e execute `sudo crictl ps`, confirmando o registro do acesso ao socket via `sudo ausearch -k containerd_socket_access -i`.

## Conexões
- [[auditd-streaming-tempo-real-audisp-af-unix-remote-siem]] — Veja também: Linux Audit (`auditd`): Streaming em Tempo Real com Plugins `audisp` (`/etc/audit/plugins.d/`, `af_unix` e `audisp-remote` TLS/Kerberos).
- [[auditd-arquitetura-linux-audit-kernel-auditctl-augenrules]] — Referência cruzada direta com auditd-arquitetura-linux-audit-kernel-auditctl-augenrules.
- [[auditd-exclusao-ruido-never-exit-cron-containers-alta-performance]] — Referência cruzada direta com auditd-exclusao-ruido-never-exit-cron-containers-alta-performance.

## Fontes
- [Linux Audit Userspace Official GitHub — Architecture & Daemon Considerations](https://raw.githubusercontent.com/linux-audit/audit-userspace/master/README.md) — documentação oficial do Linux Audit System (auditd, auditctl, augenrules, audisp e RefuseManualStop); consultado em 2026-10-03.
- [Linux Audit Official Rules — README-rules & augenrules Ordering](https://raw.githubusercontent.com/linux-audit/audit-userspace/master/rules/README-rules) — especificação oficial da organização de regras 10–99 em /etc/audit/rules.d/ e 31-privileged.rules; consultado em 2026-10-03.
- [Linux Audit Rules Repository — STIG, PCI-DSS & Base Rules](https://github.com/linux-audit/audit-userspace/tree/master/rules) — catálogo oficial de regras de auditoria para Common Criteria, DISA STIG e PCI-DSS; consultado em 2026-10-03.
