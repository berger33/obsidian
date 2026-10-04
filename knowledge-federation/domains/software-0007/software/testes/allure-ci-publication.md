---
id: software.testes.tranche18.001256
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
fontes: ["https://allurereport.org/docs/", "https://github.com/allure-framework/allure2"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Allure: publicar o relatório no pipeline

## Em uma frase
O gerador produz página estática que pode ser publicada como artefato do trabalho ou em serviço de hospedagem de relatórios.

## Por que importa
Publicação automática reduz o esforço de compartilhar resultado e mantém o link disponível para toda a equipe.

## Como funciona
Gere e publique em etapa dedicada, preserve o diretório de histórico e defina retenção coerente com o tamanho dos anexos.

## Exemplo
O relatório publicado pode ser referenciado diretamente na revisão que introduziu a mudança avaliada.

## Limites e trade-offs
Relatórios com anexos grandes e sem retenção crescem indefinidamente, e a publicação de resultados com dados sensíveis exige controle de acesso.

## Como verificar
Publique o relatório de duas execuções seguidas e confirme que o histórico e as tendências aparecem atualizados.

## Conexões
- [[allure-suites-and-behaviors]] — Veja também: Allure: navegar por suítes e comportamentos.
- [[allure-limits-and-practices]] — Veja também: Allure: reconhecer limites do relatório.

## Fontes
- [Allure Report — Documentation](https://allurereport.org/docs/) — resultados, passos, anexos, histórico, tendências e publicação; consultado em 2026-10-03.
- [Allure — repositório oficial](https://github.com/allure-framework/allure2) — gerador de relatório, exemplos e documentação do projeto; consultado em 2026-10-03.
