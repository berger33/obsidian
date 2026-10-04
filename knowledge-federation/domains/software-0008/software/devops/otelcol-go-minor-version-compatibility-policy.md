---
id: software.devops.tranche01.000004
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/README.md", "https://github.com/open-telemetry/opentelemetry-collector"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Política de suporte a versões menores do Go (N e N-1, remoção de N-2) quando usado como biblioteca

## Em uma frase
A seção Compatibility do README explica que, quando usado como biblioteca Go, o OpenTelemetry Collector acompanha as versões menores suportadas pela equipe do Go com uma regra explícita em dois passos: (1) a primeira release do Collector após o lançamento de uma nova versão menor N do Go adiciona etapas de build e teste para a versão N; e (2) a primeira release após o lançamento de N remove o suporte para a versão N-2, sendo que binários oficiais das distribuições são compilados com a série menor mais recente do Go.

## Por que importa
Quem desenvolve receivers, processors ou exporters customizados ou usa o OpenTelemetry Collector Builder precisa atualizar sua toolchain Go regularmente, pois remover o suporte a uma versão Go não suportada (N-2) e elevar a versão mínima de patch dentro de uma série menor suportada não são considerados breaking changes.

## Como funciona
Ao manter componentes customizados que importam go.opentelemetry.io/collector, acompanhe os lançamentos menores do Go para migrar de N-2 para N-1 ou N antes da primeira release subsequente do Collector.

## Exemplo
Quando o Go lança uma nova versão menor (por exemplo, de 1.23 para 1.24), a release seguinte do Collector passa a testar a nova série e encerra o suporte à série duas versões atrás.

## Limites e trade-offs
Mesmo dentro de uma versão menor suportada do Go, a versão mínima de patch exigida pode subir ao longo do tempo para acomodar atualizações de dependências sem que isso conte como mudança incompatível.

## Como verificar
Conferi a seção Compatibility no README oficial de open-telemetry/opentelemetry-collector.

## Conexões
- [[otelcol-otlp-protocol-version-stability]] — Veja também: Suporte nativo ao protocolo OTLP v1.10.0 e definição de estabilidade do protocolo.
- [[otelcol-cosign-image-signature-verification]] — Veja também: Verificação criptográfica de assinaturas das imagens oficiais com Sigstore Cosign.

## Fontes
- [OpenTelemetry Collector — README oficial](https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/README.md) — README oficial do OpenTelemetry Collector com proposta vendor-agnostic, cinco objetivos, versão OTLP v1.10.0, política de versões menores N e N-2 do Go, verificação cosign e governança do SIG.; consultado em 2026-10-03.
- [Repositório oficial open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector) — Repositório oficial do OpenTelemetry Collector no GitHub com docs/vision.md, docs/security-best-practices.md, código-fonte e releases.; consultado em 2026-10-03.
