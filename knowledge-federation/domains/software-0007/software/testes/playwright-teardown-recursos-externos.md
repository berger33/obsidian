---
id: software.testes.tranche08.000153
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://playwright.dev/docs/test-fixtures", "https://playwright.dev/docs/api-testing"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Playwright: teardown confiável de recursos externos

## Em uma frase
Registre a limpeza do recurso no mesmo caminho de setup para que falhas de assertion não deixem dados residuais.

## Por que importa
Vazamentos de contas, arquivos e registros fazem execuções posteriores dependerem da ordem e elevam custo em ambientes compartilhados.

## Como funciona
Crie recurso com nome único, guarde a referência retornada e execute a remoção em teardown com timeout e diagnóstico próprios. Se remoção falhar, preserve evidência suficiente sem mascarar a falha original.

## Exemplo
Depois de criar um projeto pela API, a fixture devolve o identificador; o teardown tenta removê-lo mesmo que a navegação ou a verificação de UI falhe.

## Limites e trade-offs
Limpeza best-effort pode falhar quando o serviço está indisponível. Não apague por prefixo amplo nem use cleanup que possa remover dados de outros jobs.

## Como verificar
Force falha no meio do teste, confira o recurso no backend e examine se o teardown ocorreu. Execute duas vezes e garanta que a segunda execução não herda estado.

## Conexões
- [[playwright-fixture-ciclo-vida-isolamento]] — Veja também: Playwright: ciclo de vida de fixtures por teste.
- [[terraform-test-run-apply-cleanup]] — Veja também: Terraform: isolar testes que aplicam infraestrutura.

## Fontes
- [Playwright — Fixtures](https://playwright.dev/docs/test-fixtures) — isolamento, ciclo de vida e composição de fixtures; consultado em 2026-10-02.
- [Playwright — API testing](https://playwright.dev/docs/api-testing) — uso do APIRequestContext para testar APIs; consultado em 2026-10-02.
