---
id: software.testes.tranche09.000331
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
fontes: ["https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/", "https://docs.gitlab.com/ci/jobs/job_rules/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GitLab CI: garantir que configuração principal habilita MR pipeline

## Em uma frase
Merge request pipeline exige regras compatíveis na configuração principal do projeto; uma regra isolada dentro de job incluído pode não bastar.

## Por que importa
O pipeline GitLab seleciona jobs segundo source, regras e dependências; validar somente o YAML não comprova a execução esperada em cada evento. Uma alteração em include pode parecer habilitar teste de MR sem que o evento realmente crie aquele pipeline.

## Como funciona
Teste combinações representativas de push, merge request e downstream, e verifique artifacts, segredos e exclusão mútua no contexto real. Teste evento de merge request e inspecione workflow e regras de jobs na configuração efetivamente composta.

## Exemplo
Uma configuração principal inclui template de teste, mas ainda declara regra que aceita merge_request_event para iniciar pipeline.

## Limites e trade-offs
Comportamento depende de versão, settings do projeto, permissões e configurações incluídas; simulação local não reproduz todos os eventos do GitLab. Forks, protected branches e settings do projeto podem mudar variáveis disponíveis e permissões.

## Como verificar
Crie MR em projeto de teste e confirme source, jobs selecionados e ausência de secrets que não devem ser expostos.

## Conexões
- [[gitlab-rules-avoid-duplicate-pipelines]] — Veja também: GitLab CI: testar rules para evitar pipelines duplicados.
- [[gitlab-child-pipeline-source-parent-pipeline]] — Veja também: GitLab CI: reconhecer CI_PIPELINE_SOURCE em child pipeline.

## Fontes
- [GitLab CI — Merge request pipelines](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/) — condições e configuração de merge request pipelines; consultado em 2026-10-02.
- [GitLab CI — Job rules](https://docs.gitlab.com/ci/jobs/job_rules/) — avaliação de rules e prevenção de pipelines duplicados; consultado em 2026-10-02.
