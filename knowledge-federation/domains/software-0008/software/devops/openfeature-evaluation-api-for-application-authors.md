---
id: software.devops.tranche05.000493
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md"
fontes: ["https://openfeature.dev/docs/reference/intro/", "https://raw.githubusercontent.com/open-feature/spec/main/README.md", "https://github.com/open-feature/spec"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# A abstração Evaluation API do OpenFeature para autores de aplicação

## Em uma frase
Conforme detalha a arquitetura oficial em `openfeature.dev/docs/reference/intro/`, a **Evaluation API** (`openfeature.dev/docs/reference/concepts/evaluation-api`) é a parte do SDK do OpenFeature com a qual o **autor da aplicação (application author)** interage diretamente no dia a dia. Ela permite avaliar feature flags tipadas (booleanas, strings, números inteiros/ponto flutuante e objetos estruturados) fornecendo a chave da flag, um valor padrão obrigatório de fallback e um contexto opcional, usando os valores resolvidos para controlar o fluxo da aplicação ou características do serviço.

## Por que importa
Ao exigir sempre um **valor padrão (default value)** na assinatura dos métodos da Evaluation API e oferecer métodos que retornam detalhes completos da avaliação (`evaluation details`, incluindo razão da decisão, variante e eventuais códigos de erro como `"PARSE_ERROR"`), a API garante que uma falha no serviço externo de flags nunca derrube a aplicação com uma exceção não tratada.

## Como funciona
Nas chamadas da Evaluation API dentro das regras de negócio, escolha sempre um valor padrão (`defaultValue`) seguro e conservador — tipicamente mantendo o comportamento legado comprovado caso o provedor de flags esteja inacessível.

## Exemplo
Ao avaliar `client.getBooleanValue("novo-checkout-pix", false, ctx)`, se o provedor de flags estiver indisponível ou a flag não existir, a Evaluation API retorna com segurança o fallback `false` e registra o motivo nos metadados de `evaluation details`.

## Limites e trade-offs
Evite usar apenas flags booleanas quando a configuração exigir parâmetros ajustáveis (como limites de paginação, algoritmos de recomendação ou timeouts); aproveite os métodos de string, número e objeto estruturado da Evaluation API.

## Como verificar
Invoque o método de avaliação detalhada (`getBooleanDetails` / `evaluation details`) no SDK do OpenFeature e verifique os campos de valor resolvido, `variant` e `reason`.

## Conexões
- [[openfeature-dynamic-context-aware-runtime-feature-flags]] — Veja também: Casos de uso de feature flags dinâmicas e sensíveis ao contexto em tempo de execução.
- [[openfeature-evaluation-context-static-and-dynamic-merging]] — Veja também: Gerenciamento de dados estáticos e dinâmicos com Evaluation Context no OpenFeature.

## Fontes
- [OpenFeature Official Documentation — Introduction & Core Concepts (Evaluation API, Context, Providers, Hooks & Events)](https://openfeature.dev/docs/reference/intro/) — Documentação oficial de introdução do OpenFeature detalhando o papel de feature flags dinâmicas e sensíveis ao contexto, arquitetura padronizada de SDK e as cinco abstrações fundamentais: Evaluation API, Evaluation Context, Providers, Hooks e Events.; consultado em 2026-10-03.
- [OpenFeature Specification GitHub — README.md (Design Principles, SDK Role, RFC 2119 & W3C QA Guidelines)](https://raw.githubusercontent.com/open-feature/spec/main/README.md) — README oficial do repositório da especificação OpenFeature (projeto CNCF) descrevendo os seis princípios de design, o papel do SDK como interface agnóstica sem lógica própria de avaliação, conformidade com RFC 2119 e W3C QA Framework Guidelines e geração de requisitos JSON via make.; consultado em 2026-10-03.
- [OpenFeature Specification — Official GitHub Repository](https://github.com/open-feature/spec) — Repositório oficial da especificação OpenFeature na CNCF.; consultado em 2026-10-03.
