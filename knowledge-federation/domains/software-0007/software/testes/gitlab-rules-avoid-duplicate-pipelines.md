---
id: software.testes.tranche09.000330
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
fontes: ["https://docs.gitlab.com/ci/jobs/job_rules/", "https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GitLab CI: testar rules para evitar pipelines duplicados

## Em uma frase
job rules avaliam condições na ordem declarada e workflow rules selecionam tipos de pipeline; configurações sobrepostas podem duplicar branch e merge request.

## Por que importa
O pipeline GitLab seleciona jobs segundo source, regras e dependências; validar somente o YAML não comprova a execução esperada em cada evento. Duplicação consome runner e pode publicar efeitos repetidos, principalmente quando jobs de deploy não verificam contexto.

## Como funciona
Teste combinações representativas de push, merge request e downstream, e verifique artifacts, segredos e exclusão mútua no contexto real. Defina workflow:rules para tipos de pipeline e job rules para seleção de jobs, cobrindo push, merge request e outras origens.

## Exemplo
Matriz de teste avalia push, merge request, schedule e tag, confirmando quais pipelines e jobs surgem em cada cenário.

## Limites e trade-offs
Comportamento depende de versão, settings do projeto, permissões e configurações incluídas; simulação local não reproduz todos os eventos do GitLab. Regras em includes e settings de workflow também influenciam o resultado final.

## Como verificar
Use pipeline editor/CI lint quando aplicável e compare pipeline criado com tabela de eventos e jobs esperados.

## Conexões
- [[gitlab-merge-request-rules-main-config]] — Veja também: GitLab CI: garantir que configuração principal habilita MR pipeline.

## Fontes
- [GitLab CI — Job rules](https://docs.gitlab.com/ci/jobs/job_rules/) — avaliação de rules e prevenção de pipelines duplicados; consultado em 2026-10-02.
- [GitLab CI — Merge request pipelines](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/) — condições e configuração de merge request pipelines; consultado em 2026-10-02.
