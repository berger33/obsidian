---
id: software.devops.tranche12.001120
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/score-spec/spec/main/README.md", "https://raw.githubusercontent.com/score-spec/score-k8s/main/README.md", "https://raw.githubusercontent.com/score-spec/score-compose/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Score: Integração do Score em Fluxos GitOps, Kratix Promises e Orquestradores de Plataforma

## Em uma frase
Por ser uma especificação puramente declarativa e unidirecional, o `score.yaml` funciona como a interface de entrada ideal para pipelines CI/CD que geram manifestos para Argo CD/Flux, Promises do Kratix ou plataformas baseadas em Score.

## Por que importa
Quando cada squad estrutura seu repositório de forma diferente, a plataforma não consegue automatizar deploys padronizados nem evoluir os operadores de infraestrutura sem quebrar os repositórios das aplicações.

## Como funciona
No pipeline de CI da aplicação, o desenvolvedor altera apenas o código e o `score.yaml`; o job de build compila a imagem de container, executa `score-k8s generate score.yaml --image <nova-tag>` (com os provisionadores e patch templates oficiais da plataforma) e faz commit do `manifests.yaml` resultante no repositório GitOps ou submete uma Resource Request para uma Promise do Kratix.

## Exemplo
```bash
# Exemplo em pipeline CI antes do commit GitOps:
score-k8s init --no-sample --provisioners https://platform.internal/provisioners.yaml
score-k8s generate score.yaml --image ghcr.io/org/order-api:${GIT_SHA} -o dist/manifests.yaml
kubectl kubeconform dist/manifests.yaml
```

## Limites e trade-offs
Permitir que desenvolvedores editem manualmente o `manifests.yaml` gerado pelo `score-k8s` no repositório GitOps faz com que as alterações manuais sejam sobrescritas na próxima execução automatizada do pipeline.

## Como verificar
Trate `manifests.yaml` e `compose.yaml` como artefatos gerados de forma determinística a partir do `score.yaml`, bloqueando edições manuais via revisão de CI.

## Conexões
- [[score-k8s-patch-templates-post-processing-customizacao]] — Veja também: Score: Pós-Processamento de Manifestos no score-k8s com --patch-templates.

## Fontes
- [Score Specification GitHub — README.md (score.dev/v1b1 Workload Spec, Containers, Service Ports & Resources)](https://raw.githubusercontent.com/score-spec/spec/main/README.md) — README oficial da especificação Score (score-spec/spec, Apache-2.0) detalhando o contrato declarativo score.yaml v1b1, interpolação ${resources.*} e separação entre configuração agnóstica e específica de ambiente; consultado em 2026-10-03.
- [Score Reference Implementations — score-compose & score-k8s Official READMEs](https://raw.githubusercontent.com/score-spec/score-k8s/main/README.md) — Documentação oficial das implementações de referência score-compose e score-k8s cobrindo matriz de recursos suportados, provisionadores customizados (template:// e cmd://) e --patch-templates; consultado em 2026-10-03.
- [Score — Official GitHub Organization & Repositories](https://raw.githubusercontent.com/score-spec/score-compose/main/README.md) — Repositórios oficiais do projeto Score na CNCF; consultado em 2026-10-03.
