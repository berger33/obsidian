---
id: software.devops.tranche01.000010
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/README.md", "https://github.com/open-telemetry/opentelemetry-collector"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Governança do SIG OpenTelemetry Collector: rotação de horários e GitHub como fonte da verdade

## Em uma frase
A seção Community do README explica como o SIG do OpenTelemetry Collector opera: presença no canal #otel-collector do Slack da CNCF, reuniões semanais por vídeo que rotacionam entre três horários (terça às 17:00 PT, quarta às 09:00 PT e quarta às 05:00 PT para permitir que pessoas de qualquer fuso participem de pelo menos uma a cada três reuniões), convites abertos em #otel-collector-dev para discussões ad-hoc e a regra áurea de governança: "Remember that our source of truth is GitHub: every decision made via Slack or video calls has to be recorded in the relevant GitHub issue."

## Por que importa
Em projetos distribuídos globalmente, se decisões arquiteturais ficarem restritas a quem pôde comparecer a uma chamada de vídeo síncrona ou a uma thread efêmera no Slack, contribuidores de outros fusos ficam excluídos e o histórico técnico se perde; exigir o registro na issue do GitHub mantém a governança auditável.

## Como funciona
Use as chamadas semanais rotativas ou o canal #otel-collector para destravar PRs, buscar um sponsor para um componente novo ou colher opiniões, mas registre sempre toda decisão tomada na respectiva issue ou pull request do GitHub.

## Exemplo
O próprio README lista os quatro propósitos típicos das chamadas de vídeo: conhecer as pessoas por trás do projeto, obter opinião sobre propostas específicas, procurar um sponsor para um componente proposto após tentar via GitHub/Slack e chamar atenção para um PR travado.

## Limites e trade-offs
Antes de pedir um sponsor na chamada de vídeo para um componente novo, a recomendação explícita do README é já ter tentado o contato prévio via GitHub e Slack e incluir o link da issue ou PR na pauta da reunião.

## Como verificar
Conferi a seção Community no README oficial de open-telemetry/opentelemetry-collector.

## Conexões
- [[otelcol-internal-telemetry-and-security-best-practices]] — Veja também: Auto-observabilidade, práticas de segurança e verificação contínua via OSS-Fuzz.

## Fontes
- [OpenTelemetry Collector — README oficial](https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/README.md) — README oficial do OpenTelemetry Collector com proposta vendor-agnostic, cinco objetivos, versão OTLP v1.10.0, política de versões menores N e N-2 do Go, verificação cosign e governança do SIG.; consultado em 2026-10-03.
- [Repositório oficial open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector) — Repositório oficial do OpenTelemetry Collector no GitHub com docs/vision.md, docs/security-best-practices.md, código-fonte e releases.; consultado em 2026-10-03.
