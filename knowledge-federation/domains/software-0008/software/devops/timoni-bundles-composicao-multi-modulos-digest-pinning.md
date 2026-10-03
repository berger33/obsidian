---
id: software.devops.tranche16.001545
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

# Timoni: composição declarativa de aplicações e dependências com `bundle.cue` e pinagem por digest

## Em uma frase
Um Timoni *Bundle* (`bundle.cue`, `apiVersion: "v1alpha1"`) define declarativamente um grupo de instâncias de módulos (por exemplo, um banco Redis e a aplicação `podinfo` que o consome), permitindo travar versões por SemVer ou por digest OCI (`sha256:...`).

## Por que importa
Aplicações modernas raramente consistem em um único workload isolado; elas exigem caches, filas e bancos de dados coordenados, onde a URL de conexão de uma instância precisa ser derivada dinamicamente dos parâmetros de outra instância.

## Como funciona
Em um arquivo `bundle.cue`, o autor declara o mapa `bundle.instances`, apontando cada instância para seu `module.url` (`oci://...`), `version` e/ou `digest`, `namespace` e `values`. Como o próprio bundle é escrito em CUE, é possível usar interpolação de strings, operações aritméticas e referências cruzadas entre instâncias, aplicando todo o conjunto com `timoni bundle apply -f bundle.cue`.

## Exemplo
```cue
bundle: {
	apiVersion: "v1alpha1"
	name:       "podinfo-stack"
	instances: {
		redis: {
			module: {
				url:     "oci://ghcr.io/stefanprodan/modules/redis"
				version: "8.10.1"
				digest:  "sha256:4f377b66fd6d608f6a347bbef5b4fcd1aaff3dfa253b1c8437ae8e11fa08b70a"
			}
			namespace: "podinfo"
			values: maxmemory: 256
		}
		podinfo: {
			module: {
				url:     "oci://ghcr.io/stefanprodan/modules/podinfo"
				version: "6.14.1"
			}
			namespace: "podinfo"
			values: caching: {
				enabled:  true
				redisURL: "tcp://redis:6379"
			}
		}
	}
}
```

## Limites e trade-offs
É possível dividir um bundle em múltiplos arquivos CUE (por exemplo `timoni bundle build -f bundle.cue -f bundle_secrets.cue`), permitindo manter segredos criptografados separadamente da topologia base da aplicação.

## Como verificar
Valide a sintaxe e o esquema do bundle com `timoni bundle vet -f bundle.cue` e visualize o diff no cluster com `timoni bundle apply -f bundle.cue --diff --dry-run`.

## Conexões
- [[timoni-values-cue-unificacao-tipos-constraints-validacao]] — Veja também: Timoni: customização de instâncias via `values.cue` e validação por unificação de tipos CUE.
- [[timoni-bundle-runtime-injecao-dinamica-segredos-multi-cluster]] — Veja também: Timoni: carregamento dinâmico de segredos e parâmetros de cluster via Bundle Runtime (`--runtime`).

## Fontes
- [Timoni GitHub — README.md (CUE-Powered Kubernetes Package Manager, Modules, Bundles, OCI Artifacts & AI Agent MCP Integration)](https://timoni.sh/concepts) — README oficial do stefanprodan/timoni detalhando a arquitetura CUE, comparação com Helm/Kustomize, fluxo de módulos e bundles e integração MCP; consultado em 2026-10-03.
- [Timoni Official Documentation — Concepts (Module, Instance, Bundle, OCI Artifact Media Types, Flux SSA Drift Detection & Cosign Signing)](https://raw.githubusercontent.com/stefanprodan/timoni/main/README.md) — Documentação oficial de conceitos do Timoni cobrindo vendoring de CRDs, Server-Side Apply com garbage collection, bundles e media types OCI; consultado em 2026-10-03.
- [Timoni — Official GitHub Repository](https://github.com/stefanprodan/timoni) — Repositório oficial Apache-2.0 do Timoni; consultado em 2026-10-03.
