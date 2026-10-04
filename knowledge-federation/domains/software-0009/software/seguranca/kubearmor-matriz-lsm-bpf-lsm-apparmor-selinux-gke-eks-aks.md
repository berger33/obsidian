---
id: software.seguranca.tranche03.000220
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

# KubeArmor Matriz de LSMs (`BPF-LSM` vs `AppArmor` vs `SELinux`): escolha de sistema operacional de nó em `EKS`, `GKE`, `AKS` e `RKE`

## Em uma frase
Conforme detalhado na documentação oficial do KubeArmor, a capacidade de bloqueio inline (`action: Block`) depende do **Linux Security Module (LSM)** disponível no kernel do nó: **`BPF-LSM`** (Linux 5.7+ com `CONFIG_BPF_LSM=y` e `lsm=bpf,...` nos parâmetros de boot do kernel), **`AppArmor`** (padrão no Ubuntu, Debian e imagens Google **GKE Container-Optimized OS — COS**) ou **`SELinux`** (para políticas de host em RHEL/Fedora/CentOS).

## Por que importa
Se você provisionar nós worker no Amazon EKS usando a imagem *Amazon Linux 2* antiga (kernel 4.14/5.10 sem AppArmor e sem BPF-LSM ativado no boot), o KubeArmor conseguirá **auditar (`Audit`)** via eBPF, mas não terá um LSM para **bloquear (`Block`)** containers!

## Como funciona
Para ter suporte completo e moderno ao **`BPF-LSM`** (que anexa programas eBPF diretamente aos hooks de segurança do kernel sem depender de perfis textuais do AppArmor), utilize imagens de nó com kernel moderno (como **Amazon Linux 2023**, **Bottlerocket**, **Ubuntu 22.04/24.04** ou **GKE COS**) e verifique a lista de LSMs ativos em `/sys/kernel/security/lsm`!

## Exemplo
```bash
# Verificando no nó Linux quais Linux Security Modules (LSMs) estão ativos no kernel:
cat /sys/kernel/security/lsm
# Saída esperada para suporte moderno a BPF-LSM ou AppArmor:
# lockdown,capability,landlock,yama,apparmor,bpf
```

## Limites e trade-offs
Caso `bpf` não esteja listado em `/sys/kernel/security/lsm` mesmo em um kernel 5.15+, basta adicionar `bpf` à lista do parâmetro de kernel `lsm=...` no GRUB (ou habilitar o container init `kubearmor-init` que configura o ambiente automaticamente).

## Como verificar
Rode `karmor probe` após o boot dos nós para confirmar `Enforcement: true` e o LSM selecionado.

## Conexões
- [[kubearmor-cli-karmor-logs-profile-recommend-telemetria-tempo-real]] — Veja também: KubeArmor CLI (`karmor`): streaming de telemetria e alertas (`karmor logs`), perfilamento (`karmor profile`) e `karmor recommend`.

## Fontes
- [CNCF KubeArmor GitHub — README.md (Cloud-Native Runtime Security Enforcement System, LSMs AppArmor/SELinux/BPF-LSM, eBPF & Architecture)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/README.md) — README oficial do kubearmor/KubeArmor descrevendo o bloqueio inline no kernel via LSMs, casos de uso Zero-Trust e ecossistema karmor; consultado em 2026-10-03.
- [CNCF KubeArmor Official Documentation — Security Policy Specification for Containers (KubeArmorPolicy selector, process, file, network, capabilities & action)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/getting-started/security_policy_specification.md) — Especificação oficial da KubeArmorPolicy detalhando matchPaths, matchDirectories, fromSource, ownerOnly, readOnly e ações Allow/Audit/Block; consultado em 2026-10-03.
- [CNCF KubeArmor — Official GitHub Repository](https://github.com/kubearmor/KubeArmor) — Repositório oficial Apache-2.0 do CNCF KubeArmor; consultado em 2026-10-03.
