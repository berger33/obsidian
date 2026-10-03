---
id: software.devops.tranche16.001547
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/stefanprodan/timoni/main/README.md", "https://timoni.sh/concepts", "https://github.com/stefanprodan/timoni"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Timoni: distribuição de módulos e bundles como artefatos OCI reproduzíveis (`application/vnd.timoni.*`)

## Em uma frase
O Timoni empacota e distribui módulos e arquivos de entrega como artefatos Open Container Initiative (OCI) com media types dedicados e metadados determinísticos extraídos do Git.

## Por que importa
Diferentemente de repositórios HTTP legados de `index.yaml` (que crescem indefinidamente e exigem reindexação a cada pacote publicado), o armazenamento em registries OCI aproveita a mesma infraestrutura de autenticação, replicação e escaneamento usada para imagens de container.

## Como funciona
Os artefatos gerados pelo Timoni usam o manifesto `application/vnd.oci.image.manifest.v1+json`, config `application/vnd.timoni.config.v1+json` e camada `application/vnd.timoni.content.v1.tar+gzip`. Para garantir builds reproduzíveis, o Timoni fixa a data de modificação do artefato e preenche as anotações OCI de URL de origem e revisão a partir dos metadados do repositório Git.

## Exemplo
```bash
timoni mod build ./my-app -v 1.0.0 -o my-app-1.0.0.oci.tar
timoni mod push ./my-app oci://ghcr.io/org/modules/my-app -v 1.0.0
timoni mod list oci://ghcr.io/org/modules/my-app
```

## Limites e trade-offs
O comando `timoni mod build -o arquivo.oci.tar` gera um arquivo OCI local não assinado voltado para transporte offline (handoff), enquanto `timoni mod push` publica diretamente no registry semântico.

## Como verificar
Execute `timoni mod list oci://ghcr.io/stefanprodan/modules/podinfo` para inspecionar as versões SemVer e os digests publicados no registry.

## Conexões
- [[timoni-bundle-runtime-injecao-dinamica-segredos-multi-cluster]] — Veja também: Timoni: carregamento dinâmico de segredos e parâmetros de cluster via Bundle Runtime (`--runtime`).
- [[timoni-assinatura-verificacao-modulos-cosign-sigstore]] — Veja também: Timoni: assinatura criptográfica (`--sign`) e verificação (`--verify`) de módulos OCI com Cosign.

## Fontes
- [Timoni GitHub — README.md (CUE-Powered Kubernetes Package Manager, Modules, Bundles, OCI Artifacts & AI Agent MCP Integration)](https://raw.githubusercontent.com/stefanprodan/timoni/main/README.md) — README oficial do stefanprodan/timoni detalhando a arquitetura CUE, comparação com Helm/Kustomize, fluxo de módulos e bundles e integração MCP; consultado em 2026-10-03.
- [Timoni Official Documentation — Concepts (Module, Instance, Bundle, OCI Artifact Media Types, Flux SSA Drift Detection & Cosign Signing)](https://timoni.sh/concepts) — Documentação oficial de conceitos do Timoni cobrindo vendoring de CRDs, Server-Side Apply com garbage collection, bundles e media types OCI; consultado em 2026-10-03.
- [Timoni — Official GitHub Repository](https://github.com/stefanprodan/timoni) — Repositório oficial Apache-2.0 do Timoni; consultado em 2026-10-03.
