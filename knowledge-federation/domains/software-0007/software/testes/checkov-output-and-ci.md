---
id: software.testes.tranche19.001314
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://github.com/bridgecrewio/checkov", "https://github.com/bridgecrewio/checkov-action"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Checkov: publicar o resultado na esteira

## Em uma frase
A execução gera saída legível e formatos estruturados, e a esteira pode falhar por política ou apenas reportar.

## Por que importa
O formato estruturado integra o resultado ao acompanhamento, e a política de falha define o que bloqueia a entrega.

## Como funciona
Gere formato estruturado como artefato, escolha a política de falha conforme a maturidade e publique o resumo na revisão de código.

## Exemplo
Um trabalho pode começar apenas reportando, passar a falhar em achados de risco alto e depois endurecer o critério.

## Limites e trade-offs
Sem política de falha o relatório é ignorado, e falhar por todo achado desde o primeiro dia inviabiliza o fluxo de entrega.

## Como verificar
Ajuste a política para o nível atual do projeto e confirme que o trabalho falha exatamente nos achados previstos.

## Conexões
- [[checkov-custom-policies]] — Veja também: Checkov: escrever políticas próprias.
- [[checkov-terraform-checks]] — Veja também: Checkov: análise de configuração declarada.

## Fontes
- [Checkov — repositório oficial](https://github.com/bridgecrewio/checkov) — código-fonte, verificações e documentação do projeto; consultado em 2026-10-03.
- [Checkov — Ação do GitHub](https://github.com/bridgecrewio/checkov-action) — integração publicada para pipelines; consultado em 2026-10-03.
