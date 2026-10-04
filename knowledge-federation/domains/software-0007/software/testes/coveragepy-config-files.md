---
id: software.testes.tranche16.000994
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
fontes: ["https://coverage.readthedocs.io/en/6.5.0/config.html", "https://coverage.readthedocs.io/en/6.5.0/cmd.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# coverage.py: centralizar regras na configuração

## Em uma frase
As opções podem ser declaradas em arquivo próprio, no arquivo de configuração do projeto ou no empacotamento, com precedência definida.

## Por que importa
Configuração versionada evita divergência entre execuções locais e no pipeline e documenta as escolhas de medição do projeto.

## Como funciona
Declare fontes, ramos, exclusões e limites no arquivo versionado, mantendo a linha de comando restrita ao que varia por execução.

## Exemplo
Um projeto pode definir o pacote de origem, ativar ramos e registrar o limite mínimo de cobertura em um único ponto de configuração.

## Limites e trade-offs
Seções duplicadas em arquivos diferentes criam disputa silenciosa, e a ferramenta escolhe um deles conforme a ordem de busca.

## Como verificar
Execute com e sem arquivo de configuração explícito e compare os efeitos relatados para confirmar qual origem está sendo aplicada.

## Conexões
- [[coveragepy-branch-coverage]] — Veja também: coverage.py: habilitar cobertura de ramos.
- [[coveragepy-omit-and-exclude]] — Veja também: coverage.py: excluir o que não deve ser medido.

## Fontes
- [coverage.py — Configuration](https://coverage.readthedocs.io/en/6.5.0/config.html) — arquivos de configuração, fontes, omissões, exclusões e limites; consultado em 2026-10-03.
- [coverage.py — Command line](https://coverage.readthedocs.io/en/6.5.0/cmd.html) — comandos run, combine, report, xml, json e html com suas opções; consultado em 2026-10-03.
