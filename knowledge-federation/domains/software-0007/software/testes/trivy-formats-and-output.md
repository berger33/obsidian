---
id: software.testes.tranche18.001246
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://trivy.dev/latest/docs/", "https://github.com/aquasecurity/trivy"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Trivy: escolher formato de saída

## Em uma frase
A ferramenta gera saída em tabela para leitura e em formatos estruturados, inclusive padronizados para intercâmbio com outras ferramentas.

## Por que importa
O formato estruturado integra o resultado ao pipeline e permite tendência histórica, enquanto a tabela serve à inspeção rápida.

## Como funciona
Use tabela no desenvolvimento, publique formato estruturado como artefato e encaminhe o resultado padronizado ao painel de segurança quando existir.

## Exemplo
O formato de intercâmbio permite que o sistema de acompanhamento agregue os achados de várias aplicações em um único lugar.

## Limites e trade-offs
Saídas volumosas sem política de retenção ocupam espaço, e formatos proprietários dificultam a integração com ferramentas de terceiros.

## Como verificar
Gere os dois formatos da mesma varredura e confirme que a contagem de achados coincide entre eles.

## Conexões
- [[trivy-ci-policy]] — Veja também: Trivy: definir política no pipeline.
- [[trivy-limits-and-practices]] — Veja também: Trivy: reconhecer limites da varredura.

## Fontes
- [Trivy — Documentation](https://trivy.dev/latest/docs/) — alvos, verificadores, políticas, exceções e formatos de saída; consultado em 2026-10-03.
- [Trivy — repositório oficial](https://github.com/aquasecurity/trivy) — código-fonte, alvos suportados e documentação do projeto; consultado em 2026-10-03.
