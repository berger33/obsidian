---
id: software.testes.tranche18.001248
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

# Allure: gerar relatório a partir de resultados

## Em uma frase
A execução dos testes grava arquivos de resultado em diretório próprio, e o gerador transforma esse conjunto em relatório navegável estático.

## Por que importa
A separação entre coleta e geração permite arquivar o resultado bruto e regerar o relatório sem repetir a suíte.

## Como funciona
Configure o diretório de resultados na ferramenta de teste, gere o relatório em etapa separada e preserve os arquivos brutos como artefato.

## Exemplo
Um resultado combinado de várias suítes pode gerar um único relatório consolidado da execução completa.

## Limites e trade-offs
Resultados de execuções diferentes misturados no mesmo diretório produzem relatório incoerente, e a limpeza entre execuções precisa ser explícita.

## Como verificar
Gere o relatório de uma execução, apague o diretório de resultados e confirme que o relatório estático continua navegável.

## Conexões
- [[allure-steps]] — Veja também: Allure: descrever passos do teste.

## Fontes
- [Allure Report — Documentation](https://allurereport.org/docs/) — resultados, passos, anexos, histórico, tendências e publicação; consultado em 2026-10-03.
- [Allure — repositório oficial](https://github.com/allure-framework/allure2) — gerador de relatório, exemplos e documentação do projeto; consultado em 2026-10-03.
