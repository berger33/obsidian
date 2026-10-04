---
id: software.testes.tranche22.001659
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://gcovr.com/en/stable/index.html", "https://gcovr.com/en/stable/manpage.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# gcovr: quando lcov basta e quando não

## Em uma frase
A resposta oficial à pergunta "qual a diferença entre gcovr e lcov?" estrutura a escolha: ambos rodam o gcov, mas o gcovr nasceu dos sumários de texto e dos relatórios XML que o lcov não oferecia, mantendo também o HTML com detalhes por arquivo.

## Por que importa
Times que só querem HTML2 do lcov ganham pouco migrando; o valor aparece quando CI, portal e badge precisam do mesmo número de uma fonte só.

## Como funciona
O --lcov do gcovr fecha o ciclo de coexistência: quem depende do formato .info para diff-cover ou Codecov pode adotar gcovr sem trocar o resto da esteira.

## Exemplo
A matriz de output do índice inclui ainda Clover e SonarQube, territórios que o tooling clássico de gcov não cobre nativamente.

## Limites e trade-offs
Branch coverage continua sendo a fronteira política entre as duas ferramentas — a FAQ do gcovr assume que o usuário chega brigando com branches C++.

## Como verificar
Gere o mesmo run como --lcov no gcovr e lcov --capture + geninfo e compare as linhas LF/LH dos arquivos instrumentados.

## Conexões
- [[gcovr-versions]] — Veja também: gcovr: ciclo de release visível na doc.

## Fontes
- [gcovr — documentação inicial (8.6)](https://gcovr.com/en/stable/index.html) — definição, matriz de formatos de saída e índice da doc; consultado em 2026-10-03.
- [gcovr — Command Line Reference](https://gcovr.com/en/stable/manpage.html) — filtros, exclusões, config keys e --no-markers; consultado em 2026-10-03.
