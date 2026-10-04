---
id: software.testes.tranche09.000332
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://docs.gitlab.com/ci/pipelines/downstream_pipelines/", "https://docs.gitlab.com/ci/jobs/job_rules/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GitLab CI: reconhecer CI_PIPELINE_SOURCE em child pipeline

## Em uma frase
Jobs dentro de child pipeline têm CI_PIPELINE_SOURCE parent_pipeline, diferentemente do evento que iniciou pipeline pai.

## Por que importa
O pipeline GitLab seleciona jobs segundo source, regras e dependências; validar somente o YAML não comprova a execução esperada em cada evento. Reutilizar regra de merge_request_event dentro do filho pode impedir os jobs downstream de executar.

## Como funciona
Teste combinações representativas de push, merge request e downstream, e verifique artifacts, segredos e exclusão mútua no contexto real. Passe contexto necessário do pai e escreva regras do child para a origem parent_pipeline esperada.

## Exemplo
Parent pipeline iniciado por MR dispara child pipeline; teste confirma que job de validação do filho roda sob parent_pipeline.

## Limites e trade-offs
Comportamento depende de versão, settings do projeto, permissões e configurações incluídas; simulação local não reproduz todos os eventos do GitLab. O child não herda todas as condições como string de source; variáveis e dependências precisam ser avaliadas explicitamente.

## Como verificar
Inspecione source e variáveis nos dois níveis e valide caminho positivo e um evento que deve ser ignorado.

## Conexões
- [[gitlab-merge-request-rules-main-config]] — Veja também: GitLab CI: garantir que configuração principal habilita MR pipeline.
- [[gitlab-trigger-strategy-propagate-result]] — Veja também: GitLab CI: propagar resultado do downstream ao pipeline pai.

## Fontes
- [GitLab CI — Downstream pipelines](https://docs.gitlab.com/ci/pipelines/downstream_pipelines/) — parent-child pipelines e CI_PIPELINE_SOURCE; consultado em 2026-10-02.
- [GitLab CI — Job rules](https://docs.gitlab.com/ci/jobs/job_rules/) — avaliação de rules e prevenção de pipelines duplicados; consultado em 2026-10-02.
