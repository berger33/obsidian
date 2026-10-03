---
id: software.devops.tranche01.000008
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
fontes: ["https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/docs/component-stability.md", "https://github.com/open-telemetry/opentelemetry-collector"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Os três requisitos obrigatórios de testes para graduação de um componente a Stable

## Em uma frase
Na subseção Testing requirements dentro de Stable em docs/component-stability.md, todo componente Stable DEVE possuir uma suíte abrangente de testes composta por três exigências: (1) cobertura de testes que supere o maior valor entre 80% e o mínimo global do repositório (cobrindo todas as opções de configuração e exibida na documentação do componente); (2) pelo menos um teste de ciclo de vida (lifecycle test) que valide a inicialização com configuração válida e a propagação de contexto; e (3) pelo menos um teste de benchmark para cada sinal estável, com link na documentação para a execução mais recente dos resultados.

## Por que importa
Exigir no mínimo 80% de cobertura de código, teste de ciclo de vida e benchmarks publicados por sinal estável impede que um componente receba o selo Stable apenas por tempo de existência sem comprovação empírica de desempenho e inicialização limpa.

## Como funciona
Ao propor a graduação de um componente para Stable (ou ao auditar a maturidade de um componente crítico), verifique se o README do componente exibe a cobertura >= 80%, o lifecycle test e o link para os benchmarks de cada sinal estável.

## Exemplo
Se um componente busca graduar para Stable tanto em métricas quanto em traces, ele precisa manter pelo menos um benchmark dedicado para métricas e outro para traces, ambos linkados na documentação.

## Limites e trade-offs
Os requisitos de documentação de um componente Stable incluem ainda documentar todas as feature gates, recursos próprios de auto-observabilidade e, se o componente mantiver estado (stateful), como configurar armazenamento persistente e desligamento/reinício gracioso.

## Como verificar
Conferi as subseções Testing requirements e Documentation requirements de Stable em docs/component-stability.md.

## Conexões
- [[otelcol-beta-and-stable-configuration-deprecation-rules]] — Veja também: Garantias de configuração em Beta e Stable: depreciação com WARN e prazo N+2 ou 6 meses.
- [[otelcol-internal-telemetry-and-security-best-practices]] — Veja também: Auto-observabilidade, práticas de segurança e verificação contínua via OSS-Fuzz.

## Fontes
- [OpenTelemetry Collector — Stability Levels and versioning](https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/docs/component-stability.md) — Documento oficial docs/component-stability.md com os seis níveis de estabilidade por sinal, regras de depreciação em Beta/Stable (N+2 ou 6 meses) e requisitos de testes em Stable.; consultado em 2026-10-03.
- [Repositório oficial open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector) — Repositório oficial do OpenTelemetry Collector no GitHub com docs/vision.md, docs/security-best-practices.md, código-fonte e releases.; consultado em 2026-10-03.
