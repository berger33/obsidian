---
id: software.testes.tranche18.001250
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

# Allure: anexar evidências ao resultado

## Em uma frase
Arquivos podem ser anexados ao teste ou a um passo específico, com tipo declarado, incluindo texto, imagem e conteúdo estruturado.

## Por que importa
Evidência ligada ao passo exato reduz o tempo de diagnóstico e evita reproduzir a falha localmente.

## Como funciona
Anexe no momento da falha, escolha o tipo adequado ao conteúdo e limite o volume para manter o relatório utilizável.

## Exemplo
Uma captura de tela anexada ao passo de confirmação mostra o estado da interface no instante do erro.

## Limites e trade-offs
Anexar tudo em todas as execuções infla o relatório e pode expor dados sensíveis capturados nas telas.

## Como verificar
Compare o tamanho do relatório de uma execução com e sem anexos em casos aprovados e defina a política de retenção.

## Conexões
- [[allure-steps]] — Veja também: Allure: descrever passos do teste.
- [[allure-categories]] — Veja também: Allure: classificar falhas por categoria.

## Fontes
- [Allure Report — Documentation](https://allurereport.org/docs/) — resultados, passos, anexos, histórico, tendências e publicação; consultado em 2026-10-03.
- [Allure — repositório oficial](https://github.com/allure-framework/allure2) — gerador de relatório, exemplos e documentação do projeto; consultado em 2026-10-03.
