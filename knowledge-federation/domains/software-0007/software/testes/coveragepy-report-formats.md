---
id: software.testes.tranche16.000998
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

# coverage.py: escolher formatos de saída

## Em uma frase
A ferramenta gera resumo em terminal, página navegável, formato estruturado e formato de intercâmbio, todos derivados dos mesmos dados.

## Por que importa
Cada formato atende a um consumo diferente: leitura humana, navegação por código, integração com esteira e interoperabilidade com outras ferramentas.

## Como funciona
Gere a página para investigação local e o formato estruturado para o pipeline, ativando a listagem de linhas ausentes no resumo de terminal.

## Exemplo
O resumo com linhas ausentes aponta diretamente o trecho não executado, dispensando abrir a página para cada arquivo.

## Limites e trade-offs
Relatórios gerados a partir de dados antigos descrevem revisão diferente do código analisado e induzem a conclusão errada sobre o estado atual.

## Como verificar
Gere os formatos a partir do mesmo arquivo de dados e verifique se os totais apresentados coincidem entre eles.

## Conexões
- [[coveragepy-fail-under]] — Veja também: coverage.py: falhar o build por limite de cobertura.
- [[coveragepy-contexts]] — Veja também: coverage.py: separar medições por contexto.

## Fontes
- [coverage.py — Command line](https://coverage.readthedocs.io/en/6.5.0/cmd.html) — comandos run, combine, report, xml, json e html com suas opções; consultado em 2026-10-03.
- [coverage.py — Configuration](https://coverage.readthedocs.io/en/6.5.0/config.html) — arquivos de configuração, fontes, omissões, exclusões e limites; consultado em 2026-10-03.
