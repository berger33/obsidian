---
id: software.devops.tranche16.001549
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

# Timoni: transporte de bundles, runtimes e arquivos arbitrários com `timoni artifact push` e `pull`

## Em uma frase
Enquanto `timoni mod` gerencia módulos CUE estruturados, o subcomando `timoni artifact` (`push`, `pull`, `list`, `tag`) transporta diretórios arbitrários — como definições de `bundle.cue`, arquivos `runtime.cue` e configurações de entrega — como artefatos OCI genéricos sem semântica de módulo.

## Por que importa
Em fluxos GitOps baseados em OCI (onde controladores no cluster ou pipelines de CD buscam a definição de deploy a partir de um registry em vez de clonar repositórios Git via SSH), é necessário publicar os próprios arquivos `bundle.cue` e `runtime.cue` no registry.

## Como funciona
O operador empacota e envia o diretório de entrega com `timoni artifact push oci://registry.example.com/org/delivery -f ./delivery -t 1.0.0` e pode adicionar tags de ambiente (`timoni artifact tag oci://.../delivery:1.0.0 -t prod`). No estágio de implantação, `timoni artifact pull oci://.../delivery:prod -o ./deploy` extrai os arquivos para execução imediata do `timoni bundle apply`.

## Exemplo
```bash
timoni artifact push oci://ghcr.io/org/clusters/prod-eu -f ./delivery -t 1.0.0
timoni artifact tag oci://ghcr.io/org/clusters/prod-eu:1.0.0 -t latest
timoni artifact pull oci://ghcr.io/org/clusters/prod-eu:latest -o /tmp/prod-eu-delivery
```

## Limites e trade-offs
Diferentemente de `timoni mod push` (que exige versionamento SemVer estrito e valida a estrutura CUE do módulo), `timoni artifact push` aceita tags arbitrárias (como nomes de branch ou ambientes) e empacota qualquer conteúdo de diretório.

## Como verificar
Execute `timoni artifact list oci://ghcr.io/org/clusters/prod-eu` para listar todas as tags e digests disponíveis para o artefato de entrega.

## Conexões
- [[timoni-assinatura-verificacao-modulos-cosign-sigstore]] — Veja também: Timoni: assinatura criptográfica (`--sign`) e verificação (`--verify`) de módulos OCI com Cosign.
- [[timoni-integracao-agentes-ia-skills-mcp-server-operacao]] — Veja também: Timoni: operação assistida por agentes de IA via Agent Skills e servidor MCP de documentação.

## Fontes
- [Timoni GitHub — README.md (CUE-Powered Kubernetes Package Manager, Modules, Bundles, OCI Artifacts & AI Agent MCP Integration)](https://raw.githubusercontent.com/stefanprodan/timoni/main/README.md) — README oficial do stefanprodan/timoni detalhando a arquitetura CUE, comparação com Helm/Kustomize, fluxo de módulos e bundles e integração MCP; consultado em 2026-10-03.
- [Timoni Official Documentation — Concepts (Module, Instance, Bundle, OCI Artifact Media Types, Flux SSA Drift Detection & Cosign Signing)](https://timoni.sh/concepts) — Documentação oficial de conceitos do Timoni cobrindo vendoring de CRDs, Server-Side Apply com garbage collection, bundles e media types OCI; consultado em 2026-10-03.
- [Timoni — Official GitHub Repository](https://github.com/stefanprodan/timoni) — Repositório oficial Apache-2.0 do Timoni; consultado em 2026-10-03.
