---
id: software.testes.tranche09.000334
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
fontes: ["https://docs.gitlab.com/ci/jobs/job_artifacts/", "https://docs.gitlab.com/ci/yaml/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GitLab CI: verificar que jobs recebem artifacts necessários

## Em uma frase
Artifacts são arquivos produzidos por jobs e disponibilizados por dependências de pipeline conforme configuração do job consumidor.

## Por que importa
O pipeline GitLab seleciona jobs segundo source, regras e dependências; validar somente o YAML não comprova a execução esperada em cada evento. Uma relação `needs` incompleta ou artifact expirado pode fazer teste consumir arquivo antigo ou inexistente.

## Como funciona
Teste combinações representativas de push, merge request e downstream, e verifique artifacts, segredos e exclusão mútua no contexto real. Declare jobs produtores necessários e artifacts requeridos; valide caminho, nome e conteúdo no job consumidor.

## Exemplo
Teste baixa pacote de build do job selecionado por needs e verifica digest antes de rodar suite de integração.

## Limites e trade-offs
Comportamento depende de versão, settings do projeto, permissões e configurações incluídas; simulação local não reproduz todos os eventos do GitLab. Artifacts têm política de expiração e não devem ser usados como cache genérico permanente.

## Como verificar
Force produtor ausente e artifact inválido e confirme falha explícita sem fallback silencioso para arquivo de workspace.

## Conexões
- [[gitlab-trigger-strategy-propagate-result]] — Veja também: GitLab CI: propagar resultado do downstream ao pipeline pai.
- [[gitlab-cache-not-artifact]] — Veja também: GitLab CI: não usar cache como evidência de build.

## Fontes
- [GitLab CI — Job artifacts](https://docs.gitlab.com/ci/jobs/job_artifacts/) — persistência e passagem explícita de artifacts; consultado em 2026-10-02.
- [GitLab CI — YAML syntax reference](https://docs.gitlab.com/ci/yaml/) — semântica de jobs, needs, artifacts e keywords; consultado em 2026-10-02.
