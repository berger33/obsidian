---
id: software.devops.tranche12.001119
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
fontes: ["https://raw.githubusercontent.com/score-spec/score-k8s/main/README.md", "https://raw.githubusercontent.com/score-spec/spec/main/README.md", "https://github.com/score-spec/score-k8s"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Score: Pós-Processamento de Manifestos no score-k8s com --patch-templates

## Em uma frase
O `score-k8s` permite ajustar ou enriquecer os manifestos Kubernetes gerados sem alterar a especificação `score.yaml` do desenvolvedor por meio da flag `--patch-templates` durante o `score-k8s init`.

## Por que importa
Equipes de plataforma e segurança frequentemente precisam injetar `securityContext` restritivo, labels de centro de custo, sidecars de malha de serviço ou `imagePullSecrets` em todos os Deployments gerados, sem poluir o arquivo `score.yaml`.

## Como funciona
Cada arquivo passado em `--patch-templates` é armazenado no projeto e avaliado como um `text/template` Go que recebe `.Manifests` e `.Workloads` e emite um array YAML/JSON de operações de patch (`op: set` ou `op: delete`, `patch` com caminho separado por pontos, `value` e `description`).

## Exemplo
```bash
score-k8s init --no-sample \
  --patch-templates ./platform-security-patches.tpl
score-k8s generate score.yaml --image ghcr.io/org/catalog-api:1.4.2 -o manifests.yaml
```

## Limites e trade-offs
Usar `--patch-templates` para sobrescrever portas ou variáveis de negócio declaradas pelo desenvolvedor no `score.yaml` cria comportamento oculto que diverge do que foi testado localmente com `score-compose`.

## Como verificar
Restrinja os templates de patch a metadados operacionais, segurança e governança de cluster, revisando os logs de descrição de cada patch aplicado durante `score-k8s generate`.

## Conexões
- [[score-dns-route-exposicao-http-roteamento-ingress]] — Veja também: Score: Exposição de Tráfego Externo com Recursos dns e route.
- [[score-fluxo-gitops-integracao-kratix-argocd-humanitec]] — Veja também: Score: Integração do Score em Fluxos GitOps, Kratix Promises e Orquestradores de Plataforma.

## Fontes
- [Score Specification GitHub — README.md (score.dev/v1b1 Workload Spec, Containers, Service Ports & Resources)](https://raw.githubusercontent.com/score-spec/score-k8s/main/README.md) — README oficial da especificação Score (score-spec/spec, Apache-2.0) detalhando o contrato declarativo score.yaml v1b1, interpolação ${resources.*} e separação entre configuração agnóstica e específica de ambiente; consultado em 2026-10-03.
- [Score Reference Implementations — score-compose & score-k8s Official READMEs](https://raw.githubusercontent.com/score-spec/spec/main/README.md) — Documentação oficial das implementações de referência score-compose e score-k8s cobrindo matriz de recursos suportados, provisionadores customizados (template:// e cmd://) e --patch-templates; consultado em 2026-10-03.
- [Score — Official GitHub Organization & Repositories](https://github.com/score-spec/score-k8s) — Repositórios oficiais do projeto Score na CNCF; consultado em 2026-10-03.
