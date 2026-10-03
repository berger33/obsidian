---
id: software.devops.tranche12.001115
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
fontes: ["https://raw.githubusercontent.com/score-spec/score-k8s/main/README.md", "https://raw.githubusercontent.com/score-spec/score-compose/main/README.md", "https://raw.githubusercontent.com/score-spec/spec/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Score: Provisionadores Customizados (template:// e cmd://) em score-compose e score-k8s

## Em uma frase
Tanto `score-compose` quanto `score-k8s` utilizam um sistema extensível de provisionadores em arquivos `*.provisioners.yaml` que mapeiam recursos declarados (`type`, `class`, `id`) para geradores baseados em templates Go (`template://`) ou execução de comandos externos (`cmd://`).

## Por que importa
Em clusters de produção, um recurso `type: postgres` não deve criar um Pod estático de brinquedo, mas sim emitir uma CRD do CloudNativePG, Crossplane ou Kratix Promise aprovada pela equipe de plataforma.

## Como funciona
Os provisionadores são carregados em ordem de precedência com política first-match. Equipes de plataforma distribuem arquivos de provisionadores corporativos importados via `score-k8s init --provisioners <uri>`. Quando o workload pede `type: postgres` com `class: prod`, o provisionador customizado gera a CRD do operador do cluster e devolve os outputs (`host`, `port`, referências de `Secret`) para interpolação no Deployment.

## Exemplo
```bash
score-k8s init --no-sample \
  --provisioners https://raw.githubusercontent.com/org/platform-provisioners/main/cnpg-postgres.provisioners.yaml
score-k8s provisioners list
score-k8s generate score.yaml -o manifests.yaml
```

## Limites e trade-offs
Escrever um provisionador customizado que retorna nomes de campos de output diferentes do provisionador default (por exemplo, `db_host` em vez de `host`) quebra a portabilidade do `score.yaml` entre `score-compose` e `score-k8s`.

## Como verificar
Mantenha os mesmos nomes de outputs (`host`, `port`, `name`, `username`, `password`) entre os provisionadores locais e os de produção, verificando a lista ativa com `score-k8s provisioners list`.

## Conexões
- [[score-k8s-geracao-manifestos-kubernetes-init-generate]] — Veja também: Score: score-k8s para Tradução de Workloads em Manifestos Kubernetes.
- [[score-containers-files-volumes-variables-probes-limits]] — Veja também: Score: Configuração de Containers (Variables, Files, Volumes, Probes e Resources).

## Fontes
- [Score Specification GitHub — README.md (score.dev/v1b1 Workload Spec, Containers, Service Ports & Resources)](https://raw.githubusercontent.com/score-spec/score-k8s/main/README.md) — README oficial da especificação Score (score-spec/spec, Apache-2.0) detalhando o contrato declarativo score.yaml v1b1, interpolação ${resources.*} e separação entre configuração agnóstica e específica de ambiente; consultado em 2026-10-03.
- [Score Reference Implementations — score-compose & score-k8s Official READMEs](https://raw.githubusercontent.com/score-spec/score-compose/main/README.md) — Documentação oficial das implementações de referência score-compose e score-k8s cobrindo matriz de recursos suportados, provisionadores customizados (template:// e cmd://) e --patch-templates; consultado em 2026-10-03.
- [Score — Official GitHub Organization & Repositories](https://raw.githubusercontent.com/score-spec/spec/main/README.md) — Repositórios oficiais do projeto Score na CNCF; consultado em 2026-10-03.
