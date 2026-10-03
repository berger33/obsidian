---
id: software.seguranca.tranche03.000211
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

# CNCF KubeArmor: arquitetura de segurança em runtime com bloqueio inline no kernel via `Linux Security Modules (LSMs)` e `eBPF`

## Em uma frase
Conforme documentado no README oficial (`kubearmor/KubeArmor`, projeto Sandbox da CNCF licenciado sob Apache 2.0), o **KubeArmor** é um sistema cloud-native de **aplicação de políticas de segurança em tempo de execução (*Runtime Security Enforcement*)** que restringe o comportamento de **Pods, Containers e Nós (VMs/Bare-Metal)** diretamente no nível do kernel usando **Linux Security Modules (`AppArmor`, `BPF-LSM` ou `SELinux`)** combinados com observabilidade **`eBPF`**.

## Por que importa
Ferramentas de segurança em runtime baseadas apenas em observar syscalls via eBPF em espaço de usuário detectam que um processo malicioso foi executado e enviam um alerta (ou tentam matar o processo depois que ele já rodou algumas instruções, sofrendo de *TOCTOU race conditions*); o KubeArmor usa **LSMs do kernel Linux** para **bloquear a chamada antes da execução (*inline enforcement*)**!

## Como funciona
Quando você aplica um CRD `KubeArmorPolicy` no Kubernetes, o DaemonSet do KubeArmor traduz a política para regras nativas do LSM ativo no nó (`BPF-LSM` ou `AppArmor`) e correlaciona toda telemetria e alertas de violação com os metadados do Pod, Container e Namespace via eBPF.

## Exemplo
```bash
# Instalando o cliente oficial karmor e verificando o ambiente e os LSMs suportados no cluster:
curl -sfL http://get.kubearmor.io/ | sudo sh -s -- -b /usr/local/bin
karmor probe
```

## Limites e trade-offs
O comando **`karmor probe`** inspeciona os nós do seu cluster Kubernetes (ou host local) e informa exatamente qual LSM está habilitado (`BPF-LSM`, `AppArmor` ou `SELinux`) e se o kernel atende todos os pré-requisitos para bloqueio inline.

## Como verificar
Execute `karmor probe` e `kubectl get pods -n kubearmor` para validar a saúde do DaemonSet e dos controladores.

## Conexões
- [[kubearmor-crd-kubearmorpolicy-especificacao-selector-process-file-network]] — Veja também: KubeArmor `KubeArmorPolicy` (`ksp`): anatomia da política para Pods/Containers (`selector`, `process`, `file`, `network`, `capabilities`, `action`).

## Fontes
- [CNCF KubeArmor GitHub — README.md (Cloud-Native Runtime Security Enforcement System, LSMs AppArmor/SELinux/BPF-LSM, eBPF & Architecture)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/README.md) — README oficial do kubearmor/KubeArmor descrevendo o bloqueio inline no kernel via LSMs, casos de uso Zero-Trust e ecossistema karmor; consultado em 2026-10-03.
- [CNCF KubeArmor Official Documentation — Security Policy Specification for Containers (KubeArmorPolicy selector, process, file, network, capabilities & action)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/getting-started/security_policy_specification.md) — Especificação oficial da KubeArmorPolicy detalhando matchPaths, matchDirectories, fromSource, ownerOnly, readOnly e ações Allow/Audit/Block; consultado em 2026-10-03.
- [CNCF KubeArmor — Official GitHub Repository](https://github.com/kubearmor/KubeArmor) — Repositório oficial Apache-2.0 do CNCF KubeArmor; consultado em 2026-10-03.
