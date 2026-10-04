---
id: software.devops.tranche16.001543
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

# Timoni: reconciliação de Instances com Server-Side Apply, detecção de drift Flux e Garbage Collector

## Em uma frase
Para aplicar e atualizar uma *Instance* no cluster (`timoni apply`, `install` ou `upgrade`), o Timoni utiliza o Kubernetes Server-Side Apply (SSA) combinado com o motor de detecção de drift do Flux e um coletor de lixo (*Garbage Collector*) transacional.

## Por que importa
Atualizações baseadas em three-way merge client-side frequentemente entram em conflito com mutating webhooks ou deixam recursos órfãos no cluster quando um objeto (como um `Ingress` ou `ServiceMonitor`) é desabilitado nos valores de uma nova versão.

## Como funciona
Durante o `timoni apply`, a ferramenta primeiro valida todos os recursos gerados com um *dry-run* Server-Side Apply contra o `kube-apiserver`, reconcilia apenas os objetos que apresentam mudanças reais em relação ao estado do cluster e aguarda a convergência (`Ready`) de Deployments, Jobs, Services, Ingresses e CRs. Em upgrades, o Timoni grava a nova revisão como `pending` no armazenamento da instância antes de tocar no cluster, só a marca como aplicada após a reconciliação concluir e remove automaticamente objetos órfãos da revisão anterior.

## Exemplo
```bash
timoni apply payments ./my-webapp -n prod -f values-prod.cue --dry-run --diff
timoni apply payments ./my-webapp -n prod -f values-prod.cue --wait
timoni status payments -n prod
```

## Limites e trade-offs
Se um upgrade for interrompido no meio da execução (por exemplo, por queda do runner de CI), a revisão fica registrada como pendente: a próxima execução retoma a partir do estado gravado, e um eventual `timoni delete` limpa recursos de ambas as revisões.

## Como verificar
Execute `timoni inspect resources payments -n prod` e `timoni status payments -n prod` para auditar o inventário exato de objetos gerenciados e suas condições de prontidão.

## Conexões
- [[timoni-mod-vendor-k8s-crds-schemas-cue-tipagem-estrita]] — Veja também: Timoni: importação de schemas da API Kubernetes e CRDs (`timoni mod vendor k8s` e `vendor crds`).
- [[timoni-values-cue-unificacao-tipos-constraints-validacao]] — Veja também: Timoni: customização de instâncias via `values.cue` e validação por unificação de tipos CUE.

## Fontes
- [Timoni GitHub — README.md (CUE-Powered Kubernetes Package Manager, Modules, Bundles, OCI Artifacts & AI Agent MCP Integration)](https://timoni.sh/concepts) — README oficial do stefanprodan/timoni detalhando a arquitetura CUE, comparação com Helm/Kustomize, fluxo de módulos e bundles e integração MCP; consultado em 2026-10-03.
- [Timoni Official Documentation — Concepts (Module, Instance, Bundle, OCI Artifact Media Types, Flux SSA Drift Detection & Cosign Signing)](https://raw.githubusercontent.com/stefanprodan/timoni/main/README.md) — Documentação oficial de conceitos do Timoni cobrindo vendoring de CRDs, Server-Side Apply com garbage collection, bundles e media types OCI; consultado em 2026-10-03.
- [Timoni — Official GitHub Repository](https://github.com/stefanprodan/timoni) — Repositório oficial Apache-2.0 do Timoni; consultado em 2026-10-03.
