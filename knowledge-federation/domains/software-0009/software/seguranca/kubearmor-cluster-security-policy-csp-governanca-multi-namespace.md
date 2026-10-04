---
id: software.seguranca.tranche03.000217
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/kubearmor/KubeArmor/main/README.md", "https://raw.githubusercontent.com/kubearmor/KubeArmor/main/getting-started/security_policy_specification.md", "https://github.com/kubearmor/KubeArmor"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# KubeArmor `KubeArmorClusterPolicy` (`csp`): políticas de segurança em nível de cluster através de múltiplos namespaces

## Em uma frase
Conforme listado no README oficial (*Cluster level security Policy for Pods/Containers*), o CRD **`KubeArmorClusterPolicy`** (`apiVersion: security.kubearmor.com/v1`, `kind: KubeArmorClusterPolicy`) permite que a equipe de Plataforma/SecOps aplique regras de segurança transversalmente em ** múltiplos ou todos os namespaces do cluster** usando seletores `matchLabels` ou `matchExpressions` sobre namespaces e pods.

## Por que importa
Criar e manter sincronizadas 80 cópias idênticas de uma `KubeArmorPolicy` (por exemplo, bloqueando acesso ao metadado de nuvem ou execução de mineradores) em 80 namespaces diferentes é propenso a esquecimento quando uma nova squad cria o 81º namespace.

## Como funciona
Com `KubeArmorClusterPolicy`, uma única definição em escopo de cluster protege automaticamente todos os namespaces selecionados (ou todos os namespaces exceto `kube-system` usando `operator: NotIn`), aplicando governança uniforme desde o primeiro segundo de vida de qualquer novo namespace.

## Exemplo
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorClusterPolicy
metadata:
  name: csp-protect-ca-certificates-clusterwide
spec:
  severity: 9
  tags: ["CIS", "CLUSTER_BASELINE"]
  message: "Modificação do bundle de autoridades certificadoras (CA) bloqueada em todo o cluster"
  selector:
    matchExpressions:
      - key: namespace
        operator: NotIn
        values:
          - kube-system
          - kubearmor
  file:
    matchDirectories:
      - dir: /etc/ssl/certs/
        recursive: true
        readOnly: true
  action: Block
```

## Limites e trade-offs
Restrinja via Kubernetes RBAC a permissão de criar/editar objetos `KubeArmorClusterPolicy` exclusivamente à equipe de Segurança/Plataforma, deixando `KubeArmorPolicy` namespaced para políticas específicas de cada aplicação.

## Como verificar
Liste todas as políticas de cluster ativas com `kubectl get csp`.

## Conexões
- [[kubearmor-politicas-default-posture-allow-whitelist-least-permissive]] — Veja também: KubeArmor Postura *Zero-Trust Whitelisting* (`action: Allow` + `kubearmor-file-posture` / `kubearmor-Visibility`): modelo de privilégio mínimo.
- [[kubearmor-host-security-policy-hsp-protecao-nodes-vms-systemd-kubelet]] — Veja também: KubeArmor `KubeArmorHostPolicy` (`hsp`): hardening de Nós Kubernetes e Servidores Linux Bare-Metal/VM.

## Fontes
- [CNCF KubeArmor GitHub — README.md (Cloud-Native Runtime Security Enforcement System, LSMs AppArmor/SELinux/BPF-LSM, eBPF & Architecture)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/README.md) — README oficial do kubearmor/KubeArmor descrevendo o bloqueio inline no kernel via LSMs, casos de uso Zero-Trust e ecossistema karmor; consultado em 2026-10-03.
- [CNCF KubeArmor Official Documentation — Security Policy Specification for Containers (KubeArmorPolicy selector, process, file, network, capabilities & action)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/getting-started/security_policy_specification.md) — Especificação oficial da KubeArmorPolicy detalhando matchPaths, matchDirectories, fromSource, ownerOnly, readOnly e ações Allow/Audit/Block; consultado em 2026-10-03.
- [CNCF KubeArmor — Official GitHub Repository](https://github.com/kubearmor/KubeArmor) — Repositório oficial Apache-2.0 do CNCF KubeArmor; consultado em 2026-10-03.
