---
id: software.testes.tranche15.000877
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://coverage.readthedocs.io/en/latest/", "https://coverage.readthedocs.io/en/latest/branch.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# coverage.py: não interpretar linha executada como comportamento validado

## Em uma frase
Uma linha registrada como coberta prova que o interpreter passou por ela durante a medição, não que o teste tenha confirmado a saída, a exceção ou o estado que deveria resultar.

## Por que importa
Mesmo relatório de 100% em linhas pode omitir saídas de condicionais, interações com I/O, invariantes e requisitos; branch coverage acrescenta oportunidades de destino, mas tampouco demonstra que as expectativas do teste são adequadas.

## Como funciona
Contextos ajudam a localizar a origem, não a julgar sua força.

## Exemplo
Para cada requisito importante, associe testes com assertions explícitas e use cobertura para detectar lacunas de execução; combine-a com revisão de casos limite, mutation testing ou inspeção de comportamento quando necessário.

## Limites e trade-offs
Metas numéricas podem incentivar exclusões ou testes que apenas percorrem código; cobertura é uma evidência de seleção, não um certificado de correção.

## Como verificar
Escolha alguns branches críticos e verifique no corpo dos testes se existe expectativa capaz de falhar quando a implementação viola o contrato, não apenas se as linhas ficam verdes.

## Conexões
- [[coverage-py-source-detecta-arquivos-nao-executados]] — Veja também: coverage.py: declarar source para incluir módulos sem execução.
- [[coverage-py-relatorios-formatados-e-fail-under]] — Veja também: coverage.py: escolher formato de relatório e aplicar limite de cobertura.

## Fontes
- [Coverage.py 7.16.2 — Documentation](https://coverage.readthedocs.io/en/latest/) — origem medida, capacidades e visão geral dos relatórios; consultado em 2026-10-02.
- [Coverage.py 7.16.2 — Branch coverage measurement](https://coverage.readthedocs.io/en/latest/branch.html) — destinos parciais, linhas ausentes e pragma no branch; consultado em 2026-10-02.
