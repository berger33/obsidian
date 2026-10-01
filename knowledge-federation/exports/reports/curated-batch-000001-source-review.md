---
report_id: curated-batch-000001-source-review
batch_id: curated-batch-000001
kind: assistant_source_consistency_check
checked_at: 2026-10-01T22:34:58Z
human_review: pending
approval: none
---

# Checagem assistida de fontes — lote curated-batch-000001

> **Este é um registro de checagem assistida por agente, não uma revisão humana nem uma aprovação do lote.** Ele compara afirmações das oito notas com a documentação citada e registra ajustes pontuais. As oito notas continuam candidatas; `valid_count`/notas válidas permanece **0** até a aprovação humana.

## Escopo e método

- Conferidas as oito notas candidatas, suas referências e as afirmações técnicas centrais.
- Preferidas fontes primárias dos respectivos padrões, projetos e fornecedores; os links abaixo permanecem nas notas e no manifesto.
- A documentação da Stripe bloqueou a leitura direta com hCaptcha. Para essa fonte, usei o trecho indexado da própria página oficial; o resultado detalha escopo comportamental, retenção e validação de parâmetros, mas a limitação de acesso direto permanece aberta para revisão humana.
- A checagem não prova que exemplos funcionem em uma implementação específica, não substitui teste de código/configuração, revisão de especialista, avaliação de segurança nem aprovação humana.

## Resultado por nota

| Nota | Resultado da comparação | Ajuste ou ressalva |
|---|---|---|
| [Contrato OpenAPI/HTTP](../../domains/software-0002/software/apis/contrato-openapi-http.md) | A especificação descreve operações HTTP e exige `operationId` único no documento; a RFC 9110 complementa a semântica HTTP. | A nota e o manifesto agora apontam para OpenAPI 3.2.1, publicada em 2026-09-10 e vigente na consulta de 2026-10-01; substitui a referência anterior a 3.2.0. A especificação não prova conformidade da implementação, como a nota já ressalta. |
| [Idempotência em APIs](../../domains/software-0002/software/backend/idempotencia-http-api.md) | A RFC define idempotência pelo efeito pretendido, não por respostas ou efeitos internos idênticos; a documentação da Stripe descreve um exemplo concreto de chave. | A explicação agora separa o comportamento específico da Stripe de regras gerais e remove a afirmação não sustentada de que toda API associa uma chave a um “escopo da conta”. A consulta da Stripe foi limitada ao índice da página oficial por hCaptcha; confirmar diretamente seus detalhes de retenção e escopo continua recomendado. |
| [Timeouts, retries, backoff e jitter](../../domains/software-0002/software/backend/timeouts-retries-backoff-jitter.md) | AWS aborda timeouts, retries, backoff e jitter; o SRE Book descreve orçamento por solicitação/cliente e recomenda evitar amplificação entre camadas. | Tornado explícito o exemplo matemático: três chamadas totais por camada em três camadas podem gerar até 27 chamadas a jusante; a tentativa inicial precisa estar incluída no orçamento. Valores e políticas do Google são exemplos, não limites universais. |
| [Migrações expand-contract](../../domains/software-0002/software/dados/migracoes-expand-contract.md) | A documentação atual do GitLab descreve mudanças graduais e remoção de schema em etapa posterior; a nota também ressalta dependência do banco e da operação. | Atualizada a rota do Migration Style Guide para a URL canônica atual. As referências são práticas documentadas pelo GitLab, não garantias universais para qualquer banco. |
| [Gates antes do merge](../../domains/software-0002/software/devops/gates-de-qualidade-no-merge.md) | A documentação do GitHub sustenta proteções de branch, aprovações e checks; a página de troubleshooting confirma a diferença entre workflow inteiro filtrado (check pendente) e job pulado por condição (sucesso). | Precisada a afirmação sobre filtros de paths/branches/mensagem e atualizado o link para a rota canônica atual da documentação. O comportamento deve ser testado na configuração real do repositório. |
| [Observabilidade distribuída](../../domains/software-0002/software/devops/observabilidade-sinais-distribuidos.md) | A documentação OpenTelemetry sustenta os conceitos de sinais/contexto, o risco de cardinalidade em métricas e o risco de dados pessoais/credenciais na telemetria. | Acrescentadas fontes específicas de cardinalidade e tratamento de dados sensíveis, além de Signals e Specification Overview. |
| [SLI, SLO e orçamento de erro](../../domains/software-0002/software/devops/sli-slo-orcamento-de-erro.md) | O SRE Workbook recomenda SLI como razão de eventos bons pelo total, define o orçamento como 100% menos o SLO e discute burn rate. | A aritmética citada na nota confere: SLO de 99,9% deixa 0,1% de eventos ruins, ou 1.000 em 1.000.000 de eventos elegíveis. A definição dos eventos e exclusões continua dependente do serviço. |
| [Contract testing consumer/provider](../../domains/software-0002/software/testes/contract-testing-consumer-provider.md) | A documentação Pact sustenta o fluxo em que o consumidor registra interações e o provedor verifica o contrato. | Nenhuma correção factual material identificada nesta leitura. A própria nota delimita que contratos cobrem interações registradas, não todo comportamento do produto. |

## Fontes primárias consultadas

- OpenAPI Initiative: [OAS 3.2.1](https://spec.openapis.org/oas/v3.2.1.html); IETF: [RFC 9110, §9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2).
- Stripe: [Idempotent requests](https://docs.stripe.com/api/idempotent_requests) — leitura direta impedida pelo hCaptcha; trecho indexado da página oficial usado com essa ressalva.
- AWS: [Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/); Google SRE: [Handling Overload](https://sre.google/sre-book/handling-overload/).
- GitLab: [Avoiding downtime in migrations](https://docs.gitlab.com/development/database/avoiding_downtime_in_migrations/); [Migration Style Guide](https://docs.gitlab.com/development/migration_style_guide/).
- GitHub Docs: [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches); [Managing a branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule); [Troubleshooting required status checks](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks).
- OpenTelemetry: [Signals](https://opentelemetry.io/docs/concepts/signals/); [Specification overview](https://opentelemetry.io/docs/specs/otel/overview/); [Metrics and cardinality limits](https://opentelemetry.io/docs/concepts/signals/metrics/); [Handling sensitive data](https://opentelemetry.io/docs/security/handling-sensitive-data/).
- Google SRE Workbook: [Example SLO document](https://sre.google/workbook/slo-document/); [Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/).
- Pact: [Introduction](https://docs.pact.io/); [Python consumer testing](https://docs.pact.io/implementation_guides/python/docs/consumer); [JavaScript overview](https://docs.pact.io/implementation_guides/javascript/readme).

## Estado do lote após a checagem

- Gate automatizado anterior: **8 candidatas**; esta checagem de fontes não altera esse resultado.
- Revisão humana: **pendente**.
- Notas aprovadas/válidas por revisão humana: **0**.
- Não contar IDs, links, arquivos de índice, MOCs, relatórios ou registros de catálogo como notas válidas.
