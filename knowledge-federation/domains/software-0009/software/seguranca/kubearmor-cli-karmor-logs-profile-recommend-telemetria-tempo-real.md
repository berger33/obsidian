---
id: software.seguranca.tranche03.000219
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

# KubeArmor CLI (`karmor`): streaming de telemetria e alertas (`karmor logs`), perfilamento (`karmor profile`) e `karmor recommend`

## Em uma frase
Conforme listado na tabela de repositórios Core do README oficial (`kubearmor/kubearmor-client`), a ferramenta de linha de comando **`karmor`** é a interface operacional oficial para instalar, inspecionar (`karmor probe`), acompanhar telemetria e alertas em tempo real (**`karmor logs`**), perfilar o comportamento de cargas de trabalho (**`karmor profile`**) e gerar políticas recomendadas (**`karmor recommend`**).

## Por que importa
Escrever políticas de segurança de runtime do zero sem saber exatamente quais arquivos e processos um container acessa em execução normal exige tentativa e erro.

## Como funciona
Com `karmor logs` (conectado via gRPC ao serviço `kubearmor-relay`), você filtra em tempo real alertas de políticas (`--logFilter policy`) ou eventos de sistema (`--logFilter system`) por namespace, pod, operação (`Process`, `File`, `Network`) e exporta em JSON para integração com SIEM/Fluentd/Wazuh.

## Exemplo
```bash
# Acompanhando em tempo real apenas os alertas de violação de política (Block/Audit) em formato JSON:
karmor logs --logFilter policy --json

# Filtrando telemetria de execução de processos de um namespace específico:
karmor logs -n production --operation Process
```

## Limites e trade-offs
Para reduzir o overhead de telemetria em clusters de altíssima escala, ajuste a anotação `kubearmor-visibility` por namespace (ex.: `process,file,network` em namespaces críticos ou `none` onde desejar apenas alertas de violação de política sem logar todas as chamadas permitidas).

## Como verificar
Execute `karmor summary` e `karmor logs --logFilter policy` para auditar o comportamento das políticas em execução.

## Conexões
- [[kubearmor-host-security-policy-hsp-protecao-nodes-vms-systemd-kubelet]] — Veja também: KubeArmor `KubeArmorHostPolicy` (`hsp`): hardening de Nós Kubernetes e Servidores Linux Bare-Metal/VM.
- [[kubearmor-matriz-lsm-bpf-lsm-apparmor-selinux-gke-eks-aks]] — Veja também: KubeArmor Matriz de LSMs (`BPF-LSM` vs `AppArmor` vs `SELinux`): escolha de sistema operacional de nó em `EKS`, `GKE`, `AKS` e `RKE`.

## Fontes
- [CNCF KubeArmor GitHub — README.md (Cloud-Native Runtime Security Enforcement System, LSMs AppArmor/SELinux/BPF-LSM, eBPF & Architecture)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/README.md) — README oficial do kubearmor/KubeArmor descrevendo o bloqueio inline no kernel via LSMs, casos de uso Zero-Trust e ecossistema karmor; consultado em 2026-10-03.
- [CNCF KubeArmor Official Documentation — Security Policy Specification for Containers (KubeArmorPolicy selector, process, file, network, capabilities & action)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/getting-started/security_policy_specification.md) — Especificação oficial da KubeArmorPolicy detalhando matchPaths, matchDirectories, fromSource, ownerOnly, readOnly e ações Allow/Audit/Block; consultado em 2026-10-03.
- [CNCF KubeArmor — Official GitHub Repository](https://github.com/kubearmor/KubeArmor) — Repositório oficial Apache-2.0 do CNCF KubeArmor; consultado em 2026-10-03.
