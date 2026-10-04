---
id: software.devops.tranche05.000494
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

# Gerenciamento de dados estáticos e dinâmicos com Evaluation Context no OpenFeature

## Em uma frase
A segunda abstração fundamental documentada em `openfeature.dev/docs/reference/intro/` é o **Evaluation Context** (`openfeature.dev/docs/reference/concepts/evaluation-context`): um contêiner para dados contextuais arbitrários que servem de base para a avaliação dinâmica e segmentada (targeting) das feature flags. O OpenFeature permite configurar **dados estáticos globalmente** (como o nome do host, região do cluster ou identificador da aplicação) e combinar esses dados com **contexto de avaliação dinâmico** (como o `targetingKey`/ID do usuário logado, plano de assinatura ou endereço IP do cliente em uma requisição web), que pode ser propagado implicitamente no escopo da requisição ou passado explicitamente no momento da avaliação da flag, sendo mesclado (*merged*) com os valores estáticos.

## Por que importa
Separar atributos globais estáticos do ambiente (configurados uma única vez na inicialização do processo) dos atributos dinâmicos por requisição evita que o desenvolvedor precise repetir metadados de infraestrutura em cada chamada de flag espalhada pelo código.

## Como funciona
Configure os atributos de ambiente (`environment`, `region`, `service_version`) no Evaluation Context global/de cliente na inicialização e injete o `targetingKey` (identificador determinístico do usuário/sessão) e atributos do usuário via middleware HTTP/gRPC no contexto da requisição.

## Exemplo
Para realizar um rollout canário consistente para 10% dos usuários (onde o mesmo usuário sempre cai no mesmo bucket), o middleware web popula o `Evaluation Context` com o ID hash do usuário como `targetingKey` e o código da rota apenas chama a Evaluation API.

## Limites e trade-offs
Nunca coloque dados sensíveis desnecessários (como senhas, números de cartão ou PII bruta não anonimizada) dentro do `Evaluation Context` se o seu `Provider` enviar esse contexto pela rede para um serviço SaaS externo; utilize identificadores opacos ou hashes como `targetingKey`.

## Como verificar
Configure um atributo no contexto global e um atributo no contexto da chamada, avalie uma regra de segmentação que dependa de ambos e confirme que a fusão (*merge*) do contexto produziu a decisão esperada.

## Conexões
- [[openfeature-evaluation-api-for-application-authors]] — Veja também: A abstração Evaluation API do OpenFeature para autores de aplicação.
- [[openfeature-providers-translation-layer-architecture]] — Veja também: Arquitetura de Providers como camada de tradução no OpenFeature.

## Fontes
- [OpenFeature Official Documentation — Introduction & Core Concepts (Evaluation API, Context, Providers, Hooks & Events)](https://openfeature.dev/docs/reference/intro/) — Documentação oficial de introdução do OpenFeature detalhando o papel de feature flags dinâmicas e sensíveis ao contexto, arquitetura padronizada de SDK e as cinco abstrações fundamentais: Evaluation API, Evaluation Context, Providers, Hooks e Events.; consultado em 2026-10-03.
- [OpenFeature Specification GitHub — README.md (Design Principles, SDK Role, RFC 2119 & W3C QA Guidelines)](https://raw.githubusercontent.com/open-feature/spec/main/README.md) — README oficial do repositório da especificação OpenFeature (projeto CNCF) descrevendo os seis princípios de design, o papel do SDK como interface agnóstica sem lógica própria de avaliação, conformidade com RFC 2119 e W3C QA Framework Guidelines e geração de requisitos JSON via make.; consultado em 2026-10-03.
- [OpenFeature Specification — Official GitHub Repository](https://github.com/open-feature/spec) — Repositório oficial da especificação OpenFeature na CNCF.; consultado em 2026-10-03.
