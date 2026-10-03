---
id: software.devops.tranche16.001542
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

# Timoni: importação de schemas da API Kubernetes e CRDs (`timoni mod vendor k8s` e `vendor crds`)

## Em uma frase
O Timoni provê os comandos `timoni mod vendor k8s` e `timoni mod vendor crds` para importar definições Go/OpenAPI do Kubernetes e CustomResourceDefinitions em YAML diretamente para pacotes CUE dentro de `cue.mod/gen/`.

## Por que importa
Escrever manifestos de Custom Resources (como `Certificate` do cert-manager, `ServiceMonitor` do Prometheus Operator ou `VirtualService` do Istio) em templates tradicionais não oferece nenhuma verificação de compilação se um campo obrigatório do CRD mudar entre versões.

## Como funciona
Ao executar `timoni mod vendor k8s --version latest`, o Timoni popula `cue.mod/gen/k8s.io/` com as definições de tipos oficiais do Kubernetes. Da mesma forma, `timoni mod vendor crds -f crds.yaml` lê as especificações OpenAPI v3 de qualquer arquivo de CRDs e gera definições CUE fortemente tipadas que podem ser importadas pelos templates do módulo.

## Exemplo
```bash
timoni mod vendor k8s --version 1.31
timoni mod vendor crds -f https://github.com/cert-manager/cert-manager/releases/download/v1.16.1/cert-manager.crds.yaml
timoni mod vet .
```

## Limites e trade-offs
Após atualizar a versão dos CRDs vendored com `timoni mod vendor crds`, campos depreciados ou removidos pelo fornecedor do operador causarão falha imediata de unificação em `timoni mod vet`, exigindo atualização explícita do template do módulo.

## Como verificar
Verifique os arquivos `.cue` gerados dentro do diretório `cue.mod/gen/` e execute `timoni mod vet .` para comprovar a checagem estática dos Custom Resources.

## Conexões
- [[timoni-arquitetura-gerenciador-pacotes-kubernetes-cue-oci]] — Veja também: Timoni: arquitetura de gerenciamento de pacotes Kubernetes tipado com CUE e artefatos OCI.
- [[timoni-instance-server-side-apply-flux-drift-detection-gc]] — Veja também: Timoni: reconciliação de Instances com Server-Side Apply, detecção de drift Flux e Garbage Collector.

## Fontes
- [Timoni GitHub — README.md (CUE-Powered Kubernetes Package Manager, Modules, Bundles, OCI Artifacts & AI Agent MCP Integration)](https://timoni.sh/concepts) — README oficial do stefanprodan/timoni detalhando a arquitetura CUE, comparação com Helm/Kustomize, fluxo de módulos e bundles e integração MCP; consultado em 2026-10-03.
- [Timoni Official Documentation — Concepts (Module, Instance, Bundle, OCI Artifact Media Types, Flux SSA Drift Detection & Cosign Signing)](https://raw.githubusercontent.com/stefanprodan/timoni/main/README.md) — Documentação oficial de conceitos do Timoni cobrindo vendoring de CRDs, Server-Side Apply com garbage collection, bundles e media types OCI; consultado em 2026-10-03.
- [Timoni — Official GitHub Repository](https://github.com/stefanprodan/timoni) — Repositório oficial Apache-2.0 do Timoni; consultado em 2026-10-03.
