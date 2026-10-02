---
id: software.testes.tranche09.000335
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
fontes: ["https://docs.gitlab.com/ci/caching/", "https://docs.gitlab.com/ci/jobs/job_artifacts/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GitLab CI: não usar cache como evidência de build

## Em uma frase
Cache acelera reutilização de dependências e artifacts transportam saídas identificáveis entre jobs; os objetivos não são equivalentes.

## Por que importa
O pipeline GitLab seleciona jobs segundo source, regras e dependências; validar somente o YAML não comprova a execução esperada em cada evento. Cache pode ser ausente, atualizado ou compartilhado por chaves concorrentes e não é garantia de output confiável.

## Como funciona
Teste combinações representativas de push, merge request e downstream, e verifique artifacts, segredos e exclusão mútua no contexto real. Reconstrua arquivo que outro job precisa como artifact e reserve cache a dados regeneráveis com chave deliberada.

## Exemplo
Pipeline consome artifact versionado da aplicação e usa cache de pacotes como otimização sem depender de seu conteúdo para correção.

## Limites e trade-offs
Comportamento depende de versão, settings do projeto, permissões e configurações incluídas; simulação local não reproduz todos os eventos do GitLab. Cache pode melhorar tempo, mas chave errada ou conteúdo envenenado exige controles adicionais.

## Como verificar
Rode job com cache vazio e confira que resultado funcional permanece igual e artifact veio do produtor da execução atual.

## Conexões
- [[gitlab-needs-artifacts-explicit-dependency]] — Veja também: GitLab CI: verificar que jobs recebem artifacts necessários.
- [[gitlab-resource-group-serialize-deploy]] — Veja também: GitLab CI: serializar deploys com resource_group.

## Fontes
- [GitLab CI — Caching](https://docs.gitlab.com/ci/caching/) — cache reutilizável, chaves e distinção de artifacts; consultado em 2026-10-02.
- [GitLab CI — Job artifacts](https://docs.gitlab.com/ci/jobs/job_artifacts/) — persistência e passagem explícita de artifacts; consultado em 2026-10-02.
