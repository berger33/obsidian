---
id: software.testes.tranche16.000999
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://coverage.readthedocs.io/en/6.5.0/cmd.html", "https://coverage.readthedocs.io/en/6.5.0/config.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# coverage.py: separar medições por contexto

## Em uma frase
Cada execução pode receber um rótulo e os relatórios podem filtrar por expressão sobre esses contextos, distinguindo o que cada tipo de teste cobre.

## Por que importa
Saber se uma linha é exercitada por teste unitário ou por teste de integração orienta onde investir esforço e evita duplicação de cenários.

## Como funciona
Atribua rótulos por suíte ou grupo de casos, mantenha a convenção simples e consulte o relatório filtrado quando a pergunta for sobre origem da cobertura.

## Exemplo
Execuções de testes rápidos e de integração com rótulos distintos permitem verificar se o caminho de erro é coberto apenas pela suíte lenta.

## Limites e trade-offs
Contextos multiplicam o volume de dados e exigem disciplina de nomenclatura, e a filtragem não altera o total combinado quando todos os rótulos são considerados.

## Como verificar
Gere o relatório com e sem filtro de contexto e confirme que as diferenças correspondem às suítes rotuladas.

## Conexões
- [[coveragepy-report-formats]] — Veja também: coverage.py: escolher formatos de saída.
- [[coveragepy-subprocesses]] — Veja também: coverage.py: medir código executado em subprocessos.

## Fontes
- [coverage.py — Command line](https://coverage.readthedocs.io/en/6.5.0/cmd.html) — comandos run, combine, report, xml, json e html com suas opções; consultado em 2026-10-03.
- [coverage.py — Configuration](https://coverage.readthedocs.io/en/6.5.0/config.html) — arquivos de configuração, fontes, omissões, exclusões e limites; consultado em 2026-10-03.
