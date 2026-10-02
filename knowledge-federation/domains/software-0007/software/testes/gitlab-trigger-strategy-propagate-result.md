---
id: software.testes.tranche09.000333
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
fontes: ["https://docs.gitlab.com/ci/pipelines/downstream_pipelines/", "https://docs.gitlab.com/ci/yaml/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GitLab CI: propagar resultado do downstream ao pipeline pai

## Em uma frase
Jobs trigger e configuração de strategy determinam quando o job do pai reflete status do pipeline downstream.

## Por que importa
O pipeline GitLab seleciona jobs segundo source, regras e dependências; validar somente o YAML não comprova a execução esperada em cada evento. Pai pode aparentar sucesso antes que teste obrigatório do filho termine se a dependência não aguarda resultado.

## Como funciona
Teste combinações representativas de push, merge request e downstream, e verifique artifacts, segredos e exclusão mútua no contexto real. Escolha estratégia de trigger suportada pela versão e confirme que status do pai acompanha falha do downstream.

## Exemplo
Job de deploy depende de child pipeline; um teste falho no filho mantém etapa pai bloqueada ou falha conforme política adotada.

## Limites e trade-offs
Comportamento depende de versão, settings do projeto, permissões e configurações incluídas; simulação local não reproduz todos os eventos do GitLab. Sem estratégia apropriada, pai e filho podem ter lifecycles e statuses não intuitivos.

## Como verificar
Provoque sucesso e falha no child e observe status e ordem de conclusão no pipeline pai.

## Conexões
- [[gitlab-child-pipeline-source-parent-pipeline]] — Veja também: GitLab CI: reconhecer CI_PIPELINE_SOURCE em child pipeline.
- [[gitlab-needs-artifacts-explicit-dependency]] — Veja também: GitLab CI: verificar que jobs recebem artifacts necessários.

## Fontes
- [GitLab CI — Downstream pipelines](https://docs.gitlab.com/ci/pipelines/downstream_pipelines/) — parent-child pipelines e CI_PIPELINE_SOURCE; consultado em 2026-10-02.
- [GitLab CI — YAML syntax reference](https://docs.gitlab.com/ci/yaml/) — semântica de jobs, needs, artifacts e keywords; consultado em 2026-10-02.
