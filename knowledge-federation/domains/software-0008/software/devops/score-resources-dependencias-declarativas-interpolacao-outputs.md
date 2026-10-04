---
id: software.devops.tranche12.001112
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

# Score: Declaração de Recursos Dependentes e Interpolação de Outputs (${resources.*})

## Em uma frase
Na especificação Score, a seção `resources` permite ao desenvolvedor declarar dependências abstratas (`type`, `class`, `id`, `params`, `metadata`), cujos atributos resolvidos pelo ambiente são injetados nos containers via placeholders `${resources.<nome>.<atributo>}`.

## Por que importa
Hardcodar endereços de banco de dados, nomes de buckets S3 ou credenciais em arquivos de configuração da aplicação acopla o código a um ambiente específico e aumenta o risco de vazamento de segredos.

## Como funciona
O desenvolvedor declara apenas o que precisa (por exemplo, `db: { type: postgres }` e `cache: { type: redis }`) e referencia `${resources.db.host}`, `${resources.db.port}` ou `${resources.cache.password}` em `containers.*.variables` ou `containers.*.files`. Cabe ao provisionador da implementação Score no ambiente alvo instanciar ou vincular o recurso real e fornecer os outputs correspondentes.

## Exemplo
```yaml
apiVersion: score.dev/v1b1
metadata:
  name: payment-worker
containers:
  worker:
    image: ghcr.io/org/payment-worker:2.1.0
    variables:
      REDIS_ADDR: "${resources.cache.host}:${resources.cache.port}"
      S3_BUCKET: "${resources.receipts.bucket}"
resources:
  cache:
    type: redis
    class: ha
  receipts:
    type: s3
```

## Limites e trade-offs
Referenciar um atributo de output (como `${resources.db.connection_uri}`) que não faz parte do contrato padrão do provisionador para aquele `type` causa falha de resolução durante o comando `generate`.

## Como verificar
Consulte a tabela de outputs suportados pelo provisionador (`host`, `port`, `name`, `username`, `password`) e valide a resolução completa dos placeholders na saída gerada.

## Conexões
- [[score-especificacao-workload-platform-agnostic-score-yaml]] — Veja também: Score: Especificação de Workload Agnóstica de Plataforma (score.yaml v1b1).
- [[score-compose-desenvolvimento-local-docker-compose-generation]] — Veja também: Score: score-compose para Geração de Ambientes Locais Docker Compose.

## Fontes
- [Score Specification GitHub — README.md (score.dev/v1b1 Workload Spec, Containers, Service Ports & Resources)](https://raw.githubusercontent.com/score-spec/spec/main/README.md) — README oficial da especificação Score (score-spec/spec, Apache-2.0) detalhando o contrato declarativo score.yaml v1b1, interpolação ${resources.*} e separação entre configuração agnóstica e específica de ambiente; consultado em 2026-10-03.
- [Score Reference Implementations — score-compose & score-k8s Official READMEs](https://raw.githubusercontent.com/score-spec/score-compose/main/README.md) — Documentação oficial das implementações de referência score-compose e score-k8s cobrindo matriz de recursos suportados, provisionadores customizados (template:// e cmd://) e --patch-templates; consultado em 2026-10-03.
- [Score — Official GitHub Organization & Repositories](https://raw.githubusercontent.com/score-spec/score-k8s/main/README.md) — Repositórios oficiais do projeto Score na CNCF; consultado em 2026-10-03.
