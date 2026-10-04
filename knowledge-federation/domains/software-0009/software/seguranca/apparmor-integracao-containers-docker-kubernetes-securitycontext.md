---
id: software.seguranca.tranche05.000487
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
fontes: ["https://gitlab.com/apparmor/apparmor/-/raw/master/README.md", "https://gitlab.com/apparmor/apparmor/-/wikis/home", "https://gitlab.com/apparmor/apparmor/-/wikis/Documentation"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# AppArmor: Confinamento de Containers e Pods Kubernetes (`securityContext.appArmorProfile` GA no Kubernetes v1.30+)

## Em uma frase
O AppArmor é suportado nativamente pelo Docker (`--security-opt apparmor=<perfil>`), pelo `containerd`/`CRI-O` e pela especificação oficial do Kubernetes através do campo nativo **`securityContext.appArmorProfile`** (estável/GA a partir do Kubernetes v1.30, substituindo a antiga anotação `container.apparmor.security.beta.kubernetes.io/*`).

## Por que importa
O perfil padrão de containers (`container-default` / `docker-default`) bloqueia a montagem de sistemas de arquivos e escrita em `/proc/sys`, mas ainda permite que processos dentro do container executem shells, gravem na maior parte do filesystem do container e abram conexões de rede arbitrárias; perfis customizados por workload trancam o pod ao mínimo estrito.

## Como funciona
Nos nós de trabalho do cluster, um DaemonSet ou gerenciador de configuração (ou o *Security Profiles Operator*) carrega o perfil customizado em `/etc/apparmor.d/` via `apparmor_parser -r`. No manifesto do Pod (ou container individual), declara-se `appArmorProfile.type: Localhost` e `localhostProfile: k8s-payments-worker`.

## Exemplo
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: payments-worker
  namespace: production
spec:
  securityContext:
    appArmorProfile:
      type: Localhost
      localhostProfile: k8s-payments-worker
  containers:
    - name: worker
      image: registry.internal.corp/payments/worker@sha256:9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
```

## Limites e trade-offs
Perfis de containers em Kubernetes **devem** declarar a flag `flags=(attach_disconnected,mediate_deleted)` no cabeçalho do perfil para lidar corretamente com namespaces de montagem (`mount namespaces`) e sockets abertos antes do `pivot_root` do container.

## Como verificar
Dentro do nó onde o pod foi agendado, verifique `/proc/<PID>/attr/current` do processo do container e confirme que ele exibe `k8s-payments-worker (enforce)`.

## Conexões
- [[apparmor-geracao-aprendizado-perfis-aa-genprof-aa-logprof-auditd]] — Veja também: AppArmor: Criação e Refinamento Guiado de Perfis com `aa-genprof`, `aa-logprof` e `aa-autodep`.
- [[apparmor-subperfis-change-hat-pam-apparmor-mod-apparmor]] — Veja também: AppArmor: Mudança Dinâmica de Privilégio Intra-Processo com `aa_change_hat(2)`, `aa_change_profile(2)` e `pam_apparmor`.
- [[apparmor-arquitetura-lsm-mandatory-access-control-path-based-profiles]] — Referência cruzada direta com apparmor-arquitetura-lsm-mandatory-access-control-path-based-profiles.
- [[apparmor-regras-arquivos-capabilities-network-mount-ptrace-signal]] — Referência cruzada direta com apparmor-regras-arquivos-capabilities-network-mount-ptrace-signal.

## Fontes
- [AppArmor Official GitLab — Kernel LSM & Userspace Architecture](https://gitlab.com/apparmor/apparmor/-/raw/master/README.md) — documentação oficial do projeto AppArmor cobrindo o módulo LSM do kernel, libapparmor, parser e utilitários; consultado em 2026-10-03.
- [AppArmor Official Wiki — Home & Profiles Overview](https://gitlab.com/apparmor/apparmor/-/wikis/home) — wiki oficial do AppArmor sobre perfis de confinamento, distribuições e ferramentas de política; consultado em 2026-10-03.
- [AppArmor Official Wiki — Technical Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/Documentation) — documentação técnica da linguagem de perfis, transições de execução e abstrações do AppArmor; consultado em 2026-10-03.
