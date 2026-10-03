---
id: software.devops.tranche16.001546
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
fontes: ["https://timoni.sh/concepts", "https://raw.githubusercontent.com/stefanprodan/timoni/main/README.md", "https://github.com/stefanprodan/timoni"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Timoni: carregamento dinâmico de segredos e parâmetros de cluster via Bundle Runtime (`--runtime`)

## Em uma frase
O recurso de *Bundle Runtime* (`timoni bundle apply -f bundle.cue --runtime runtime.cue`) permite carregar dinamicamente no momento do deploy valores existentes no próprio cluster Kubernetes (como Secrets de vaults, ConfigMaps de plataforma ou metadados de região) e injetá-los nos bundles.

## Por que importa
Hardcodar senhas de banco de dados, tokens de API ou nomes de domínio específicos de cada cluster dentro do arquivo `bundle.cue` versionado no Git viola boas práticas de segurança e impede o reuso do mesmo arquivo de bundle entre múltiplos clusters (staging, prod-us, prod-eu).

## Como funciona
O arquivo `runtime.cue` declara seletores de consulta a recursos do cluster (`Secret`, `ConfigMap`, `Service`) e até frotas de múltiplos clusters (`kubeconfig`). Antes de avaliar o `bundle.cue`, o Timoni lê esses valores da API do Kubernetes em memória e os injeta nos atributos `@timoni(runtime:...)` declarados no bundle.

## Exemplo
```bash
timoni bundle vet -f bundle.cue --runtime runtime.cue
timoni bundle apply -f bundle.cue --runtime runtime.cue --diff
```

## Limites e trade-offs
Se uma chave de `Secret` ou `ConfigMap` referenciada como obrigatória no `runtime.cue` ainda não existir no cluster alvo no momento da execução do comando, o Timoni abortará a avaliação antes de aplicar qualquer instância do bundle.

## Como verificar
Execute `timoni bundle apply -f bundle.cue --runtime runtime.cue --dry-run --diff` para validar a resolução dos valores de runtime contra o cluster sem aplicar mudanças.

## Conexões
- [[timoni-bundles-composicao-multi-modulos-digest-pinning]] — Veja também: Timoni: composição declarativa de aplicações e dependências com `bundle.cue` e pinagem por digest.
- [[timoni-oci-artifacts-media-types-builds-reprodutiveis-git]] — Veja também: Timoni: distribuição de módulos e bundles como artefatos OCI reproduzíveis (`application/vnd.timoni.*`).

## Fontes
- [Timoni GitHub — README.md (CUE-Powered Kubernetes Package Manager, Modules, Bundles, OCI Artifacts & AI Agent MCP Integration)](https://timoni.sh/concepts) — README oficial do stefanprodan/timoni detalhando a arquitetura CUE, comparação com Helm/Kustomize, fluxo de módulos e bundles e integração MCP; consultado em 2026-10-03.
- [Timoni Official Documentation — Concepts (Module, Instance, Bundle, OCI Artifact Media Types, Flux SSA Drift Detection & Cosign Signing)](https://raw.githubusercontent.com/stefanprodan/timoni/main/README.md) — Documentação oficial de conceitos do Timoni cobrindo vendoring de CRDs, Server-Side Apply com garbage collection, bundles e media types OCI; consultado em 2026-10-03.
- [Timoni — Official GitHub Repository](https://github.com/stefanprodan/timoni) — Repositório oficial Apache-2.0 do Timoni; consultado em 2026-10-03.
