---
id: software.devops.tranche01.000007
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
fontes: ["https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/docs/component-stability.md", "https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Garantias de configuração em Beta e Stable: depreciação com WARN e prazo N+2 ou 6 meses

## Em uma frase
Na seção Beta (aplicável também a Stable) de docs/component-stability.md, o projeto estabelece regras estritas para alterações de configuração: ao adicionar uma nova opção obrigatória, ela DEVE vir com um valor padrão sensato; ao renomear ou remover uma opção, ela DEVE ser depreciada em uma versão emitindo log de nível WARN com link para o guia de migração no repositório do componente, DEVE ser mantida na versão N+1 (podendo ficar atrás de feature gate em N+2) e NÃO DEVE ser removida antes de N+2 ou 6 meses (o que ocorrer por último).

## Por que importa
Operadores de plataforma não podem ter instâncias do Collector falhando na inicialização após uma atualização menor por causa de uma chave YAML renomeada sem aviso; a janela mínima de N+2 ou 6 meses com log WARN dá tempo previsível para migrar os manifestos.

## Como funciona
Monitore mensagens de nível WARN nos logs de inicialização do Collector após cada upgrade de versão e siga o link do guia de migração indicado antes que a janela de duas versões menores ou 6 meses se encerre.

## Exemplo
Em componentes Stable, a documentação acrescenta que a compatibilidade entre versões menores é obrigatória, salvo quando problemas críticos de segurança exigirem mudança com caminho de migração documentado.

## Limites e trade-offs
O documento faz uma ressalva importante ao remover uma opção em Beta/Stable: a opção já PODE ser tornada não operacional na própria versão em que foi depreciada, mesmo que a chave continue aceita no arquivo de configuração até N+2 ou 6 meses para não quebrar o startup.

## Como verificar
Conferi as subseções Configuration changes de Beta e Stable em docs/component-stability.md.

## Conexões
- [[otelcol-component-stability-tiers-per-signal]] — Veja também: Os seis níveis de estabilidade de componentes por sinal: Development a Unmaintained.
- [[otelcol-stable-component-testing-requirements]] — Veja também: Os três requisitos obrigatórios de testes para graduação de um componente a Stable.

## Fontes
- [OpenTelemetry Collector — Stability Levels and versioning](https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/docs/component-stability.md) — Documento oficial docs/component-stability.md com os seis níveis de estabilidade por sinal, regras de depreciação em Beta/Stable (N+2 ou 6 meses) e requisitos de testes em Stable.; consultado em 2026-10-03.
- [OpenTelemetry Collector — README oficial](https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/README.md) — README oficial do OpenTelemetry Collector com proposta vendor-agnostic, cinco objetivos, versão OTLP v1.10.0, política de versões menores N e N-2 do Go, verificação cosign e governança do SIG.; consultado em 2026-10-03.
