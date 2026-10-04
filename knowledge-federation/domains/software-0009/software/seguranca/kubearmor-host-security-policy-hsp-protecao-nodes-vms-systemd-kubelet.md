---
id: software.seguranca.tranche03.000218
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

# KubeArmor `KubeArmorHostPolicy` (`hsp`): hardening de Nós Kubernetes e Servidores Linux Bare-Metal/VM

## Em uma frase
Além de proteger containers, o KubeArmor protege o **próprio sistema operacional do Nó (VM ou Bare-Metal)** por meio do CRD **`KubeArmorHostPolicy`** (`kind: KubeArmorHostPolicy`, abreviado como `hsp`), selecionando nós via `nodeSelector.matchLabels` e restringindo processos, arquivos, rede, capabilities e syscalls diretamente no host!

## Por que importa
Se um invasor escapar de um container mal configurado ou obtiver acesso SSH a um nó worker do Kubernetes, ele tentará ler `/etc/shadow`, modificar unidades do `systemd`, alterar a configuração do `kubelet` (`/var/lib/kubelet/config.yaml`) ou ler as chaves privadas do `etcd` em `/etc/kubernetes/pki/`.

## Como funciona
O `KubeArmorHostPolicy` opera tanto em nós de um cluster Kubernetes quanto em máquinas virtuais Linux standalone (onde o KubeArmor roda como serviço `systemd` ou container Docker sem Kubernetes), bloqueando modificações em `/boot`, `/etc/sudoers` e `/etc/kubernetes/` no nível do LSM do host.

## Exemplo
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorHostPolicy
metadata:
  name: hsp-audit-and-block-shadow-access
spec:
  severity: 10
  tags: ["MITRE_T1003", "HOST_HARDENING"]
  message: "Acesso não autorizado ao arquivo /etc/shadow do nó bloqueado"
  nodeSelector:
    matchLabels:
      kubernetes.io/os: linux
  file:
    matchPaths:
      - path: /etc/shadow
        fromSource:
          - path: /bin/cat
          - path: /usr/bin/awk
  action: Block
```

## Limites e trade-offs
Tenha extremo cuidado ao aplicar `KubeArmorHostPolicy` com `action: Block` sobre diretórios amplos do nó (`/usr`, `/var/lib/kubelet`, `/run`): teste sempre primeiro com `action: Audit` para garantir que agentes legítimos do nó (`kubelet`, `containerd`, CNI) não sejam bloqueados!

## Como verificar
Verifique as políticas de host aplicadas com `kubectl get hsp` e monitore eventos de host com `karmor logs --logFilter policy`.

## Conexões
- [[kubearmor-cluster-security-policy-csp-governanca-multi-namespace]] — Veja também: KubeArmor `KubeArmorClusterPolicy` (`csp`): políticas de segurança em nível de cluster através de múltiplos namespaces.
- [[kubearmor-cli-karmor-logs-profile-recommend-telemetria-tempo-real]] — Veja também: KubeArmor CLI (`karmor`): streaming de telemetria e alertas (`karmor logs`), perfilamento (`karmor profile`) e `karmor recommend`.

## Fontes
- [CNCF KubeArmor GitHub — README.md (Cloud-Native Runtime Security Enforcement System, LSMs AppArmor/SELinux/BPF-LSM, eBPF & Architecture)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/README.md) — README oficial do kubearmor/KubeArmor descrevendo o bloqueio inline no kernel via LSMs, casos de uso Zero-Trust e ecossistema karmor; consultado em 2026-10-03.
- [CNCF KubeArmor Official Documentation — Security Policy Specification for Containers (KubeArmorPolicy selector, process, file, network, capabilities & action)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/getting-started/security_policy_specification.md) — Especificação oficial da KubeArmorPolicy detalhando matchPaths, matchDirectories, fromSource, ownerOnly, readOnly e ações Allow/Audit/Block; consultado em 2026-10-03.
- [CNCF KubeArmor — Official GitHub Repository](https://github.com/kubearmor/KubeArmor) — Repositório oficial Apache-2.0 do CNCF KubeArmor; consultado em 2026-10-03.
