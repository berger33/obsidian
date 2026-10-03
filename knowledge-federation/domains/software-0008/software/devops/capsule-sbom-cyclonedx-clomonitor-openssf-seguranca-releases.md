---
id: software.devops.tranche15.001489
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/projectcapsule/capsule/main/README.md", "https://raw.githubusercontent.com/projectcapsule/capsule-proxy/main/README.md", "https://github.com/projectcapsule/capsule"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Capsule: artefatos OCI com SBOM CycloneDX JSON, conformidade OpenSSF Best Practices e CLOMonitor

## Em uma frase
Todos os artefatos de release OCI do projeto Capsule incluem um *Software Bill of Materials* (SBOM) em formato CycloneDX JSON, acompanhados por verificação contínua no OpenSSF Scorecard, CII Best Practices e CLOMonitor da CNCF.

## Por que importa
Como o Capsule atua como webhook crítico de admissão no caminho de todas as operações de namespaces e políticas do cluster, auditar a cadeia de suprimentos de suas imagens e dependências Go é um requisito obrigatório em ambientes regulados.

## Como funciona
Os administradores podem inspecionar o SBOM CycloneDX publicado junto às releases no GitHub/GHCR, verificar relatórios de licenças FOSSA e consultar o histórico de versões compatível com Kubernetes vanilla `1.16+` em nuvens públicas e privadas.

## Exemplo
```bash
kubectl get deployment -n capsule-system capsule-controller-manager \
  -o jsonpath='{.spec.template.spec.containers[0].image}'
```

## Limites e trade-offs
Ao atualizar o Capsule entre versões minor/major (por exemplo migrando APIs `v1beta1` para `v1beta2`), atualize sempre os CRDs e o webhook conversion antes ou simultaneamente ao controlador conforme as notas de release do `CHANGELOG.md`.

## Como verificar
Verifique a imagem em execução do `capsule-controller-manager` e valide os CRDs instalados com `kubectl get crd | grep capsule.clastix.io`.

## Conexões
- [[capsule-combinado-kamaji-hard-vs-soft-multitenancy-kubernetes]] — Veja também: Capsule e Kamaji: escolha e combinação entre Soft Multi-Tenancy (namespaces) e Hard Multi-Tenancy (control planes).
- [[capsule-operacao-producao-alta-disponibilidade-webhooks-troubleshooting]] — Veja também: Capsule: operação em produção, alta disponibilidade do controlador de admissão e diagnóstico de webhooks.

## Fontes
- [Capsule GitHub — README.md (Multi-Tenancy Operator, Tenant Abstraction, Policy Engine, Self-Service Namespaces, BYOD & CycloneDX SBOM)](https://raw.githubusercontent.com/projectcapsule/capsule/main/README.md) — README oficial do projectcapsule/capsule (CNCF Sandbox) detalhando a prevenção de cluster sprawl via CRD Tenant, herança automática de políticas/cotas e modelo BYOD; consultado em 2026-10-03.
- [Capsule Proxy GitHub — README.md (Filtered Cluster-Scoped Resource Listing, ProxySetting vs GlobalProxySettings Security Boundary)](https://raw.githubusercontent.com/projectcapsule/capsule-proxy/main/README.md) — README oficial do projectcapsule/capsule-proxy explicando a filtragem de recursos cluster-scoped para tenants e a fronteira de segurança entre ProxySetting e GlobalProxySettings; consultado em 2026-10-03.
- [Project Capsule — Official GitHub Repository](https://github.com/projectcapsule/capsule) — Repositório oficial Apache-2.0 do Capsule na CNCF; consultado em 2026-10-03.
