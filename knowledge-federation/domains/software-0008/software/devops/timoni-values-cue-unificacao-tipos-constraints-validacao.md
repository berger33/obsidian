---
id: software.devops.tranche16.001544
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

# Timoni: customização de instâncias via `values.cue` e validação por unificação de tipos CUE

## Em uma frase
Ao instanciar ou atualizar um módulo Timoni (`-f values.cue`), os valores fornecidos pelo usuário são mesclados com os padrões do módulo por meio da operação de unificação comutativa e associativa da linguagem CUE.

## Por que importa
No Helm, um arquivo `values.yaml` mal indentado ou com um valor fora da faixa permitida pode passar silenciosamente ou gerar um erro críptico de `nil pointer evaluating interface` no meio de um template.

## Como funciona
No Timoni, o esquema do módulo (`#Config` em `templates/config.cue`) define tipos, valores default (marcados com `*`) e restrições matemáticas ou de expressão regular (como `replicas: *1 | int & >=1 & <=100`). Quando o usuário passa `values.cue`, o avaliador CUE unifica as duas árvores; qualquer violação de restrição é reportada com o caminho exato do campo antes de qualquer chamada à API do Kubernetes.

## Exemplo
```cue
// values-prod.cue
values: {
	ingress: {
		enabled:   true
		className: "nginx"
		host:      "app.example.com"
	}
	autoscaling: enabled: true
	monitoring:  enabled: true
}
```

## Limites e trade-offs
Como em CUE os tipos e os valores fazem parte do mesmo reticulado (*values are types*), um valor default sem o marcador de preferência `*` torna o campo imutável (constante), impedindo que o usuário o sobrescreva em `values.cue`.

## Como verificar
Execute `timoni inspect values payments -n prod` em uma instância instalada para visualizar a configuração resultante da unificação entre os defaults do módulo e o `values.cue`.

## Conexões
- [[timoni-instance-server-side-apply-flux-drift-detection-gc]] — Veja também: Timoni: reconciliação de Instances com Server-Side Apply, detecção de drift Flux e Garbage Collector.
- [[timoni-bundles-composicao-multi-modulos-digest-pinning]] — Veja também: Timoni: composição declarativa de aplicações e dependências com `bundle.cue` e pinagem por digest.

## Fontes
- [Timoni GitHub — README.md (CUE-Powered Kubernetes Package Manager, Modules, Bundles, OCI Artifacts & AI Agent MCP Integration)](https://timoni.sh/concepts) — README oficial do stefanprodan/timoni detalhando a arquitetura CUE, comparação com Helm/Kustomize, fluxo de módulos e bundles e integração MCP; consultado em 2026-10-03.
- [Timoni Official Documentation — Concepts (Module, Instance, Bundle, OCI Artifact Media Types, Flux SSA Drift Detection & Cosign Signing)](https://raw.githubusercontent.com/stefanprodan/timoni/main/README.md) — Documentação oficial de conceitos do Timoni cobrindo vendoring de CRDs, Server-Side Apply com garbage collection, bundles e media types OCI; consultado em 2026-10-03.
- [Timoni — Official GitHub Repository](https://github.com/stefanprodan/timoni) — Repositório oficial Apache-2.0 do Timoni; consultado em 2026-10-03.
