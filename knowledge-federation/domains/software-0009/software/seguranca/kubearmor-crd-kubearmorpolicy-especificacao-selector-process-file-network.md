---
id: software.seguranca.tranche03.000212
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
fontes: ["https://raw.githubusercontent.com/kubearmor/KubeArmor/main/getting-started/security_policy_specification.md", "https://raw.githubusercontent.com/kubearmor/KubeArmor/main/README.md", "https://github.com/kubearmor/KubeArmor"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# KubeArmor `KubeArmorPolicy` (`ksp`): anatomia da política para Pods/Containers (`selector`, `process`, `file`, `network`, `capabilities`, `action`)

## Em uma frase
Conforme a especificação oficial *Specification of Security Policy for Containers* (`getting-started/security_policy_specification.md`), uma política **`KubeArmorPolicy`** (`apiVersion: security.kubearmor.com/v1`) seleciona Pods por labels (`selector.matchLabels` / `matchExpressions`) e governa cinco subsistemas do container: **`process`**, **`file`**, **`network`**, **`capabilities`** e **`syscalls`**, aplicando uma **`action`** (`Block`, `Audit` ou `Allow`, sendo **`Block`** o padrão!).

## Por que importa
Sem uma política de runtime no nível do container, um invasor que explore uma vulnerabilidade RCE na aplicação web pode invocar `/bin/sh`, `/usr/bin/apt`, `/usr/bin/curl` ou ler o token da ServiceAccount em `/var/run/secrets/kubernetes.io/serviceaccount/token`.

## Como funciona
No `KubeArmorPolicy`, você atribui `severity` (de `1` a `10`), `tags` (ex.: `["MITRE", "CIS", "PCI-DSS"]`), `message` e declara exatamente quais caminhos (`matchPaths`), diretórios (`matchDirectories` com `recursive: true`) ou protocolos (`matchProtocols`) devem ser bloqueados ou auditados.

## Exemplo
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: ksp-block-package-managers
  namespace: production
spec:
  severity: 8
  tags: ["CIS", "MITRE_T1059"]
  message: "Execução de gerenciadores de pacotes bloqueada em produção"
  selector:
    matchLabels:
      app: checkout-api
  process:
    matchPaths:
      - path: /usr/bin/apt
      - path: /usr/bin/apt-get
      - path: /sbin/apk
  action: Block
```

## Limites e trade-offs
Atenção à nota oficial da especificação: na seção `selector`, quando `matchLabels` e `matchExpressions` são usados juntos, eles operam como uma condição lógica **`AND`**; além disso, para a seção `syscalls`, apenas a ação `Audit` é suportada.

## Como verificar
Aplique a política com `kubectl apply -f policy.yaml` e verifique seu status com `kubectl get ksp -n production`.

## Conexões
- [[kubearmor-arquitetura-cncf-runtime-security-enforcement-lsm-ebpf]] — Veja também: CNCF KubeArmor: arquitetura de segurança em runtime com bloqueio inline no kernel via `Linux Security Modules (LSMs)` e `eBPF`.
- [[kubearmor-restricao-processos-fromsource-owneronly-recursive]] — Veja também: KubeArmor Controle Fino de Execução de Processos: `fromSource`, `ownerOnly` e `matchDirectories` recursivos.

## Fontes
- [CNCF KubeArmor GitHub — README.md (Cloud-Native Runtime Security Enforcement System, LSMs AppArmor/SELinux/BPF-LSM, eBPF & Architecture)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/getting-started/security_policy_specification.md) — README oficial do kubearmor/KubeArmor descrevendo o bloqueio inline no kernel via LSMs, casos de uso Zero-Trust e ecossistema karmor; consultado em 2026-10-03.
- [CNCF KubeArmor Official Documentation — Security Policy Specification for Containers (KubeArmorPolicy selector, process, file, network, capabilities & action)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/README.md) — Especificação oficial da KubeArmorPolicy detalhando matchPaths, matchDirectories, fromSource, ownerOnly, readOnly e ações Allow/Audit/Block; consultado em 2026-10-03.
- [CNCF KubeArmor — Official GitHub Repository](https://github.com/kubearmor/KubeArmor) — Repositório oficial Apache-2.0 do CNCF KubeArmor; consultado em 2026-10-03.
