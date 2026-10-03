---
id: software.devops.tranche19.001856
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

# Tailscale Políticas Zero-Trust (ACLs e `Grants`): controle de acesso baseado em identidade, `tagOwners` e `autoApprovers`

## Em uma frase
No Tailscale, o controle de acesso da rede (*Zero-Trust Network Access*) é definido declarativamente em um arquivo HuJSON (JSON com comentários) contendo **`grants`** (ou `acls`), **`tagOwners`**, **`autoApprovers`**, **`ssh`** e **`tests`**, compilado pelo plano de controle em filtros de pacotes aplicados diretamente na interface de cada nó.

## Por que importa
Uma rede mesh onde qualquer laptop conectado pode acessar todas as portas de todos os servidores de produção permitiria movimentação lateral imediata caso uma estação fosse comprometida.

## Como funciona
Atribuir uma **Tag** (ex.: `tag:prod-db`) a um servidor remove a identidade pessoal do humano que o registrou e passa a tratá-lo como uma identidade de máquina governada por `tagOwners`. Com `grants`, é possível restringir não apenas IP e porta, mas também permissões de aplicação (como acesso ao proxy do Kubernetes API Server).

## Exemplo
```json
{
  "tagOwners": {
    "tag:k8s-operator": ["autogroup:admin"],
    "tag:prod-app": ["tag:k8s-operator"]
  },
  "grants": [
    {
      "src": ["group:sre"],
      "dst": ["tag:prod-app"],
      "ip": ["tcp:443", "tcp:8080"]
    }
  ]
}
```

## Limites e trade-offs
Inclua sempre blocos `"tests"` e `"sshTests"` no próprio arquivo de política HuJSON: o plano de controle executa os testes automaticamente a cada alteração e rejeita salvar a política se algum teste de permissão/negação falhar.

## Como verificar
Valide suas regras declarando asserções `accept` e `deny` na seção `"tests"` da política da *tailnet*.

## Conexões
- [[tailscale-connector-crd-subnet-router-exit-node-kubernetes]] — Veja também: Tailscale `Connector` CRD: implantação declarativa de Subnet Routers e Exit Nodes em alta disponibilidade no Kubernetes.
- [[tailscale-ssh-session-recording-tsrecorder-kubernetes-auditoria]] — Veja também: Tailscale SSH e `Recorder` (`tsrecorder`): autenticação SSH sem chaves pela *tailnet* e gravação de sessões no Kubernetes.

## Fontes
- [Tailscale GitHub — README.md (Private WireGuard Networks Made Easy, tailscaled Daemon & tailscale CLI)](https://tailscale.com/docs/kubernetes-operator) — README oficial do tailscale/tailscale descrevendo o daemon tailscaled, a CLI tailscale e suporte multiplataforma; consultado em 2026-10-03.
- [Tailscale Official Documentation — Tailscale Kubernetes Operator (API Server Proxy, Ingress, Egress, Connector, Multi-Cluster & Session Recorder)](https://raw.githubusercontent.com/tailscale/tailscale/main/README.md) — Documentação oficial do Tailscale Kubernetes Operator detalhando exposição de workloads, egresso para a tailnet, Connector CRD (Subnet Router/Exit Node) e Recorder; consultado em 2026-10-03.
- [Tailscale — Official GitHub Repository](https://github.com/tailscale/tailscale) — Repositório oficial BSD-3-Clause do cliente e daemon Tailscale; consultado em 2026-10-03.
