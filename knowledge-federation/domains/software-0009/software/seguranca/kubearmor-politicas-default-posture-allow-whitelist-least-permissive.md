---
id: software.seguranca.tranche03.000216
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

# KubeArmor Postura *Zero-Trust Whitelisting* (`action: Allow` + `kubearmor-file-posture` / `kubearmor-Visibility`): modelo de privilégio mínimo

## Em uma frase
O KubeArmor suporta duas abordagens de política: **Denylisting (`action: Block`)**, onde tudo é permitido exceto o que a política proíbe, e **Allowlisting / Least Permissive Access (`action: Allow`)**, onde você declara apenas os processos, arquivos e protocolos permitidos para a aplicação e o KubeArmor **bloqueia automaticamente tudo o mais** de acordo com a postura padrão (*Default Posture*) do namespace ou pod!

## Por que importa
Tentar listar em uma *denylist* todos os binários perigosos possíveis em uma distribuição Linux (`curl`, `wget`, `python`, `perl`, `nc`, `socat`, `dd`, `base64`) é frágil; se o container só precisa executar `/app/checkout-service`, uma política `action: Allow` reduz a superfície de ataque a um único binário!

## Como funciona
A postura padrão para recursos não cobertos por regras `Allow` é controlada por anotações no Namespace (ou flags globais): `kubearmor-file-posture: block|audit`, `kubearmor-network-posture: block|audit` e `kubearmor-capabilities-posture: block|audit`.

## Exemplo
```yaml
# Política de Allowlist (Zero-Trust): permite apenas que /bin/sh inicie /app/service e que /app/service acesse /app/conf/:
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: ksp-zero-trust-allowlist
  namespace: secure-apps
spec:
  severity: 9
  selector:
    matchLabels:
      app: vault-connector
  process:
    matchPaths:
      - path: /app/service
      - path: /bin/sh
  file:
    matchDirectories:
      - dir: /app/conf/
        recursive: true
        readOnly: true
      - dir: /lib/
        recursive: true
      - dir: /usr/lib/
        recursive: true
  action: Allow
```

## Limites e trade-offs
Sempre inicie políticas `action: Allow` com a postura padrão do namespace em modo **`audit`** (`kubectl annotate ns secure-apps kubearmor-file-posture=audit kubearmor-network-posture=audit`), valide em staging que nenhuma biblioteca dinâmica compartilhada (`/lib`, `/etc/ld.so.cache`) faltou na lista e só então mude a postura para `block`!

## Como verificar
Inspecione os alertas de postura com `karmor logs --namespace secure-apps` antes de ativar o bloqueio estrito.

## Conexões
- [[kubearmor-restricao-rede-capabilities-socket-icmp-tcp-udp-por-processo]] — Veja também: KubeArmor Controle de Rede (`network`) e Linux Capabilities (`capabilities`) por Executável (`fromSource`).
- [[kubearmor-cluster-security-policy-csp-governanca-multi-namespace]] — Veja também: KubeArmor `KubeArmorClusterPolicy` (`csp`): políticas de segurança em nível de cluster através de múltiplos namespaces.

## Fontes
- [CNCF KubeArmor GitHub — README.md (Cloud-Native Runtime Security Enforcement System, LSMs AppArmor/SELinux/BPF-LSM, eBPF & Architecture)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/getting-started/security_policy_specification.md) — README oficial do kubearmor/KubeArmor descrevendo o bloqueio inline no kernel via LSMs, casos de uso Zero-Trust e ecossistema karmor; consultado em 2026-10-03.
- [CNCF KubeArmor Official Documentation — Security Policy Specification for Containers (KubeArmorPolicy selector, process, file, network, capabilities & action)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/README.md) — Especificação oficial da KubeArmorPolicy detalhando matchPaths, matchDirectories, fromSource, ownerOnly, readOnly e ações Allow/Audit/Block; consultado em 2026-10-03.
- [CNCF KubeArmor — Official GitHub Repository](https://github.com/kubearmor/KubeArmor) — Repositório oficial Apache-2.0 do CNCF KubeArmor; consultado em 2026-10-03.
