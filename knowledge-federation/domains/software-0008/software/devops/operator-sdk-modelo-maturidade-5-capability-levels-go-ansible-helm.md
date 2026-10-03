---
id: software.devops.tranche18.001752
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-18.md"
fontes: ["https://sdk.operatorframework.io/docs/overview/", "https://raw.githubusercontent.com/operator-framework/operator-sdk/master/README.md", "https://github.com/operator-framework/operator-sdk"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Operator SDK: modelo de maturidade de 5 níveis (*Operator Capability Levels*) e comparação entre Go, Ansible e Helm

## Em uma frase
A documentação oficial do Operator SDK define o modelo de maturidade de **5 níveis de capacidade (*Operator Capability Levels*)** para orientar a escolha entre operadores baseados em Helm, Ansible ou Go.

## Por que importa
Iniciar um projeto como Helm Operator quando o requisito de negócio exige failover automático de shards, reconfiguração dinâmica de topologia e auto-tuning (Nível 5) levará a um beco sem saída arquitetural.

## Como funciona
Os cinco níveis de maturidade são: **Level I — Basic Install** (provisionamento automatizado e configuração); **Level II — Seamless Upgrades** (atualizações de patch e minor version suportadas); **Level III — Full Lifecycle** (ciclo de vida da aplicação, backup e recuperação de falhas); **Level IV — Deep Insights** (métricas Prometheus, alertas, processamento de logs e análise de carga); e **Level V — Auto Pilot** (auto-scaling horizontal/vertical, auto-configuração, detecção de anomalias e *auto-healing*). Enquanto Helm Operators cobrem bem os níveis I e II, Go e Ansible Operators alcançam do nível I até o nível V.

## Exemplo
```bash
# Comparando os plugins disponíveis na inicialização do projeto:
operator-sdk init --help
```

## Limites e trade-offs
Mesmo quando você começa com um Helm Operator simples, o layout baseado em Kubebuilder facilita migrar ou reimplementar o mesmo CRD posteriormente em Go caso a complexidade operacional evolua para o Nível V.

## Como verificar
Avalie os requisitos de Dia 2 do seu sistema stateful contra os 5 níveis de capacidade antes de escolher `--plugins=helm`, `--plugins=ansible` ou `--plugins=go`.

## Conexões
- [[operator-sdk-arquitetura-operator-framework-go-ansible-helm]] — Veja também: Operator SDK: arquitetura do kit CNCF Incubating para criação de Operators em Go, Ansible e Helm.
- [[operator-sdk-ansible-operator-watches-yaml-roles-playbooks]] — Veja também: Operator SDK `ansible-operator`: reconciliação de Custom Resources via `watches.yaml`, Roles e Playbooks Ansible.

## Fontes
- [Operator SDK GitHub — README.md (Operator Framework Toolkit, Controller-Runtime Integration & Metrics Authn/Authz Notice)](https://sdk.operatorframework.io/docs/overview/) — README oficial do operator-framework/operator-sdk detalhando a arquitetura do SDK e a substituição do kube-rbac-proxy por WithAuthenticationAndAuthorization; consultado em 2026-10-03.
- [Operator SDK Official Documentation — Overview (Go/Ansible/Helm Workflows, 5 Capability Levels, Kubernetes/client-go & OLM Compatibility)](https://raw.githubusercontent.com/operator-framework/operator-sdk/master/README.md) — Documentação oficial Overview do Operator SDK cobrindo fluxos Go/Ansible/Helm, 5 níveis de maturidade, versões embutidas do OLM e suporte multi-arquitetura; consultado em 2026-10-03.
- [Operator SDK — Official GitHub Repository](https://github.com/operator-framework/operator-sdk) — Repositório oficial Apache-2.0 do Operator SDK na CNCF; consultado em 2026-10-03.
