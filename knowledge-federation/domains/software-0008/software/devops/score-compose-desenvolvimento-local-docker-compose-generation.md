---
id: software.devops.tranche12.001113
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
fontes: ["https://raw.githubusercontent.com/score-spec/score-compose/main/README.md", "https://raw.githubusercontent.com/score-spec/spec/main/README.md", "https://github.com/score-spec/score-compose"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Score: score-compose para Geração de Ambientes Locais Docker Compose

## Em uma frase
O `score-compose` é a implementação de referência da especificação Score para Docker Compose, convertendo um ou mais arquivos `score.yaml` em um `compose.yaml` completo com containers de aplicação e serviços anexados provisionados automaticamente para desenvolvimento local.

## Por que importa
Configurar manualmente containers de Postgres, Redis, MinIO, RabbitMQ e redes compartilhadas no Docker Compose para cada microsserviço consome tempo e frequentemente diverge das variáveis de ambiente que a aplicação receberá no Kubernetes.

## Como funciona
O fluxo utiliza `score-compose init` para criar o diretório de estado `.score-compose/` com os provisionadores padrão e `score-compose generate score.yaml` para resolver os recursos e produzir o `compose.yaml` pronto para `docker compose up`. Ele suporta nativamente provisionadores locais para `postgres`, `mysql`, `redis`, `mongodb`, `amqp`, `kafka-topic`, `s3`, `elasticsearch`, `dns` e `route`.

## Exemplo
```bash
score-compose init --no-sample
score-compose generate score.yaml --output compose.yaml
docker compose -f compose.yaml config
docker compose -f compose.yaml up -d
```

## Limites e trade-offs
Commitar o diretório `.score-compose/` no controle de versão público expõe o arquivo `state.yaml` local, que pode conter senhas geradas automaticamente e caminhos absolutos da máquina do desenvolvedor.

## Como verificar
Adicione `.score-compose/` ao `.gitignore` e verifique com `docker compose config` se todos os serviços e variáveis de ambiente foram renderizados corretamente.

## Conexões
- [[score-resources-dependencias-declarativas-interpolacao-outputs]] — Veja também: Score: Declaração de Recursos Dependentes e Interpolação de Outputs (${resources.*}).
- [[score-k8s-geracao-manifestos-kubernetes-init-generate]] — Veja também: Score: score-k8s para Tradução de Workloads em Manifestos Kubernetes.

## Fontes
- [Score Specification GitHub — README.md (score.dev/v1b1 Workload Spec, Containers, Service Ports & Resources)](https://raw.githubusercontent.com/score-spec/score-compose/main/README.md) — README oficial da especificação Score (score-spec/spec, Apache-2.0) detalhando o contrato declarativo score.yaml v1b1, interpolação ${resources.*} e separação entre configuração agnóstica e específica de ambiente; consultado em 2026-10-03.
- [Score Reference Implementations — score-compose & score-k8s Official READMEs](https://raw.githubusercontent.com/score-spec/spec/main/README.md) — Documentação oficial das implementações de referência score-compose e score-k8s cobrindo matriz de recursos suportados, provisionadores customizados (template:// e cmd://) e --patch-templates; consultado em 2026-10-03.
- [Score — Official GitHub Organization & Repositories](https://github.com/score-spec/score-compose) — Repositórios oficiais do projeto Score na CNCF; consultado em 2026-10-03.
