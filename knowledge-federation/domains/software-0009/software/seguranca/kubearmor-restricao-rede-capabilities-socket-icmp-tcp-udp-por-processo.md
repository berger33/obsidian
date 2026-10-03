---
id: software.seguranca.tranche03.000215
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

# KubeArmor Controle de Rede (`network`) e Linux Capabilities (`capabilities`) por Executável (`fromSource`)

## Em uma frase
Diferente das `NetworkPolicies` padrão do Kubernetes (que operam na camada 3/4 para o Pod inteiro, sem saber qual processo dentro do Pod abriu o socket), as seções **`network.matchProtocols`** (`tcp`, `udp`, `icmp`, `raw`) e **`capabilities.matchCapabilities`** do KubeArmor operam no nível do socket/capability do kernel e aceitam **`fromSource`** para restringir operações de rede **por binário executável**!

## Por que importa
Se uma `NetworkPolicy` do Kubernetes libera saída na porta TCP 443 para que o binário `/app/server` converse com uma API externa, qualquer exploit que invoque `/usr/bin/curl` ou `/usr/bin/nc` dentro do mesmo Pod também conseguiria usar aquela saída TCP 443 se o filtro for apenas por IP do Pod!

## Como funciona
No KubeArmor, você pode bloquear a criação de sockets `tcp`, `udp` e `icmp` especificamente para utilitários de linha de comando (ou permitir rede apenas para `/app/server`), além de bloquear o uso de Linux Capabilities críticas como `net_raw` ou `sys_admin`.

## Exemplo
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: ksp-block-raw-sockets-and-icmp
  namespace: production
spec:
  severity: 7
  selector:
    matchLabels:
      tier: backend
  network:
    matchProtocols:
      - protocol: icmp
      - protocol: raw
  capabilities:
    matchCapabilities:
      - capability: net_raw
  action: Block
```

## Limites e trade-offs
Conforme a documentação oficial `security_policy_specification.md`, os nomes de protocolos aceitos em `matchProtocols` são `TCP`/`tcp`, `UDP`/`udp`, `ICMP`/`icmp` e `RAW`/`raw`.

## Como verificar
Teste executar `ping 8.8.8.8` de dentro do Pod protegido e confirme que a criação do socket ICMP/RAW é negada pelo LSM.

## Conexões
- [[kubearmor-protecao-arquivos-sensi-readonly-fromsource-serviceaccount-token]] — Veja também: KubeArmor Proteção de Arquivos e Segredos (`file`): `readOnly: true`, vínculo `fromSource` e blindagem do Token da ServiceAccount.
- [[kubearmor-politicas-default-posture-allow-whitelist-least-permissive]] — Veja também: KubeArmor Postura *Zero-Trust Whitelisting* (`action: Allow` + `kubearmor-file-posture` / `kubearmor-Visibility`): modelo de privilégio mínimo.

## Fontes
- [CNCF KubeArmor GitHub — README.md (Cloud-Native Runtime Security Enforcement System, LSMs AppArmor/SELinux/BPF-LSM, eBPF & Architecture)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/getting-started/security_policy_specification.md) — README oficial do kubearmor/KubeArmor descrevendo o bloqueio inline no kernel via LSMs, casos de uso Zero-Trust e ecossistema karmor; consultado em 2026-10-03.
- [CNCF KubeArmor Official Documentation — Security Policy Specification for Containers (KubeArmorPolicy selector, process, file, network, capabilities & action)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/README.md) — Especificação oficial da KubeArmorPolicy detalhando matchPaths, matchDirectories, fromSource, ownerOnly, readOnly e ações Allow/Audit/Block; consultado em 2026-10-03.
- [CNCF KubeArmor — Official GitHub Repository](https://github.com/kubearmor/KubeArmor) — Repositório oficial Apache-2.0 do CNCF KubeArmor; consultado em 2026-10-03.
