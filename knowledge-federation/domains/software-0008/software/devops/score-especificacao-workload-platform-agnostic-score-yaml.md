---
id: software.devops.tranche12.001111
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
fontes: ["https://raw.githubusercontent.com/score-spec/spec/main/README.md", "https://raw.githubusercontent.com/score-spec/score-compose/main/README.md", "https://raw.githubusercontent.com/score-spec/score-k8s/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Score: Especificação de Workload Agnóstica de Plataforma (score.yaml v1b1)

## Em uma frase
Score é uma especificação open-source de workload (CNCF Sandbox, `apiVersion: score.dev/v1b1`) centrada no desenvolvedor que descreve em um único arquivo `score.yaml` os containers, portas de serviço e dependências de recursos exigidos por uma aplicação, de forma independente da plataforma de execução.

## Por que importa
Quando desenvolvedores usam Docker Compose localmente e Kubernetes ou Helm em ambientes remotos, manter duas ou mais árvores de configuração em sincronia gera deriva de variáveis de ambiente, portas divergentes e alta sobrecarga cognitiva.

## Como funciona
O arquivo `score.yaml` é versionado junto ao código-fonte da aplicação e declara `metadata.name`, `containers` (imagem, variáveis interpoladas, arquivos, volumes, probes e limites), `service.ports` e `resources` (como `postgres`, `redis`, `dns`, `route`, `s3`). Implementações de referência como `score-compose` e `score-k8s` traduzem esse mesmo contrato para a plataforma alvo.

## Exemplo
```yaml
apiVersion: score.dev/v1b1
metadata:
  name: catalog-api
containers:
  web:
    image: ghcr.io/org/catalog-api:1.4.0
    variables:
      DATABASE_URL: "postgresql://${resources.db.username}:${resources.db.password}@${resources.db.host}:${resources.db.port}/${resources.db.name}"
service:
  ports:
    http:
      port: 8080
resources:
  db:
    type: postgres
```

## Limites e trade-offs
Tentar embutir construções específicas de um único orquestrador (como anotações proprietárias de Ingress Controller ou afinidades de nó do Kubernetes) diretamente no `score.yaml` viola a portabilidade entre ambientes locais e remotos.

## Como verificar
Valide o `score.yaml` contra o schema `score.dev/v1b1` testando a geração simultânea com `score-compose generate` e `score-k8s generate` no pipeline de CI.

## Conexões
- [[score-resources-dependencias-declarativas-interpolacao-outputs]] — Veja também: Score: Declaração de Recursos Dependentes e Interpolação de Outputs (${resources.*}).

## Fontes
- [Score Specification GitHub — README.md (score.dev/v1b1 Workload Spec, Containers, Service Ports & Resources)](https://raw.githubusercontent.com/score-spec/spec/main/README.md) — README oficial da especificação Score (score-spec/spec, Apache-2.0) detalhando o contrato declarativo score.yaml v1b1, interpolação ${resources.*} e separação entre configuração agnóstica e específica de ambiente; consultado em 2026-10-03.
- [Score Reference Implementations — score-compose & score-k8s Official READMEs](https://raw.githubusercontent.com/score-spec/score-compose/main/README.md) — Documentação oficial das implementações de referência score-compose e score-k8s cobrindo matriz de recursos suportados, provisionadores customizados (template:// e cmd://) e --patch-templates; consultado em 2026-10-03.
- [Score — Official GitHub Organization & Repositories](https://raw.githubusercontent.com/score-spec/score-k8s/main/README.md) — Repositórios oficiais do projeto Score na CNCF; consultado em 2026-10-03.
