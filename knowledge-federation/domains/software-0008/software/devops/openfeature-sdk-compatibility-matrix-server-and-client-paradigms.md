---
id: software.devops.tranche05.000499
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

# Matriz de compatibilidade de SDKs e distinção entre paradigmas Server-side e Client-side no OpenFeature

## Em uma frase
O repositório `open-feature/spec` referencia a visão geral atualizada de compatibilidade de SDKs em **`openfeature.dev/docs/reference/sdks/sdk-compatibility`** e suporta requisitos condicionais na especificação para diferentes paradigmas de execução. Na especificação e nos SDKs do OpenFeature, distingue-se o paradigma **Multi-context / Server-side** (onde um único processo de backend atende milhares de usuários diferentes simultaneamente e o `Evaluation Context` muda a cada requisição avaliada) do paradigma **Single-context / Client-side** (aplicações web browser, mobile iOS/Android ou desktop, onde a instância do aplicativo roda para um único usuário por vez e o contexto é atualizado quando o estado do usuário muda, pré-buscando as flags avaliadas para aquele contexto).

## Por que importa
Usar um modelo de avaliação puramente server-side em um aplicativo mobile ou SPA no navegador exporia todas as regras de segmentação confidenciais ao cliente ou exigiria um round-trip de rede lento para cada `if` renderizado na tela. A separação clara entre SDKs Server-side e Client-side no OpenFeature resolve essa diferença de arquitetura mantendo os mesmos conceitos centrais.

## Como funciona
Utilize os SDKs **Server-side** do OpenFeature nos microsserviços de backend (passando o `Evaluation Context` por requisição) e os SDKs **Client-side** (Web, React, Android, iOS) nos aplicativos de interface do usuário (atualizando o contexto na autenticação e lendo as flags pré-avaliadas em memória).

## Exemplo
Em uma aplicação web moderna, o backend em Go usa o SDK Server-side do OpenFeature para avaliar flags por requisição, enquanto o frontend React usa o SDK Client-side do OpenFeature sincronizado com o mesmo provedor, reagindo instantaneamente via `Events` sem bloquear a renderização da UI.

## Limites e trade-offs
Consulte `openfeature.dev/docs/reference/sdks/sdk-compatibility` antes de iniciar um projeto em uma nova stack tecnológica para confirmar a versão da especificação e os recursos (Hooks, Events, Context Propagation) já homologados naquele SDK específico.

## Como verificar
Verifique na documentação do SDK escolhido se ele implementa o perfil Server-side ou Client-side da especificação OpenFeature e valide o fluxo de atualização de contexto correspondente.

## Conexões
- [[openfeature-rfc2119-and-w3c-qa-framework-specification-tooling]] — Veja também: Conformidade da especificação OpenFeature com RFC 2119, W3C QA Guidelines e parser automatizado via make.
- [[openfeature-progressive-delivery-and-safe-degradation-in-devops]] — Veja também: Entrega progressiva (Progressive Delivery), kill switches e governança de feature flags em DevOps.

## Fontes
- [OpenFeature Official Documentation — Introduction & Core Concepts (Evaluation API, Context, Providers, Hooks & Events)](https://openfeature.dev/docs/reference/intro/) — Documentação oficial de introdução do OpenFeature detalhando o papel de feature flags dinâmicas e sensíveis ao contexto, arquitetura padronizada de SDK e as cinco abstrações fundamentais: Evaluation API, Evaluation Context, Providers, Hooks e Events.; consultado em 2026-10-03.
- [OpenFeature Specification GitHub — README.md (Design Principles, SDK Role, RFC 2119 & W3C QA Guidelines)](https://raw.githubusercontent.com/open-feature/spec/main/README.md) — README oficial do repositório da especificação OpenFeature (projeto CNCF) descrevendo os seis princípios de design, o papel do SDK como interface agnóstica sem lógica própria de avaliação, conformidade com RFC 2119 e W3C QA Framework Guidelines e geração de requisitos JSON via make.; consultado em 2026-10-03.
- [OpenFeature Specification — Official GitHub Repository](https://github.com/open-feature/spec) — Repositório oficial da especificação OpenFeature na CNCF.; consultado em 2026-10-03.
