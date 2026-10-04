---
id: software.devops.tranche19.001857
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://tailscale.com/docs/kubernetes-operator", "https://raw.githubusercontent.com/tailscale/tailscale/main/README.md", "https://github.com/tailscale/tailscale"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Tailscale SSH e `Recorder` (`tsrecorder`): autenticação SSH sem chaves pela *tailnet* e gravação de sessões no Kubernetes

## Em uma frase
O **Tailscale SSH** permite autenticar conexões SSH entre nós da *tailnet* usando a própria identidade criptográfica do WireGuard/Tailscale (sem distribuir chaves `~/.ssh/authorized_keys` e com opção de *check mode* que exige reautenticação MFA/SSO no navegador), enquanto o componente **`tsrecorder`** grava sessões SSH e `kubectl exec` para auditoria.

## Por que importa
Gerenciar chaves públicas SSH estáticas de ex-funcionários em centenas de VMs e auditar sessões interativas de terminal em clusters Kubernetes exige infraestrutura pesada se feito com ferramentas legadas.

## Como funciona
No Tailscale Kubernetes Operator, o Custom Resource **`Recorder`** implanta instâncias do `tsrecorder` no cluster (enviando gravações no formato asciicast para um bucket S3 ou volume persistente) para capturar tanto sessões **Tailscale SSH** quanto sessões **`kubectl exec` / `attach`** que passam pelo API Server Proxy.

## Exemplo
```yaml
apiVersion: tailscale.com/v1alpha1
kind: Recorder
metadata:
  name: prod-session-recorder
spec:
  replicas: 1
  enableUI: true
  storage:
    s3:
      endpoint: s3.amazonaws.com
      bucket: corp-tailscale-audit-logs
```

## Limites e trade-offs
Se a regra de política SSH definir `"recorder": ["tag:session-recorder"]` com `enforceRecorder: true` (padrão de falha fechada), caso nenhum nó `tsrecorder` esteja acessível no momento da conexão, a sessão será bloqueada por segurança.

## Como verificar
Implante um `Recorder` via operador (`kubectl get recorders`) e teste uma sessão auditada verificando a geração do log no storage configurado.

## Conexões
- [[tailscale-acls-grants-tags-autoapprovers-politica-zero-trust]] — Veja também: Tailscale Políticas Zero-Trust (ACLs e `Grants`): controle de acesso baseado em identidade, `tagOwners` e `autoApprovers`.
- [[tailscale-magicdns-split-dns-search-domains-resolucao-nomes]] — Veja também: Tailscale MagicDNS e Split DNS: resolução automática de nomes `.ts.net` e encaminhamento seletivo por domínio.

## Fontes
- [Tailscale GitHub — README.md (Private WireGuard Networks Made Easy, tailscaled Daemon & tailscale CLI)](https://tailscale.com/docs/kubernetes-operator) — README oficial do tailscale/tailscale descrevendo o daemon tailscaled, a CLI tailscale e suporte multiplataforma; consultado em 2026-10-03.
- [Tailscale Official Documentation — Tailscale Kubernetes Operator (API Server Proxy, Ingress, Egress, Connector, Multi-Cluster & Session Recorder)](https://raw.githubusercontent.com/tailscale/tailscale/main/README.md) — Documentação oficial do Tailscale Kubernetes Operator detalhando exposição de workloads, egresso para a tailnet, Connector CRD (Subnet Router/Exit Node) e Recorder; consultado em 2026-10-03.
- [Tailscale — Official GitHub Repository](https://github.com/tailscale/tailscale) — Repositório oficial BSD-3-Clause do cliente e daemon Tailscale; consultado em 2026-10-03.
